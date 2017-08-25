from __future__ import unicode_literals
import bcrypt 
from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def regVal(self, postdata):
        results ={'status': True, 'errors': []}
        if len(postdata['name']) <3:
            results['errors'].append('your name must be more then 3 characters!')
        if len(postdata['username']) <3:
            results['errors'].append('your user name must be more then 3 characters!')
        if len(postdata['password'])<8:
            results['errors'].append('your password must be atleast 8 characters long!')
        if postdata['password'] != postdata['c_password']:
            results['errors'].append('your password doesnt match')
        if len(self.filter(username = postdata['username'])) >0:
            results['errors'].append('username already exsits')
        if len(results['errors']) >0:
            results['status'] = False
        print results
        return results

    def creator(self, postdata):
        hashed = bcrypt.hashpw(postdata['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(name = postdata['name'],username = postdata['username'],datehired=postdata['datehired'],password= hashed)
        return user
    def loginVal(self, postdata):
        results={'status': True, 'errors':[],'user':None}
        user = self.filter(username= postdata['username'])
        if len(user) <1:
            results['errors'].append('something went wrong with username')
        else:
            if bcrypt.checkpw(postdata['password'].encode(),user[0].password.encode()) == False:
                results['errors'].append('password did not match')
        if len(results['errors']) > 0:
            results['status'] = False
        else:
            results['user'] = user[0]
        return results

class User(models.Model):
    wish_item = models.ManyToManyField('item_app.Item', related_name='user_item')
    name =models.CharField(max_length= 255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    datehired = models.DateTimeField(auto_now=False)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    objects = UserManager()