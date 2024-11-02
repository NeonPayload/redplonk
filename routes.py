import uuid
from flask import Flask, request, render_template, redirect, url_for
import app
from models import user, hosts
from flask_login import login_user, logout_user, current_user, login_required
from scan import *

def register_routes(app, db, bcrypt):
    
    @app.route('/', methods=["GET", "POST"])
    def index():
        if current_user.is_authenticated:
            return render_template('index.html')
        else:
            return render_template("login.html")

    @app.route('/logout')
    def logout():
        logout_user()
        return "logged out"

    @app.route('/login', methods=["GET", "POST"])
    def login():
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == "POST":
            user_account = request.form.get("username")
            user_password = request.form.get("password")

            logged_in_user = user.query.filter(user.username == user_account).first()

            if logged_in_user.password == user_password:
                login_user(logged_in_user)
                host_list = hosts.query.order_by(hosts.uid).all()
                return render_template('index.html', hosts=host_list)
            else:
                return "account login error"

    @app.route('/handle_url_params') # test function 
    def handle_params():
        return str(request.args)

    @app.route('/404') # temp holding place for admin page with no session or 404 redirect
    def redirect_endpoint():
        return redirect(url_for('404'))
    
    # app route for create user
    @app.route('/createuser', methods=["GET", "POST"])
    def createuser():
        if request.method == "GET":
            return render_template("createuser.html")
        elif request.method == "POST":
            user_account = request.form.get("username")
            user_password = request.form.get("password")
            confirm_password = request.form.get("password2")

            if user_password == confirm_password:
                #hashed_password = bcrypt.generate_password_hash(user_password) # figure out why TypeError: Bcrypt.generate_password_hash() missing 1 required positional argument: 'password'
                #new_account = user(username = user_account, password = hashed_password)

                new_account= user(username = user_account, password = user_password)

                db.session.add(new_account)
                db.session.commit()

                new_account = user.query.all()
                return redirect(url_for('index'))

            elif user_account != confirm_password:
                return print("Password doesn't match try again")

    @app.route('/scan', methods=["GET", "POST"])
    def scan():
        if request.method == "GET":
            return render_template("scan.html")
        elif request.method == "POST":
            scan_item_list = request.files["scan_item_list"]
                
            try:
                for list_item in scan_item_list:
                    print("[debug] list_item " + list_item)
                    host_item = internetdb(list_item)
                    new_host = hosts(internetdb = host_item)
                
                    db.session.add(new_host)
                    db.session.commit()
            except:
                print("error: no scan item or scan item blank")

        else:
            return render_template("login.html")
