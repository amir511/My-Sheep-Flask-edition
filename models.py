import os
from peewee import SqliteDatabase
from peewee import Model
from peewee import (CharField, BlobField, 
                    BooleanField, ForeignKeyField,
                    TextField,DateField,
                    DateTimeField,)

db = SqliteDatabase('data.db')

class BaseModel(Model):
    class Meta:
        database = db    

class Stage(BaseModel):
    name = CharField()

    def __repr__(self):
        return 'Stage object: ' + self.name

class Klass(BaseModel):
    id = CharField()
    stage = ForeignKeyField(Stage, related_name='classes')
    
    def __repr__(self):
        return 'Klass object: ' + self.id + '/' +self.stage  
    
class Sheep(BaseModel):
    name = CharField()
    klass = ForeignKeyField(Klass ,related_name="sheeps")
    picture = BlobField()
    address = TextField()
    mobile = CharField(max_length=22)
    home_number = CharField(max_length=22)
    father_number = CharField(max_length=22)
    mother_number = CharField(max_length=22)
    grandparent_number = CharField(max_length=22)
    other_number_1 = CharField(max_length=22)
    other_number_2 = CharField(max_length=22)
    other_address = TextField()
    confession_father = CharField()
    birthday = DateField()
    school = CharField()
    email = CharField()
    comments = TextField()


    def __repr__(self):
        return 'Sheep object: ' + self.name

class Servant(BaseModel):
    name = CharField()
    klass = ForeignKeyField(Klass, related_name="servants")
    leader_of = ForeignKeyField(Klass, related_name="leader")
    is_admin  = BooleanField()

    def __repr__(self):
        return 'Servant object: ' + self.name
    

class Visit(BaseModel):
    sheep = ForeignKeyField(Sheep, related_name='visits')
    servants = TextField()
    visit_date = DateTimeField()
    comments = TextField()
    
    def __repr__(self):
        return 'Visit object, to: ' + self.sheep.name + ' on: ' + self.visit_date
    
class Attendance(BaseModel):
    class_id = ForeignKeyField(Klass, related_name='attendances')
    date = DateField()

    def __repr__(self):
        return 'Attendance object for class: ' + self.class_id + ' on: ' + self.date

class AttendanceRecord(BaseModel):
    sheep = ForeignKeyField(Sheep)
    attendance = ForeignKeyField(Attendance)

# Append this list whenever you add new models
TABLES_LIST = [
    Klass,
    Sheep,
    Servant,
    Visit, 
    Attendance,
    AttendanceRecord,
    ]

def main():
    try:
        print("Checking if old database file exists ")
        os.remove('data.db')
        print("Database file was found and removed")
    except:
        print("No old database found")
    print("Creating the database...")
    db.connect()
    db.create_tables(TABLES_LIST)
    db.close()
    print('Done')

if __name__ == '__main__':
    main()
