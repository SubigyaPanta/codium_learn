from flask import Flask
from flask import render_template
from flask import request
import re

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('phone_email.html')

@app.route('/filter', methods=['POST'])
def filter():
    rawtext = request.form['rawtext']
    print(rawtext)
    email = getEmail(rawtext)
    phone = getPhone(rawtext)
    print(email, phone)
    return render_template('phone_email.html', email=email, phone=phone, rawtext=rawtext)

def getPhone(raw_text):
    PHONE_REGEX = re.compile('[0-9]{10}')
    print('phone reg', PHONE_REGEX)
    return re.findall(PHONE_REGEX, raw_text)

def getEmail(raw_text):
    EMAIL_REGEX = re.compile('[a-z0-9]+@[a-z]+\.[a-z]+')
    print('email_reg', EMAIL_REGEX)
    return re.findall(EMAIL_REGEX, raw_text)