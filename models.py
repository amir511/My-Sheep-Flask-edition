import os
from peewee import SqliteDatabase
from peewee import Model
from peewee import CharField, BlobField, BooleanField, IntegerField, ForeignKeyField

db = SqliteDatabase('data.db')

class Klass(Model):
    name = CharField()
    parent_stage = CharField()
    
    def __repr__(self):
        return 'Klass object: ' + self.name + '/' +self.parent_stage  
    
    class Meta:
        database = db

class Sheep(Model):
    name = CharField()
    klass = ForeignKeyField(Klass ,related_name="sheeps")

    def __repr__(self):
        return 'Sheep object: ' + self.name
    class Meta:
        database = db

class Servant(Model):
    name = CharField()
    klass = ForeignKeyField(Klass, related_name="servants")
    leader_of = ForeignKeyField(Klass, related_name="leader")
    
    def __repr__(self):
        return 'Servant object: ' + self.name
    
    class Meta:
        database = db


class Visit(Model):
    pass

class Attendance(Model):
    pass


# Append this list whenever you add new models
TABLES_LIST = [
    Klass,
    Sheep,
    Servant,
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
