from neptapp import db,ma

class Tutors(db.Model):
    id = db.Column(db.Integer)
   # name = db.String(200,nullable=False)
    email = db.String(100)
    mskill = db.String(200)
    oskill = db.String(200)
    description = db.Text()
    uid = db.Column(db.String(200),primary_key=True)
    role = db.Column(db.String(100))

class Students(db.Model):
    id = db.Column(db.Integer)
    uid = db.Column(db.String(200),primary_key=True)
    name = db.String(200)
    email = db.String(200)
    role = db.Column(db.String(100))

# Schema
class TutorSchema(ma.ModelSchema):
    class Meta:
        model = Tutors

class StudentSchema(ma.ModelSchema):
    class Meta:
        model = Students


# Init Schema
Tutor_schema = TutorSchema()
Tutors_schema = TutorSchema(many=True)

