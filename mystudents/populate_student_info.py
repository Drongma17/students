import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mystudents.settings')
import django
django.setup()

from testapp.models import Student
from faker import Faker
from random import *
fake = Faker()
def phonenumbergen():
    d1=randint(7,9)
    num='' +str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
        return int(num)
    def populate(n):
        frollno=fake.random_int(min=1, max=999)
        fname=fake.name()
        fdob=fake.date()
        fmarks=fake.random_int(min=1, max=100)
        femail=fake.email()
        fphonenumber=phonenumbergen()
        faddress=fake.address()
        student_record=Student.objects.create(frollno=frollno,name=fname,dob=fdob,marks=fmarks,email=femail,phonenumber=fphonenumber,address=faddress)
    populate(30)

