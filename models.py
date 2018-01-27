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
    class_id = CharField()
    stage = ForeignKeyField(Stage, related_name='classes')
    
    def __repr__(self):
        return 'Klass object: ' + self.class_id + '/' +self.stage  
    
class Sheep(BaseModel):
    name = CharField()
    klass = ForeignKeyField(Klass, related_name="sheeps")
    picture = BlobField(null=True)
    address = TextField(null=True)
    mobile = CharField(null=True, max_length=22)
    home_number = CharField(null=True, max_length=22)
    father_number = CharField(null=True, max_length=22)
    mother_number = CharField(null=True, max_length=22)
    grandparent_number = CharField(null=True, max_length=22)
    other_number_1 = CharField(null=True, max_length=22)
    other_number_2 = CharField(null=True, max_length=22)
    other_address = TextField(null=True)
    confession_father = CharField(null=True)
    birthday = DateField(null=True)
    school = CharField(null=True)
    email = CharField(null=True)
    comments = TextField(null=True)


    def __repr__(self):
        return 'Sheep object: ' + self.name

class Servant(BaseModel):
    name = CharField()
    email = CharField()
    password = CharField()
    klass = ForeignKeyField(Klass, related_name="servants")
    leader_of = ForeignKeyField(Klass, null=True, related_name="leader")
    is_admin = BooleanField(default=False)

    def __repr__(self):
        return 'Servant object: ' + self.name
    

class Visit(BaseModel):
    sheep = ForeignKeyField(Sheep, related_name='visits')
    servants = TextField()
    visit_date = DateTimeField()
    comments = TextField(null=True)
    
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
    Stage,
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
