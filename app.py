from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods =['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    #below is temp post request method. I will replace with postgresql db once working. 
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == 'admin' and password == 'password':
            return 'success'
        else:
            return 'failure'


@app.route('/user/<account>')
def account(account):
    return f"account page based off user {account}"

@app.route('/handle_url_params') # test function 
def handle_params():
    return str(request.args)

@app.route('/404') # temp holding place for admin page with no session or 404 redirect
def redirect_endpoint():
    return redirect(url_for('404'))

if __name__ == '__main__':
    app.run(host='localhost', port=2000, debug=True)