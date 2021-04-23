from django.contrib import admin
from trell.models import User, Tags, UniversalTagScore, UserTagScore, Trail
# Register your models here.

admin.site.register(User)
admin.site.register(UniversalTagScore)
admin.site.register(UserTagScore)
admin.site.register(Tags)
admin.site.register(Trail)