from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name,  password=None):
        email = self.normalize_email(email)
        user = User(email =  email,
         first_name = first_name, last_name= last_name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, first_name, last_name,  password=None):
        email = self.normalize_email(email)
        user = User(email =  email,
                first_name = first_name, last_name= last_name)
        user.is_superuser = True            
        user.is_staff = True    
        user.set_password(password)
        user.save()
        return user
        
class User(AbstractUser):
    first_name = models.CharField(max_length=500, blank=True)
    last_name = models.CharField(max_length=500, blank=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length = 500, null=True, blank= True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name']
    EMAIL_FIELD = 'email'



class Tags(models.Model):
    """
    These are Global tags which would be created by our 
    Algorithm
    """
    tag = models.CharField(max_length=5000, unique=True)


class UniversalTagScore(models.Model):
    tag = models.ForeignKey("Tags", on_delete = models.CASCADE)
    score = models.IntegerField(default=0)



class UserTagScore(models.Model):
    tag = models.ForeignKey("Tags", on_delete = models.CASCADE)
    score = models.IntegerField(default=0)
    user = models.ForeignKey("User", on_delete = models.CASCADE)


class Trail(models.Model):
    trail = models.ImageField(upload_to="", null=True, blank = True)
    description = models.TextField(null=True, blank=True)
    trail_id = models.IntegerField(primary_key=True)
    user =  models.ForeignKey("User", on_delete = models.CASCADE)
    likes = models.IntegerField(default=0)


class Comments(models.Model):
    comment = models.CharField(max_length=500)
    trail =  models.ForeignKey("Trail", on_delete = models.CASCADE)
    user =  models.ForeignKey("User", on_delete = models.CASCADE)
    likes = models.IntegerField(default=0)
