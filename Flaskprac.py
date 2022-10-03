from flask import Flask, redirect, url_for
app = Flask(__name__)   #Flask object instance를 만들기 위함.

@app.route('/admin')
def hello_admin():
    return 'admin hi'  
#어느 url이 관련 함수를 가르켜야 하는지.
# / 뒤에 경로 넣으세요

@app.route('/guest/<guest>')
def hello_guest(guest):
    return "hello %s as a guest!" %guest

@app.route('/user/<name>')
def hello_user(name):
    if name=='admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest = name))

if __name__ == '__main__':
    app.run()    #class run at local server