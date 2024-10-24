import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_tennis_club.settings')

# Initialize Django
django.setup()

from members.models import Member

# Insert data into the database
member1 = Member(firstname='abhi', lastname='singh')
member2 = Member(firstname='ravi', lastname='singh')

member_list = [member1, member2]

# for x in member_list:
#     x.save()
print(Member.objects.all().values())