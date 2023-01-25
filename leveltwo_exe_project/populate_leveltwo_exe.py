import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','leveltwo_exe_project.settings')

import django
django.setup()

## Fake population script
from leveltwo_exe_app.models import User
from faker import Faker

# a class in an object constructor,it's object.it don't have any value
# it has properties and method, instances created from it can utilize them.
# a new object created from base or 
# from previously constructed object is called an instance object.
# here fakegen is a instance of Faker() object

fakegen = Faker()

def populate(N=5):

  for entry in range(N):
    fake_name = fakegen.name().split()
    fake_first_name = fake_name[0]
    fake_last_name = fake_name[1]
    fake_email = fakegen.email()

    #New Entry 
    user = User.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)[0]


if __name__ == '__main__':
  print('populating database')
  populate(20)
  print('completed!')
