from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask import jsonify
import json
import requests
import importlib
import time
from datetime import datetime
import random


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Log in first')
            return redirect(url_for('login'))
    return wrap()


app = Flask(__name__)



app.secret_key = 'kwame'

@app.route('/', methods=['GET','POST'])
def home():
    #request = requests.get('http://api.ip2proxy.com/?ip=8.8.8.8&key=demo&package=PX2')
    #ip = request.json()
    #ccode = ip['countryCode']
    return render_template('homepage.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            flash('Wrong login credentials')
        else:
            session['logged_in'] = True
            flash('You are logged in')
            return redirect(url_for('home'))
            
    return render_template('login.html')

@app.route('/bmi', methods=['GET','POST'])
def bmi():
    return render_template('bmi.html')

@app.route('/guess',methods=['GET','POST'])
def guess():
    ran  = str(random.randrange(1, 10))
    return render_template('guess.html', ran=ran)

@app.route('/heart', methods=['GET','POST'])
def heart():
    if request.method == 'POST':
        global c
        c=int(request.form['age'])
        rr = int(request.form['rhr'])
        d = c
    intensity = [55,60,65,70,75,80,85,90,95]
    return render_template('heart.html', inte=intensity)

@app.route('/get_ip', methods=['GET','POST'])
def get_ip():
    now = datetime.now()
    a = now.strftime('%M')
    ip = jsonify({'ip': request.remote_addr}), 200
    #return jsonify({'ip': request.remote_addr}), 200
    return render_template('ip.html',imp0rt = importlib.import_module, a=a)

@app.route('/word', methods=['GET','POST'])
def word():
    count = 0
    mount = 0
    i=0
    if request.method == 'POST':
        words = request.form['word']
        with open('word.text', 'w') as word:
            word.write(words)
        for i in words:
            i = i
            count+=1
        with open('word.text') as word:
            if 'python' or 'Python' in word:
                mount = True
            else:
                mount = False
    return render_template('word.html', count=count, mount=mount)

@app.route('/temp',methods=['GET','POST'])
def temp():
    if request.method == 'POST':
        if request.form['one'] == 'ono1':
            num = request.form['ctfn']
            val = num/1*33.8
    return render_template('temp.html', val=val)

ans = ['']
count = 0
@app.route('/similar', methods=['GET','POST'])
def similar():
    global ans
    if request.method == 'POST':
        sought = request.form['search']
        sought = str(sought)
        parameter = {"rel_rhy":""}
        parameter["rel_rhy"] = sought
        print(parameter)
        ww = requests.get('https://api.datamuse.com/words', parameter)
        api = ww.json()
        if request.form['searchbut'] == 'searchload':
            ans = ['']
            for i in api:
                ans.append(i['word'])
    return render_template('similar.html', ans=ans, count=count)

@app.route('/search', methods=['GET','POST'])
def search():
    with open('amazon.json','r') as zon:
        prod = json.load(zon)

    return render_template('search.html', prod=prod,)



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)