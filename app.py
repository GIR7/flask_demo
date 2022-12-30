#Created by Yihui, learn about flask
# 12/29/2022

import datetime
from flask import Flask,render_template,request
app = Flask(__name__)

# @app.route('/')
# def test_hello():
#     return 'Hello World from flask demo! This is Yihui'

# @app.route('/index')
# def test_hello():
#     return 'Hello World from flask demo index page! This is Yihui'

# @app.route('/user/<usrname>') 
# @app.route('/user/<int:id>') 
# def test_hello(usrname):
#     return 'Welcome %s! I am Yihui'%usrname

#return the rendered page to user using jinja2
# @app.route('/')
# def index2():
#     return render_template("index.html")

#pass an arg to page
@app.route('/')
def index3():
    time = datetime.date.today() #regular arg
    name = ['A','B','C','D'] #list arg
    task = {"Task 1":"Opening office","Task 2":"Clean the table","Task 3":"Refill water"}#dictoinary
    return render_template("index.html",var_time = time,var_name = name,task = task)


#submit a form
@app.route('/form')
def form_test():
    return render_template("form.html")

#recieved form result page, specifiy the post method
@app.route('/result',methods=['POST','GET'])
def result():
    if request.method == 'POST':
        res = request.form
        return render_template("result.html",result = res)


if __name__ == '__main__':
    app.run(debug=True)