from flask import Flask, render_template, flash, request,session
#from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from werkzeug.utils import secure_filename
import mysql.connector
import tkinter as tk
from tkinter import *

import datetime
import time
import yagmail
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
@app.route("/")
def homepage():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1trpiot')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM iotdata ORDER BY id DESC LIMIT 6")
    data=cursor.fetchall()

    return render_template('index.html',data=data)

@app.route("/email",methods=['GET','POST'])
def view11():
    if request.method == 'POST':
        email = request.form['email']
        lvar = request.form['lvar']
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1trpiot')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM iotdata ORDER BY id DESC LIMIT 1")
        data = cursor.fetchone()


        mail = 'testsam360@gmail.com';
        password = 'rddwmbynfcbgpywf';
        # list of email_id to send the mail
        li = [email]
        body = "X:"+str(data[0])+",Y:"+str(data[1])+",Distance:"+str(data[2])+",Switch:"+str(data[3])+",Lat-Lan Values:"+str(data[5])+","+str(data[6])+",link=https://www.google.com/maps/search/?api=1&query="+data[5]+","+data[6]
        yag = yagmail.SMTP(mail, password)
        yag.send(to=email, subject="Alert...!", contents=body)
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1trpiot')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM iotdata ORDER BY id DESC LIMIT 6")
        data1 = cursor.fetchall()

        return render_template("index.html",data=data1)
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)