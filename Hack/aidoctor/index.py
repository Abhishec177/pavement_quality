from flask import Flask, render_template, url_for, flash, redirect, jsonify
from forms import RegistrationForm, LoginForm
from firebase import firebase
import json

app = Flask(__name__)

app.config['SECRET_KEY'] = '2bb3a946fea06b5fe7eedcca853b115c'

doctors_list = [
      {
             'name' : 'barath',
             'specialization' : 'corona virus',
             'shift' : '3-6',
             'availability': '1',
             'work': '5'
      },
      {
             'name' : 'Arvinth',
             'specialization' : 'casuality',
             'shift' : '6-9',
             'availability': '1',
             'work': '5'
      }
]



@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html",title='About')

@app.route("/doctors")
def doctors():
    return render_template("doctors.html", doctors_list=doctors_list,title='List of Doctors')

@app.route("/appointments")
def appointments():
    return render_template("appointments.html", title='Appointments')


firebase = firebase.FirebaseApplication('https://ai-doctor-46ded.firebaseio.com/', None)


@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # flash(f'Account created for {form.name.data}!','success')
        data1 ={
            'Name': str(form.name.data),
            'Rno': str(form.rollno.data),
            'Password': str(form.password.data),
            'Hostel': str(form.hostel.data),
            'Mess': str(form.mess.data),
        }
        print(data1)
        result = firebase.post('/Students', data1)
        print (result)
        return redirect(url_for('home'))
    print(form.errors)
    return render_template("register.html", title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.rollno.data == '108118003' and form.password.data == 'password':
            flash('you have been logged in!','success')
            return redirect(url_for('home'))
    else:
        flash('Login unsuccessful.Please check credentials', 'danger')
    return render_template("login.html", title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
