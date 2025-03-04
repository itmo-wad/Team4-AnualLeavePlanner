# Annual Leave Planner

This project is a web-based application designed to help employees submit and manage their annual leave requests, while allowing managers to approve or reject leave applications. The system also prevents overlapping leave requests and tracks leave balances.

## Table of Contents

[1. Installation Instructions](#1-installation-instructions)  
[2. Features](#2-features)  
[3. Technologies Used](#3-technologies-used)  
[4. Project Structure](#4-project-structure)  
[5. Current Progress](#5-current-progress)  
[6. Running the Project](#6-running-the-project)  
[7. Testing](#7-testing)  
[8. Contributing](#8-contributing)
<br>


## 1. Installation Instructions 

To get the project up and running locally on your machine, follow the steps below:

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/annual-leave-planner.git
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
	Ensure MongoDB is running locally
	
5. **Run the app**
   ```bash
	python app.py
   ```
   
6. **Visit the application**
	Open your browser and navigate to http://127.0.0.1:5000/
	
	
## 2. Features<br>

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


## 3. Technologies Used

- **Backend**: Flask (Python web framework)
- **Database**: MongoDB (NoSQL database)
- **Frontend**: HTML, CSS, JavaScript
- **Authentication**: Flask-Login for session management
- **Deployment**: Docker for containerization



## 4. Project Structure

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

## 5. Current Progress

### **Design Tasks**
1. **Login/Register (#1)**: Done ✅
2. **Manager Dashboard (#2)**: Done ✅
3. **Employee Dashboard (#3)**: In Progress 🔄
4. **Manage Employees Dashboard (#4)**: Not Started 🚧
5. **Leave Approvals (#5)**: Not Started 🚧

### **Feature Tasks**
1. **Login/Registration (#6)**: Done ✅
2. **Manager Employee Dashboard (#7)**: Not Started 🚧
3. **Leave Request Form (#8)**: In Progress 🔄
4. **Leave Approval Dashboard (#9)**: Not Started 🚧
5. **Handle Conflicts (#10)**: Not Started 🚧

### **Next Steps**
- **Focus on completing the Employee Dashboard (#3)** and the **Leave Request Form (#8)**.
- Start **Manage Employees Dashboard (#4)** to allow managers to create, view, and manage employee accounts.
- Implement the **Leave Approval Dashboard (#9)** where managers can approve or reject leave requests.
- Resolve overlapping leave requests by developing the **Handle Conflicts (#10)** feature, which ensures no double bookings.
<br>


## 6. Running the Project

1. **Local Development**

   Follow the steps in the [1. Installation Instructions](#1-installation-instructions) section above to set up the environment and run the app locally

2. **Docker Setup**

   To run the app in a containerized environment using Docker, use the following commands:
	```bash
	   docker-compose up --build
	 ```
	This will build the necessary containers and start the application
<br>


## 7. Testing

To test the application:

1. **Unit Tests**: We recommend writing unit tests for each module to ensure everything functions correctly. You can use the unittest or pytest framework

2. **Manual Testing**: Test the application manually by submitting leave requests, approving/rejecting them, and ensuring there are no conflicts
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
