from neptapp import app,db
from flask import json,jsonify
from neptapp.models import Tutors_schema,Tutor_schema

@app.route('/tsignup',methods=['GET','POST'])
def tsignup():
    if request.method == 'POST':
        name = request.json['name']
        email = request.json['email']
        mskill = request.json['mskill']
        oskill = request.json['oskill']
        desc = request.json['desc']
        uid = request.json['uid']
        role = request.json['role']

        tutor = Tutors(name=name,emil=email,mskill=mskill,oskill=oskill,description=desc,uid=uid,role=role)
        db.session.add(tutor)
        db.session.commit()

    return Tutor_schema.jsonify(tutor)

@app.route('/')
def index():
    return "<h1>Hello World</h1>"

@app.route('/lsignup',methods=['GET','POST'])
def lsignup():
    if request.method=='POST':
        name = request.json['name']
        email = request.json['email']
        uid = request.json['uid']
        role = request.role['uid']

        student = Students(name=name,email=email,uid=uid,role=role)
        db.session.add(student)
        db.session.commit()

    return Tutor_schema.jsonify(student)

# get single user

@app.route('/get-user',methods=['GET','POST'])
def getUser():
    uid = request.json['uid']
    userx = Tutors.query.filter_by(uid=uid).first()
    return Tutor_schema.jsonify(userx)
