import base64
from flask import Flask, url_for, request, render_template, make_response
from flask import request




app = Flask(__name__)
@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')
@app.route('/login', methods=['POST' , 'GET']) #login username
def login(username):
    return f'login page'


@app.route('/lands/') #list the available lands
def land_list():
    return "this returns list of lands"


@app.route('/admin/login',methods=['POST','GET']) #admin login page
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == 'secretloginpassword':
            encoded_username = base64.b64encode(username.encode()).decode()
            resp = make_response(render_template('admin_dashboard.html'))
            resp.set_cookie('Kookioe', encoded_username)
        return resp
    else:
        error = "Invalid user or password"
        return render_template('login.html', error=error)


@app.errorhandler(404)
def not_found(error):
    return render_template('err404.html'),404

if __name__ == '__main__':
    app.run()
