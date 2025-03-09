# Annual Leave Planner

This project is a web-based application designed to help employees submit and manage their annual leave requests, while allowing managers to approve or reject leave applications. The system also prevents overlapping leave requests and tracks leave balances.

## Table of Contents

[1. Installation Instructions](#1-installation-instructions)  
[2. Environment Variables Configuration](#2-environment-variables-configuration)  
[3. Features](#3-features)  
[4. Technologies Used](#4-technologies-used)  
[5. Project Structure](#5-project-structure)  
[6. Current Progress](#6-current-progress)  
[7. Running the Project](#7-running-the-project)  
[8. Contributing](#8-contributing)  
<br>


## 1. Installation Instructions 

To get the project up and running locally on your machine, follow the steps below:

1. **Clone the repository**

   ```bash
   git clone https://github.com/itmo-wad/Team4-AnualLeavePlanner.git
   cd annual-leave-planner
   ```
   
2. **Set up a Python virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Windows, use `venv\Scripts\activate`
   ```
   
3. **Install dependencies**
   ```bash
	pip install -r requirements.txt
   ```
   
4. **Set up MongoDB**
	Ensure MongoDB is running locally or start with docker
   ```bash
   docker run --name mongodb -p 27017:27017 -d mongodb/mongodb:latest
   ```

	
6. **Run the app**
   ```bash
	python app.py
   ```
   
7. **Visit the application**
	Open your browser and navigate to http://127.0.0.1:5000/

## 2. Environment Variables Configuration
### Environment Variables

Before running the project, you will need to configure some environment variables. These values are used for email setup, authentication, and other configurations. The environment variables should be defined in a `.env` file or set directly in your environment.

#### **List of Required Environment Variables:**
```env
FLASK_ENV=production
MONGO_HOST=mongodb
MONGO_PORT=27017
MONGO_DB_NAME=leave_management
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your_email@gmail.com
SMTP_PASSWORD=your_email_password
SEND_EMAIL=True
```

#### **Explanation of the Variables:**
- **`FLASK_ENV`** → `production` or `debug` (turns flask debug on)
- **`MONGO_HOST`** → Mongodb host
- **`MONGO_PORT`** → Mongodb port
- **`MONGO_DB_NAME`** → Mongodb database name
- **`SMTP_SERVER`** → The SMTP server address used for sending emails (`smtp.gmail.com` for Gmail).
- **`SMTP_PORT`** → The port number used for SMTP communication (`587` for TLS).
- **`SMTP_USERNAME`** → The email address used for sending emails.
- **`SMTP_PASSWORD`** → The password or app-specific password for the sender's email account.
- **`SEND_EMAIL`** → A boolean value (`True` or `False`) that controls email sending:
  - `True` → Emails will be sent as expected.
  - `False` → Email sending will be **skipped**, and the manager's password will be shown instead (useful for development).
<br>



## 3. Features<br>

### User Management
- Managers can create employee accounts, assign roles, and manage users.
- Employees can log in, submit leave requests, and view leave balances.

### Leave Request System
- Employees can submit leave requests with details such as leave type, start and end dates, and optional reasons.
- Leave requests are saved with statuses: Pending, Approved, Rejected.

### Leave Approval System
- Managers can view and approve/reject leave requests with the option to add comments on rejections.

### Calendar & Conflict Prevention
- A calendar displays upcoming leave requests and prevents overlapping leave submissions.
- Employees can see their remaining leave balance.

### Security
- Role-based access control ensures only managers can approve leave or manage employee accounts.
- Passwords are securely hashed and session management is in place.
<br>


## 4. Technologies Used

- **Backend**: Flask (Python web framework)
- **Database**: MongoDB (NoSQL database)
- **Frontend**: HTML, CSS, JavaScript
- **Authentication**: Flask-Login for session management
- **Deployment**: Docker for containerization



## 5. Project Structure

The project follows a modular structure to separate concerns for better maintainability.
```
├── .gitignore
├── app.py                  # Main application file
├── docker-compose-debug.yml
├── docker-compose.yml
├── Dockerfile
├── README.md               # This file
├── requirements.txt        # Python dependencies
├── app/
│   ├── auth.py             # Authentication-related logic
│   ├── calendar.py         # Logic for leave calendar and conflict resolution
│   ├── employee.py         # Employee leave request logic
│   ├── main.py             # Main app routes
│   ├── models.py           # Database models
│   ├── __init__.py         # Application initialization
├── static/                 
│   ├── dashboard.css       # Styles for dashboard
│   ├── manage_employee.css # Styles for employee management page
│   ├── manage_employee.js  # JS for employee management page
├── templates/
│   ├── employee_dashboard.html  # Employee dashboard page
│   ├── index.html              # Homepage
│   ├── login.html              # Login page
│   ├── manager_dashboard.html  # Manager dashboard page
│   ├── manage_employee.html    # Employee management page
│   ├── register.html           # Registration page
```
<br>

## 6. Current Progress

### **Design Tasks**
1. **Login/Register (#1)**: Done ✅
2. **Manager Dashboard (#2)**: Done ✅
3. **Employee Dashboard (#3)**: Done ✅
4. **Manage Employees Dashboard (#4)**: Done ✅
5. **Leave Approvals (#5)**: Done ✅

### **Feature Tasks**
1. **Login/Registration (#6)**: Done ✅
2. **Manager Employee Dashboard (#7)**: Done ✅
3. **Leave Request Form (#8)**: Done ✅
4. **Leave Approval Dashboard (#9)**: Done ✅
5. **Handle Conflicts (#10)**: Done ✅

### **Next Steps**
- Implement new features
<br>


## 7. Running the Project

1. **Local Development**

   Follow the steps in the [1. Installation Instructions](#1-installation-instructions) section above to set up the environment and run the app locally

2. **Docker Setup**

   To run the app in a containerized environment using Docker, use the following commands:
	```bash
	   docker-compose up --build
	 ```
	This will build the necessary containers and start the application
<br>

## 8. Contributing

We welcome contributions! If you'd like to improve the project, please follow these steps:

1. Fork the repository
2. Create a new branch
	```bash
	   git checkout -b feature/your-feature
	 ```
5. Make your changes and commit them
	```bash
	   git commit -am 'Add new feature'
	 ```
7. Push the changes
	```bash
	   git push origin feature/your-feature
	 ```
9. Submit a pull request
