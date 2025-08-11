# KenFlask - Local Setup Guide

## Quick Start
This is your complete KenFlask web application. Follow these steps to run it on your local machine.

## Prerequisites
- Python 3.8+ installed
- PostgreSQL database (or you can use SQLite for development)

## Installation Steps

### 1. Set up Python Environment
```bash
# Create virtual environment
python -m venv kenflask_env

# Activate virtual environment
# On Windows:
kenflask_env\Scripts\activate
# On Mac/Linux:
source kenflask_env/bin/activate
```

### 2. Install Dependencies
```bash
pip install flask flask-sqlalchemy flask-login flask-wtf flask-migrate
pip install werkzeug email-validator psycopg2-binary gunicorn
```

### 3. Environment Variables
Create a `.env` file in the project directory:
```bash
# For local development
DATABASE_URL=sqlite:///kenflask.db
SESSION_SECRET=your-secret-key-here-change-this
FLASK_ENV=development
```

### 4. Initialize Database
```bash
python -c "
from app import app, db
with app.app_context():
    db.create_all()
    print('Database created!')
"
```

### 5. Create Your User Account
```bash
python -c "
from app import app, db
from models import User
with app.app_context():
    user = User()
    user.username = 'NyexXx'
    user.email = 'donnyexx@gmail.com'
    user.set_password('kenflask123')
    db.session.add(user)
    db.session.commit()
    print('User account created!')
"
```

### 6. Run the Application
```bash
python main.py
```

Your application will be available at: http://localhost:5000

## Login Credentials
- Username: `NyexXx`
- Password: `kenflask123`

## File Structure
```
kenflask/
├── app.py              # Main application factory
├── main.py             # Application entry point
├── config.py           # Configuration settings
├── models.py           # Database models
├── routes.py           # URL routes and views
├── forms.py            # Form definitions
├── templates/          # HTML templates
│   ├── base.html      # Base template
│   ├── index.html     # Home page
│   ├── login.html     # Login page
│   ├── dashboard.html # User dashboard
│   └── pricing.html   # Pricing page
└── static/            # CSS, JS, images
    ├── css/
    └── js/
```

## Features Included
- User registration and authentication
- Personal dashboard
- Professional pricing page
- Responsive Bootstrap UI
- PostgreSQL/SQLite database support
- Security features (password hashing, CSRF protection)

## Customization
1. Edit `templates/` files to change the UI
2. Modify `routes.py` to add new pages
3. Update `models.py` to add database tables
4. Customize `config.py` for your environment

## Production Deployment
For production, use:
```bash
gunicorn --bind 0.0.0.0:5000 main:app
```

## Support
This is your personal copy of the KenFlask application. You own all the code and can modify it however you want for your web products.