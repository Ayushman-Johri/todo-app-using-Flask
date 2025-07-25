from flask import Flask, redirect, session, flash, url_for, Blueprint, render_template, request

auth_bp = Blueprint('auth', __name__)  # ✅ Corrected Blueprint import and usage

USER_CREDENTIAL = {
    'username': 'admin',
    'password': '1234'
}

@auth_bp.route('/login', methods=["POST", "GET"])  # ✅ Lowercase 'methods'
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        if username == USER_CREDENTIAL['username'] and password == USER_CREDENTIAL['password']:
            session['user'] = username
            flash('Login successful', 'success')
            return redirect(url_for('auth.dashboard'))  # Optional: Redirect to some dashboard
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged out', 'info')
    return redirect(url_for('auth.login'))  # ✅ Ensure 'auth.login' matches the blueprint and route

# Optional dashboard route for redirection
@auth_bp.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    return f"Welcome, {session['user']}!"
