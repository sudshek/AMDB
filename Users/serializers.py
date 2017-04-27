from rest_framework.serializers import ModelSerializer
from models import users

class UserSerializer(ModelSerializer):
    class Meta:
       model = users
       fields = ('id','name','username','short_bio')
