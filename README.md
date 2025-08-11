# KenFlask - Flask Web Application Boilerplate

A comprehensive Flask web application boilerplate designed for Ken to build independent web products. This boilerplate provides a solid foundation with authentication, database integration, modern UI components, and production-ready features.

## Features

### Core Features
- **Flask Web Framework**: Built with Flask 3.1.x
- **Database Integration**: SQLAlchemy ORM with migration support
- **User Authentication**: Complete login/logout system with Flask-Login
- **Form Handling**: Flask-WTF with validation and CSRF protection
- **Modern UI**: Bootstrap 5 with dark theme support
- **Error Handling**: Custom 404/500 error pages
- **Security**: CSRF protection, password hashing, secure sessions

### Additional Features
- **Responsive Design**: Mobile-first Bootstrap layout
- **Flash Messages**: User feedback system
- **Profile Management**: User profile editing
- **Post System**: Sample CRUD functionality
- **Configuration Management**: Environment-based configuration
- **Static File Serving**: CSS, JS, and image assets
- **Development Tools**: Debug mode and logging

## Quick Start

### 1. Installation

```bash
# Clone or download the boilerplate
git clone <repository-url> kenflask
cd kenflask

# Install dependencies (create requirements.txt with these packages)
pip install flask flask-sqlalchemy flask-login flask-wtf flask-migrate werkzeug
