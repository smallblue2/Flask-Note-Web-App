# Import the necessary libraries
from flask import Blueprint, render_template, request, flash, redirect, url_for
from website.models import User
from website import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

# Create a Blueprint for auth-related views
auth = Blueprint('auth', __name__)

# Define the route for the login page with GET and POST methods
@auth.route('/login', methods=['GET', 'POST'])
def login():
    # If the request method is POST, process the submitted form data
    if request.method == 'POST':
        # Get the email and password fields from the form
        email = request.form.get('email')
        password = request.form.get('password')

        # Retrieve the user object from the database using the email field
        user = User.query.filter_by(email=email).first()

        # Check if the user exists and if the password is correct
        if user:
            if check_password_hash(user.password, password):
                # Log in the user and set the remember attribute
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                # Redirect the user to the home page
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exit.', category='error')

    # Render the login page
    return render_template('log_in.html', user=current_user)


# Define the route for logging out and require user authentication
@auth.route('/logout')
@login_required
def logout():
    # Log out the current user
    logout_user()
    flash('Logged out succesfully', category='success')
    # Redirect user to login page
    return redirect(url_for('auth.login'))


# Define the route for signing up with GET and POST methods
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    # If the request is POST, process the submitted form data
    if request.method == 'POST':
        # Get the email, first name and password fields from the form
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Perform a bunch of basic validation
        # Does the user exist?
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists', category='error')
        # Is the email more than 4 characters long?
        elif len(email) < 4:
            flash('Email must be greater than four characters', category='error')
        # Is the first name greater than 2 characters?
        elif len(first_name) < 2:
            flash('First name must be greater than two characters', category='error')
        # Do the passwords match?
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        # Is the password too short?
        elif len(password1) < 7:
            flash('Password\'s too short. Must be longer than 7 Characters', category='error')
        else:
            # Passed validation, create new user
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            # Add user to the database
            db.session.add(new_user)
            # Commit changes to the database
            db.session.commit()
            # Login the new user and set the remember attribute
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            # Redirect to home
            return redirect(url_for('views.home'))

    return render_template('sign_up.html', user=current_user)
