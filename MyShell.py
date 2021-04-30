import os 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

import django
django.setup()

from MainApp.models import Topic
from MainApp.models import Entry

topics = Topic.objects.all()
Entry = Entry.objects.all()

t = Topic.objects.get(id=1) #this is another way of getting same info as bellow
print(t)
entries = t.entry_set.all() #this retrives all entries as before
print(entries)


from django.contrib.auth.models import User

for user in User.objects.all():
    print(user.username, user.id)


'''
for t in topics:
    print(f"Topic ID: {t.id} and Topic Name: {t}")
    print(f"Date added: {t.date_added}")

for e in Entry:
    print(f"Topic: {e.topic} ")
    print(f"Entry: {e.text}")
    '''