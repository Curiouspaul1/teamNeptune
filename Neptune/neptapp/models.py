from neptapp import db,ma

class Tutors(db.Model):
    id = db.Column(db.Integer)
    name = db.String(200,nullable=False)
    email = db.String(100)
    mskill = db.String(200)
    oskill = db.String(200)
    description = db.Text()
    uid = db.Column(db.String(200))

class Students(db.Model):
    id = db.Column(db.Integer)
    uid = db.Column(db.String(200))
    name = db.String(200)
    email = db.String(200)

# Schema
class TutorSchema(ma.Schema):
    class Meta:
        fields = ('id','name','email','mskill','oksill','description','uid')

class StudentSchema(ma.Schema):
    class Meta:
        fields = ('id','uid','name','email')


# Init Schema
Tutor_schema = TutorSchema(strict=True)
Tutors_schema = TutorSchema(many=True,strict=True)

