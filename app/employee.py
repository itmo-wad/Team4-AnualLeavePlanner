from datetime import datetime, timedelta

from flask import render_template, redirect, request, Blueprint, flash, jsonify
from bson.objectid import ObjectId
from flask_login import login_user, login_required, logout_user, current_user
from . import mongo
from .models import User
import smtplib
from email.mime.text import MIMEText
import os

employee = Blueprint('employee', __name__)


#  Route to employee dashboard
@employee.route('/employee_dashboard', methods=['GET'])
@login_required
def employee_dashboard():
    user = mongo.db.users.find_one({'username': current_user.username})
    leaves = mongo.db.leave_requests.find({'user_id': user['_id']})
    return render_template('employee_dashboard.html', user=user, leaves=leaves)


@employee.route('/employee_dashboard', methods=['POST'])
@login_required
def employee_dashboard_post():
    user = mongo.db.users.find_one({'username': current_user.username})

    # Update the user's planned_leave_days
    planned_leave_days = user['planned_leave_days']
    # Calculate the number of days between start_date and end_date
    start_date = datetime.strptime(request.form.get('start_date'), "%Y-%m-%d")
    # Here we add 1 so that the end_date is included, e.g. 2025-01-01 to 2025-01-03 is 3 days
    end_date = datetime.strptime(request.form.get('end_date'), "%Y-%m-%d") + timedelta(days=1)

    days = (end_date - start_date).days
    if days < 0:
        flash("End date cannot be before start date", "error")
        return redirect('/employee_dashboard')
    if days > user['planned_leave_days']:
        flash(f"You do not have enough leave days. You asked for {days} days, you have {user['planned_leave_days']} days", "error")
        return redirect('/employee_dashboard')

    planned_leave_days += days
    user['planned_leave_days'] = planned_leave_days
    mongo.db.users.update_one({'_id': user['_id']}, {"$set": user})

    # Create a new leave request
    leave_request = {
        "user_id": user['_id'],
        "start_date": request.form.get('start_date'),
        "end_date": request.form.get('end_date'),
        "status": "pending"
    }
    mongo.db.leave_requests.insert_one(leave_request)
    flash("Leave request submitted successfully", "success")
    return redirect('/employee_dashboard')


@employee.route('/cancel_leave/<id>', methods=['POST'])
@login_required
def cancel_leave_request(id):
    user = mongo.db.users.find_one({'username': current_user.username})
    leave_request = mongo.db.leave_requests.find_one({'_id': ObjectId(id)})
    if not leave_request:
        return jsonify({"success": False, "message": "Leave request not found"})
    if leave_request['status'] != 'pending':
        return jsonify({"success": False, "message": f"Leave request cannot be cancelled, it's already {leave_request['status']}"})
    if leave_request['user_id'] != user['_id']:
        return jsonify({"success": False, "message": "Leave request does not belong to you"})
    mongo.db.leave_requests.delete_one({'_id': ObjectId(id)})

    planned_leave_days = user['planned_leave_days']
    # Calculate the number of days between start_date and end_date
    start_date = datetime.strptime(leave_request['start_date'], "%Y-%m-%d")
    end_date = datetime.strptime(leave_request['end_date'], "%Y-%m-%d")
    # Add 1 to include the end_date
    days = (end_date - start_date).days + 1
    planned_leave_days -= days
    user['planned_leave_days'] = planned_leave_days
    mongo.db.users.update_one({'_id': user['_id']}, {"$set": user})
    return jsonify({"success": True, "message": "Leave request cancelled successfully"})