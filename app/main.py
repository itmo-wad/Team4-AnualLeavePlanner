from flask import render_template, redirect, request, Blueprint, flash, jsonify
from bson.objectid import ObjectId
from flask_login import login_user, login_required, logout_user, current_user
from . import mongo
from .models import User
import smtplib
from email.mime.text import MIMEText

main = Blueprint('main', __name__)

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "example@example.com"
SENDER_PASSWORD = "example"

def send_email(to_email, username, password):
    """Sends an email with login details."""
    subject = "Welcome to our website! Your login details"
    body = f"""
    Hello {username},

    Your account has been created.

    Credentials:
    - Username: {username}
    - Password: {password}

    Please log in and change your password.

    Best regards,
    Your Company Team
    """

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_email

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
        server.quit()
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Error sending email : {e}")

        
# We probably want to return main page at /, maybe dynamic page depending on user type
@main.route('/')
@login_required
def index():
    user = mongo.db.users.find_one({'username': current_user.username})
    if user['isManager']:
        return redirect('/manager_dashboard')  # Redirect to manager dashboard
    else:
        return redirect('/employee_dashboard') # Redirect to employee dashboard

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')

#  Route to manager dashboard
@main.route('/manager_dashboard')
@login_required
def manager_dashboard():
    user = mongo.db.users.find_one({'username': current_user.username})
    return render_template('manager_dashboard.html', user=user)

#  Route to employee dashboard
@main.route('/employee_dashboard')
@login_required
def employee_dashboard():
    user = mongo.db.users.find_one({'username': current_user.username})
    return render_template('employee_dashboard.html', user=user)

@main.route('/manager_dashboard/manage_employee', methods=['GET', 'POST'])
@login_required
def manage_employee():
    if not current_user.isManager:
        return redirect('/login')  

    if request.method == 'POST':
        surname = request.form.get('surname')
        firstname = request.form.get('firstname')
        email = request.form.get('email')

        username = email.split("@")[0]  # Generate an email-based username
        password = User.generate_employee_password()
        hashed_password = User.hash_password(password)

        if mongo.db.users.find_one({'email': email}):
            flash("User already exists", "warning")
        else:
            mongo.db.users.insert_one({
                "username": username,
                "surname": surname,
                "firstname": firstname,
                "email": email,
                "password": hashed_password,
                "isManager": False,
                "total_leave_days": 30,
                "planned_leave_days": 0
            })

            send_email(email, username, password)
            flash("Employee successfully added and email sent !", "success")

    employees = mongo.db.users.find({"isManager": False})
    return render_template("manage_employee.html", employees=employees)

@main.route('/update_employee/<id>', methods=['PUT'])
def update_employee(id):
    try:
        data = request.json  # Récupération des données envoyées en JSON
        mongo.db.users.update_one(
            {"_id": ObjectId(id)},
            {"$set": {
                "surname": data["surname"],
                "firstname": data["firstname"],
                "email": data["email"],
                "total_leave_days": int(data["total_leave_days"]),
                "planned_leave_days": int(data["planned_leave_days"])
            }}
        )
        return jsonify({"message": "Employee updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@main.route('/delete_employee/<id>', methods=['DELETE'])
def delete_employee(id):
    try:
        result = mongo.db.users.delete_one({"_id": ObjectId(id)})
        
        if result.deleted_count == 1:
            return jsonify({"message": "Employee deleted successfully"}), 200
        else:
            return jsonify({"message": "Employee not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
