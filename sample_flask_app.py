#!/usr/bin/python

from flask import Flask
from flask import request
import json
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
host="localhost",
user="root",
database="strawhatpirates")

def insertData(data):
	mycursor = mydb.cursor()
	sql = "INSERT INTO pirates (name, food, age, bloodgrp) VALUES (%s, %s, %s, %s)"
	mycursor.execute(sql, data)
	mydb.commit()


@app.route('/details',methods=["GET"])
def addition():
	name = request.args.get("name")
	age = request.args.get("age")
	food = request.args.get("food")
	bloodgrp = request.args.get("bloodgrp")
	data = (name,food,int(age),bloodgrp)
	insertData(data)
	return "inserted {}".format(data)
	
@app.route('/database',methods=["GET"])
def database():
	mycursor=mydb.cursor()
	mycursor.execute("SELECT * FROM pirates;")
	myresult=mycursor.fetchall()
	d=[]
	for i in myresult:
		a={}
		a["name"]=i[1]
		a["food"]=i[2]
		a["age"]=i[3]
		a["bloodgrp"]=i[4]
		d.append(a)	
	return json.dumps(d)
		
		

		

@app.route("/mul",methods=["POST"])
def multiply():
	a = request.json.get("a",0)
	b = request.json.get("b",0)
	return str(int(a)*int(b))

if __name__ == '__main__':
   app.run(host="0.0.0.0",port=8080)
