from datetime import datetime, timedelta
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
            end_date = datetime.strptime(leave_request['end_date'], "%Y-%m-%d") + timedelta(days=1)
            data.append({
                "title": "Leave",
                "start": leave_request['start_date'],
                "end": end_date.strftime("%Y-%m-%d"),
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
            end_date = datetime.strptime(leave_request['end_date'], "%Y-%m-%d") + timedelta(days=1)
            data.append({
                "title": f"{user['surname']} {user['firstname']}",
                "start": leave_request['start_date'],
                "end": end_date.strftime("%Y-%m-%d"),
                "backgroundColor": user.get('color', 'blue'),
                # Info so we can grab it on click
                "id": str(leave_request['_id']),
                "status": leave_request['status'],
                "email": user['email']
            })

        # Changes color for both overlapping leaves, O(n^2) complexity
        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                if data[i]['start'] <= data[j]['start'] <= data[i]['end']:
                    data[i]['borderColor'] = "red"
                    data[j]['borderColor'] = "red"
        # data = check_overlapping_leaves(data)
        return jsonify(data)

def check_overlapping_leaves(leave_requests):
    # Changes color for one overlapping leave, O(n log n) complexity?
    # Sort leave requests by start date
    leave_requests.sort(key=lambda x: x['start'])

    # Initialize the end date of the previous leave request
    prev_end = None

    for leave in leave_requests:
        if prev_end and leave['start'] <= prev_end:
            leave['borderColor'] = "red"
        prev_end = max(prev_end, leave['end']) if prev_end else leave['end']

    return leave_requests
