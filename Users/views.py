# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from Users.models import users
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Users.serializers import UserSerializer

@api_view(['POST'])
def create_user(request):
    name = request.data['name']
    username = request.data['username']
    password = request.data['password']
    short_bio = request.data['short_bio']
    print name,username,password,short_bio
    if name is None or len(name)==0:
        return Response ({"error_message": "Name field cannot be empty"}, status=400)

    if username is None or len(username)==0:
        return Response({"error_message": "Username can not be empty"},status=400)
    if password is None or len(password)<=6:
        return Response({"error_message": "Password should not be empty or less than 6 characters long"},status=400)
    #return HttpResponse(True)

    does_username_exist = users.objects.filter(username=username).first()


    if users is not None :
        return Response({"error_message":"Username already exists"},status = 400)

    new_user= users.objects.create(username=username,name=name,password='password',short_bio=short_bio)
    new_user.save()
    print new_user.id
    #return Response({"message":"Congrats!! User Created!!"})
    return Response(UserSerializer(instance=new_user).data, status=200)
    return HttpResponse(True)
