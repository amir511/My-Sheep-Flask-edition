from faker import Faker
from models import Stage, Klass, Sheep, Servant, Visit, Attendance, AttendanceRecord
from random import randint
from dateutil.parser import parse
f = Faker(locale='ar')

# Create Stages
s1 = Stage(name='Preparatory')
s1.save()
s2 = Stage(name='Secondary')
s2.save()

# Create Classes
cp1 = Klass(class_id='First', stage=s1)
cp1.save()
cp2 = Klass(class_id='Second', stage=s1)
cp2.save()
cp3 = Klass(class_id='Third', stage=s1)
cp3.save()
sp1 = Klass(class_id='First', stage=s2)
sp1.save()
sp2 = Klass(class_id='Second', stage=s2)
sp2.save()
sp3 = Klass(class_id='Third', stage=s2)
sp3.save()

classes = [cp1, cp2, cp3, sp1, sp2, sp3]

# Create Data of each class
for class_ in classes:
    class_leader_flag = False

    # Create Sheeps
    for i in range(25):
        data_dict={
        'name':f.name(),
        'klass':class_,
        'address':f.address(),
        'mobile':f.phone_number(),
        'home_number':f.phone_number(),
        'father_number':f.phone_number(),
        'mother_number':f.phone_number(),
        'grandparent_number':f.phone_number(),
        'other_number_1':f.phone_number(),
        'other_number_2':f.phone_number(),
        'other_address':f.address(),
        'confession_father':f.name(),
        'birthday':parse(f.date()),
        'school':f.name(),
        'email':f.email(),
        'comments':f.text(),
        }
        sheep = Sheep.create(**data_dict)
        sheep.save()
    
    # Create Servants
    for i in range(7):
        name = f.name()
        email = f.email()
        password = f.password()
        klass = class_
        if not class_leader_flag:
            leader_of = class_
            is_admin = True
        else:
            leader_of = None
            is_admin = False        
        servant = Servant(name=name, email=email, password=password, klass=klass, 
                            leader_of=leader_of, is_admin=is_admin)
        servant.save()
        class_leader_flag = True

# Create Random visits
for class_ in classes:
    for i in range(20):
        sheep_id = randint(1,25)
        






