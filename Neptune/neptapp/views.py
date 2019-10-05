from neptapp import app,db
from flask import json,jsonify

@app.route('/tsignup',methods=['GET','POST'])
def tsignup():
    if request.method == 'POST':
        name = request.json['name']
        email = request.json['email']
        mskill = request.json['mskill']
        oskill = request.json['oskill']
        desc = request.json['desc']
        uid = request.json['uid']

        tutor = Tutors(name=name,emil=email,mskill=mskill,oskill=oskill,description=desc,uid=uid)
        db.session.add(tutor)
        db.session.commit()


@app.route('/lsinup',methods=['GET,'POST])
def lsignup():
    if request.method=='POST':
        name = request.json['name']
        email = request.json['email']
        uid = request.json['uid']
