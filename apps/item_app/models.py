from __future__ import unicode_literals
from ..login_app.models import User
from django.db import models

# Create your models here.
class ItemManager(models.Manager):
    def itemVal(self, postdata, user):
        #passed in user to beable to append to "my list" making it able to only show that one users items
        results ={'status':False, 'errors':[]}
        if not postdata['thing'] or len(postdata['thing']) < 1:
            results['errors'].append('item must be more then 1 character')
            results['status'] = True
        if results['status'] == False:
            if len(self.filter(thing= postdata['thing'])) == 0:
                item = self.create(thing = postdata['thing'], added_by = user)
                #added_by is the forenign key and we are setting to the user. so when you create a thing that user has it append to his list
                user.wish_item.add(item)
                #this puts the item in the manytomany field so it can be called on later 
                print user.wish_item.all()
        else:
            results['errors'].append('item is already on list')
            results['status'] = True
        return results

class Item(models.Model):
    thing = models.CharField(max_length= 255)
    added_by = models.ForeignKey(User, null=True, related_name='user_item')
    # setting null to true prevents an integrity error. this feild needs a default.
    created_at = models.DateTimeField(auto_now_add= True)
    objects = ItemManager()
    def __str__(self):
        return " item+user:{},{}".format(self.thing,self.added_by.username)