# KenFlask - Flask Web Application Boilerplate

## Overview

KenFlask is a comprehensive Flask web application boilerplate designed to provide a solid foundation for building independent web products. It features a traditional server-side rendered architecture with modern UI components, user authentication, and database integration. The application follows Flask best practices with a modular structure and includes essential features like user management, post creation, and profile management.

## System Architecture

### Backend Architecture
- **Framework**: Flask 3.1.x with application factory pattern
- **Database**: SQLAlchemy ORM with Flask-Migrate for database migrations
- **Authentication**: Flask-Login for session management with secure password hashing
- **Forms**: Flask-WTF for form handling with CSRF protection
- **Configuration**: Environment-based configuration management

### Frontend Architecture
- **Template Engine**: Jinja2 templates with template inheritance
- **CSS Framework**: Bootstrap 5 with dark theme support
- **JavaScript**: Vanilla JavaScript with Bootstrap components
- **Icons**: Font Awesome for consistent iconography
- **Responsive Design**: Mobile-first approach with Bootstrap grid system

### Application Structure
```
KenFlask/
├── app.py              # Application factory and configuration
├── config.py           # Configuration classes
├── models.py           # SQLAlchemy models
├── forms.py            # WTForms form definitions
├── routes.py           # Flask routes and view functions
├── main.py             # Application entry point
├── templates/          # Jinja2 templates
├── static/            # CSS, JS, and static assets
└── migrations/        # Database migration files
```

## Key Components

### User Management System
- **User Model**: Complete user profile with authentication capabilities
- **Registration/Login**: Form-based authentication with validation
- **Profile Management**: User profile editing functionality
- **Session Management**: Secure session handling with Flask-Login

### Post Management System
- **Post Model**: Content creation and management
- **CRUD Operations**: Create, read, update, delete functionality
- **Publishing System**: Draft/published post states
- **Author Relationships**: Posts linked to user accounts

### Security Features
- **CSRF Protection**: Enabled across all forms
- **Password Hashing**: Werkzeug security for password storage
- **Session Security**: Secure cookie configuration
- **Input Validation**: Server-side form validation

### UI Components
- **Navigation**: Responsive navbar with user-specific menus
- **Dashboard**: User-specific content management interface
- **Error Pages**: Custom 404 and 500 error handling
- **Flash Messages**: User feedback system with auto-dismiss

## Data Flow

1. **User Registration**: Form submission → validation → password hashing → database storage
2. **Authentication**: Login form → credential verification → session creation → redirect
3. **Post Creation**: Authenticated user → form submission → validation → database storage
4. **Profile Management**: User updates → form validation → database update → confirmation

## External Dependencies

### Python Packages
- **Flask**: Core web framework
- **Flask-SQLAlchemy**: Database ORM integration
- **Flask-Login**: User session management
- **Flask-WTF**: Form handling and CSRF protection
- **Flask-Migrate**: Database migration support
- **Werkzeug**: Security utilities and middleware

### Frontend Dependencies
- **Bootstrap 5**: UI framework loaded via CDN
- **Font Awesome**: Icon library via CDN
- **Bootstrap JavaScript**: Interactive components

## Deployment Strategy

### Development Environment
- **Database**: SQLite for local development
- **Debug Mode**: Enabled for development with detailed error pages
- **Hot Reload**: Flask development server with auto-restart

### Production Considerations
- **Environment Variables**: Configuration through environment variables
- **Session Security**: Secure cookie settings for production
- **Database**: Configurable database URI for production databases
- **Proxy Support**: ProxyFix middleware for deployment behind reverse proxies

### Configuration Management
- **Development Config**: Debug mode with SQLite database
- **Production Config**: Secure settings with environment-based configuration
- **Session Management**: Configurable session lifetime and security settings

## Changelog

```
Changelog:
- July 06, 2025. Initial setup
- July 06, 2025. Added professional pricing page with three-tier layout (Basic/Professional/Enterprise)
- July 06, 2025. Fixed Flask-Login compatibility issues and model constructors
- July 06, 2025. Resolved database column naming issue (is_active -> active) for user registration
- July 06, 2025. Fixed login system by bypassing redirect issues and directly rendering dashboard
- July 06, 2025. Created user account for Ken with preferred credentials
```

## User Preferences

```
Preferred communication style: Simple, everyday language.
```