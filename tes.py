import requests
import json
from flask import Flask, render_template, url_for, redirect
#lid = input('Enter a word:')
fruits= ['orange','strawberry','watermelon','mango']
#print(lid[-5:])
#a = str(input('Enter the word: ' ))

#parameter = {"rel_rhy":""}
#parameter["rel_rhy"]= a
#print(parameter)
#request = requests.get('https://api.datamuse.com/words', parameter)
#rhyme = request.json()

#s = ['']
#for i in rhyme:
#    s.append(i['word'])
#print(s)
#for i in s:
#    print(i)

with open('amazon.json','r') as zon:
    prod = json.load(zon)
p = ['']
im = ['']
for i in prod:
    p.append(i['price'])
    im.append(i['image'])
del([im[0]])

#print(im[0])
#bmi = 23.0
#c = range(1.8, 44)
#for i in c:
 #   if i == bmi:
    #    print('No')
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('pro.html')


if __name__ == '__main__':
    app.run(debug=True)