from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from urllib.parse import urlparse
from app import db
from models import User, Post
from forms import LoginForm, RegistrationForm, PostForm, ProfileForm

# Create blueprints
main_bp = Blueprint('main', __name__)
auth_bp = Blueprint('auth', __name__)

# Main routes
@main_bp.route('/')
def index():
    """Home page"""
    posts = Post.query.filter_by(published=True).order_by(Post.created_at.desc()).limit(5).all()
    return render_template('index.html', posts=posts)

@main_bp.route('/dashboard')
@login_required
def dashboard():
    """User dashboard"""
    user_posts = current_user.posts.order_by(Post.created_at.desc()).all()
    return render_template('dashboard.html', posts=user_posts)

@main_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    """User profile management"""
    form = ProfileForm(current_user.username, current_user.email)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        db.session.commit()
        flash('Your profile has been updated!', 'success')
        return redirect(url_for('main.profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
    return render_template('profile.html', form=form)

@main_bp.route('/pricing')
def pricing():
    """Pricing page"""
    return render_template('pricing.html')

@main_bp.route('/create_post', methods=['GET', 'POST'])
@login_required
def create_post():
    """Create a new post"""
    form = PostForm()
    if form.validate_on_submit():
        post = Post()
        post.title = form.title.data
        post.content = form.content.data
        post.published = form.published.data
        post.user_id = current_user.id
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.dashboard'))
    return render_template('create_post.html', form=form)

# Authentication routes
@auth_bp.route('/test-login')
def test_login():
    """Simple test login page"""
    return render_template('test_login.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        remember = request.form.get('remember_me')
        
        print(f"DEBUG: Login attempt - Username: {username}, Password: {'*' * len(password) if password else 'None'}")
        
        if username and password:
            user = User.query.filter_by(username=username).first()
            print(f"DEBUG: User found: {user is not None}")
            if user and user.check_password(password):
                login_user(user, remember=bool(remember))
                print(f"DEBUG: Login successful for {username}")
                # Directly render dashboard instead of redirecting
                user_posts = user.posts.order_by(Post.created_at.desc()).all()
                return render_template('dashboard.html', posts=user_posts, user=user, success_message=f'Welcome back, {user.full_name}!')
            else:
                print(f"DEBUG: Login failed for {username}")
                flash('Invalid username or password', 'danger')
        else:
            print(f"DEBUG: Missing credentials - Username: {username}, Password: {password}")
            flash('Please enter both username and password', 'danger')
    
    form = LoginForm()
    return render_template('login.html', form=form)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """User registration"""
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User()
        user.username = form.username.data
        user.email = form.email.data
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now registered!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    """User logout"""
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.index'))
