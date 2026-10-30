import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from study_dash.service import get_service_container
from study_dash.repository import StudentRepository
from study_dash.entity import Student

from sqlite3 import IntegrityError

bp = Blueprint('auth', __name__, url_prefix='/auth')

def get_student_repository() -> StudentRepository:
    """
    Shorthand to access the student repository service.m
    """
    return get_service_container().get_service(StudentRepository)

@bp.route('/register', methods=('GET', 'POST'))
def register():
    """
    Flask View Function to register a new user.
    Displays a form on GET and creates a new user on POST.
    Redirects user to login on user creation success.
    """
    if request.method == 'POST':
        matrikel_nr = request.form['matrikel_nr']
        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        error = None

        if not matrikel_nr:
            error = 'matrikel number is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                student_repository = get_student_repository()
                student_repository.insert_student(matrikel_nr=matrikel_nr, password_hash=generate_password_hash(password), first_name=first_name, last_name=last_name)
            except IntegrityError:
                error = f"User with matrikel number {matrikel_nr} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    """
    Flask View Function to login a user.
    Displays the login form and handles the login process.
    redirects to the index page after successful login.
    """
    if request.method == 'POST':
        matrikel_nr = request.form['matrikel_nr']
        password = request.form['password']
        student_repository = get_student_repository()
        error = None
        student = student_repository.find_by_matrikel_nr(matrikel_nr)

        if student is None:
            error = 'Incorrect matrikel number.'
        elif not check_password_hash(student.password, password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['student_id'] = student.id
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    """
    If a student is logged in, they are loaded into `g.student`.
    """
    student_id = session.get('student_id')

    if student_id is None:
        g.student = None
    else:
        g.student = get_student_repository().find_by_id(student_id)

def get_student() -> Student|None:
    """
    Returns the currently logged in student or `None`.
    """
    return g.get('student')

@bp.route('/logout')
def logout():
    """
    Flask View Function to logout a user.
    """
    session.clear()
    return redirect(url_for('index'))


def login_required(view):
    """
    Decorator to require a student to be logged in.
    """

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if get_student() is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view