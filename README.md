Flask User Authentication System
Overview
This project is a Flask-based user authentication system that allows users to register and log in securely. It features user-friendly forms for both registration and login, with password security measures in place such as hashing and validation. The system uses MySQL as the backend database to store user data.

Key Features:
User Registration:

Users can sign up by providing a name, email, and password.
Passwords are hashed using werkzeug.security.generate_password_hash() for secure storage.
Validation ensures the email is in the correct format and the password is at least 6 characters long.
User Login:

Registered users can log in with their email and password.
Passwords are securely compared using check_password_hash().
Flash messages provide feedback for successful or failed login attempts.
Flash Messaging:

The app provides feedback for various user actions, such as invalid credentials or successful registration, via Flask's flash() messaging system.
MySQL Database Integration:

User information is stored and retrieved from a MySQL database.
Queries are executed securely with parameterized statements to prevent SQL injection.
Secure Form Handling:

Both registration and login forms are validated to ensure correct input.
Email and password are required fields, and there’s additional server-side validation for the email format.
Technologies Used:
Flask: A lightweight Python web framework for handling HTTP requests, routing, and templating.
MySQL: Used as the relational database management system (RDBMS) to store user information.
HTML/CSS: Front-end design with custom styling for login and registration forms.
Werkzeug: Used for password hashing and checking during user authentication.
Flask-Mysqldb: Extension to connect Flask to a MySQL database.
Flask Flash Messages: For user notifications such as login success or errors.
Setup and Installation
Prerequisites:
Python 3.x installed on your system.
MySQL server installed and running.
Required Python packages (Flask, Flask-MySQLdb, Werkzeug).
