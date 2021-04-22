from django.contrib.auth import get_user_model,backends
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

    

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        print(request, username, password)
        try:
            user = UserModel.objects.get(Q(email__iexact=username))
        except UserModel.DoesNotExist:
            print("does not exists")
            return None
        else:
            if user.check_password(password):
                print("returning user")
                return user
            print("password wrong")
        return None