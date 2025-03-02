from flask import render_template, redirect, request, Blueprint, flash, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from . import mongo

calendar = Blueprint('calendar', __name__)

@calendar.route('/calendar_data', methods=['GET'])
@login_required
def calendar_data():
    # is not manager
    if not current_user.isManager:
        # return only his own leave requests
        user = mongo.db.users.find_one({'username': current_user.username})
        leave_requests = mongo.db.leave_requests.find({'user_id': user['_id']})
        data = []
        for leave_request in leave_requests:
            data.append({
                "title": "Leave",
                "start": leave_request['start_date'],
                "end": leave_request['end_date'],
                "backgroundColor": "purple"
            })
        return jsonify(data)
    # is manager
    else:
        # return all leave requests
        leave_requests = mongo.db.leave_requests.find()
        data = []
        for leave_request in leave_requests:
            user = mongo.db.users.find_one({'_id': leave_request['user_id']})
            data.append({
                "title": f"{user['surname']} {user['firstname']}",
                "start": leave_request['start_date'],
                "end": leave_request['end_date'],
                "backgroundColor": "purple"
            })
        return jsonify(data)
