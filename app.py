
from flask import *
from workwithbd import *
app = Flask(__name__)
bd = Bd("user")


@app.route('/registration', methods=['GET','POST'])
def func():
    print(request.form['login'])
    if bd.add_user(request.form['login'], request.form['password'],"",""):
        return "1"
    return "0"


@app.route('/', methods=['GET'])
def trash():
    return "This is not work"


@app.route('/', methods=['POST'])
def trash1():
    if bd.user_exist_in_table(request.form['login'], request.form['password']):
        return "1"
    return "0"


@app.route('/', methods=['POST'])
def main():

    return "true"


if __name__ == '__main__':
    app.run()
