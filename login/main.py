from flask import Flask, render_template, request, url_for,redirect, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import requests, pprint

app = Flask(__name__)
login_manager = LoginManager()

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///login.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))


# db.create_all()


@app.route('/')
def home():
    return render_template("login.html")


@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        reg_email = request.form.get('EMAIL')
        reg_name = request.form.get('NAME')
        reg_password = request.form.get('PASSWORD')
        # print(reg_email, reg_password, reg_name)

        all_posts = db.session.query(User).all()

        for user in all_posts:
            if reg_email in user.email:
                error = "You've already logged in with this email"
                return render_template('login.html', error=error)
        hashed_password = generate_password_hash(password=reg_password,
                                                 method="pbkdf2:sha256",
                                                 salt_length=8)
        new_user = User(
            name = request.form.get('NAME'),
            email = request.form.get('EMAIL'),
            password = hashed_password
        )

        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
    return render_template('login.html')

@app.route('/signin', methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        email = request.form.get('name')
        password = request.form.get('password')
        # print(email, password)

        user = User.query.filter_by(email=email).first()
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('signin'))
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user)
    # return redirect(url_for('after_login'))
    return render_template('test.html')


@app.route('/afterlogin', methods=['POST','GET'])
@login_required
def after_login():
    return render_template("test.html")


@app.route('/oper', methods=['POST'])
def oper():
        origin = request.form.get('origin')
        # locations = request.form.getlist('destinations')
        # if locations or not locations:
        #     print(locations)
        response = requests.get(
            f"https://api.tomtom.com/search/2/geocode/{origin}.json?key=xIHjaLJlArvKxQ0dzAYEKCx4W6JV0fCl")
        a = response.json()
        b = a['results'][0]['position']
        return f'{origin} : {b}'


@app.route('/route', methods=['POST'])
def handle_route():
    input_list = request.get_json()
    print(input_list)
    return 'Location list received'
    # return jsonify({'message': 'List received'})


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
