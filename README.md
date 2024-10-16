# Flask User Authentication System

A simple **Flask** web application that allows users to register and log in securely. The app integrates with a **MySQL** database to store user credentials and utilizes password hashing for secure authentication.

## Features

- **User Registration**: Users can sign up by providing their name, email, and password. Email and password fields are validated before registration.
- **Secure Password Hashing**: Passwords are stored securely using `werkzeug.security.generate_password_hash`.
- **User Login**: Users can log in with their email and password. The app checks the hashed password for verification.
- **Flash Messaging**: Provides feedback on registration success, login success, or errors like invalid credentials or duplicate accounts.
- **Responsive UI**: User-friendly HTML forms with CSS styling for both login and registration pages.

## Technologies Used

- **Flask**: A lightweight Python web framework for routing and handling requests.
- **MySQL**: The database used to store user data.
- **HTML/CSS**: Front-end design with custom styling for login and registration pages.
- **Werkzeug**: Provides password hashing and verification utilities.
- **Flask-MySQLdb**: Flask extension to integrate MySQL with Flask.
- **Flask Flash Messages**: For displaying alerts or feedback messages to users.

## Project Structure

```bash
flask-auth-system/
│
├── templates/                # HTML templates for registration and login
│   ├── register.html
│   ├── login.html
├── app.py                    # Main Flask application
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
└── static/                   # (Optional) Static files like CSS, JS, or images
