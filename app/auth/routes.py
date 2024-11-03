from flask import render_template, url_for, redirect
from . import auth

@auth.route('/signin')
def signin():
    return render_template('signin.html')


# from flask import render_template, redirect, url_for, flash, request
# from .models import db, Student, Alum
# from werkzeug.security import generate_password_hash

# from . import auth


# @auth.route('/')
# @auth.route('/signin', methods=['GET', 'POST'])
# def signin(): 
#     if request.method == "POST":
#         username = request.form['username']
#         password_hash = generate_password_hash(request.form['password'])
#         student = Student.query.filter_by(username=username).first()
#         alum = Alum.query.filter_by(username=username).first()
#         if student:
#             if student.check_password(password_hash):
#                 flash('You have successfully signed in!')
#                 return redirect(url_for('main', 'home.html'))
#             else:
#                 flash('Invalid password')
#         elif alum:
#             if alum.check_password(password_hash):
#                 flash('You have successfully signed in!')
#                 return redirect(url_for('main', 'home.html'))
#             else:
#                 flash('Invalid password')
#         else:
#             flash('Username does not exist')
#             return redirect(url_for('/signup'))
#     return render_template('/signup.html')



# @auth.route('/signup', methods=['GET', 'POST'])
# def signup(): 
#     if request.method == "POST":
#         username = request.form['username']
#         password_hash=generate_password_hash(request.form['password'])
#         if Student.query.filter_by(username=username).first() or Alum.query.filter_by(username=username).first():
#             flash('Username already exists')
#             return redirect(url_for('/signin'))
#         else:
#             if request.form['option'] == "Alum":
#                 alum = Alum(
#                     first_name = request.form['first_name'],
#                     last_name = request.form['last_name'],
#                     initial = request.form['initial'],
#                     username = request.form['username'],
#                     email = request.form['email'],
#                     password_hash = password_hash
#                 )
#                 db.session.add(alum)
#             elif request.form['option'] == "Student":
#                 student = Student(
#                     first_name = request.form['first_name'],
#                     last_name = request.form['last_name'],
#                     initial = request.form['initial'],
#                     username = request.form['username'],
#                     email = request.form['email'],
#                     password_hash = password_hash
#                 )
#                 db.session.add(student)
#             db.session.commit()

#             flash('You have successfully signed up!')
#             return redirect(url_for('/signin'))
        
#     return render_template('/signup.html')

