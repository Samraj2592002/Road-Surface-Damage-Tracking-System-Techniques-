import os
import glob
import serial  # import serial pacakge
import sys  # import system package
import urllib3
import urllib.request
from time import sleep
import mysql.connector

arduino = serial.Serial('COM5', 9600, timeout=.1)
count = 0

while True:
    data = arduino.readline()[:-2]  # the last bit gets rid of the new-line chars

    if data:
        data = data.decode('utf-8')
        data_v = str(data)
        print(data_v)
        data_v = data_v.split(' ')
        t = data_v[0]
        h = data_v[1]
        s = data_v[2]
        r = data_v[3]
        l = data_v[4]
        la=data_v[5]
        ln=data_v[6]
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1trpiot')
        cursor = conn.cursor()
        cursor.execute("insert into iotdata values('','"+t+"','"+h+"','"+s+"','"+r+"','"+la+"','"+ln+"')")
        conn.commit()
        conn.close()





