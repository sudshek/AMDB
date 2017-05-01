# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from Users.serializers import MovieSerializer
from Users.models import user
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Users.serializers import UserSerializer
from rest_framework import filters
from django.contrib.auth.hashers import check_password, make_password
from Users.models import AccessToken
from Users.models import Movie
from Users.models import Genre
from Users.models import MovieGenre
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

    does_username_exist = user.objects.filter(username=username)

#
    if len(does_username_exist)>0:
        return Response({"error_message":"Username already exists"},status= 400)

    new_user= user.objects.create(username=username,name=name,password=make_password(password),short_bio=short_bio)
    new_user.save()
    print new_user.id
    #return Response({"message":"Congrats!! User Created!!"})
    return Response(UserSerializer(instance=new_user).data, status=200)


@api_view(['GET'])
def get_user(request):

    if 'user_id' in request.query_params:

        new_user = user.objects.filter(id=request.query_params['user_id'])
        if len(new_user)>0:
            return Response(UserSerializer(instance=new_user[0]).data,status=200)
        else :
            return Response({"error_message":"User Not Found!!"},status=200)


    else:
        user_all= user.objects.all()
        return Response(UserSerializer(instance=user_all,many=True).data,status=200)


@api_view(['POST'])
def login_user(request):
    username=request.data['username']
    password=request.data['password']

    new_user = user.objects.filter(username=username).first()
    if new_user:
        if not check_password(password, new_user.password):
            return Response({"message":"User name or password error"},status=200)


        else :
            token = AccessToken(users_id=new_user)
            token.create_token()
            print token.access_token
            token.save()
            return Response({"message":token.access_token},status=200)

    else :
        return Response({"message":"Username or password error!!"},200)



@api_view(['POST'])
def create_movie(request):
    global movie_id, movie_id
    current_user = check_token(request)
    user_id = current_user
    if current_user is not None:
        name = request.data['name']
        duration_in_minutes = request.data['duration_in_minutes']
        release_date = request.data['release_date']
        poster_picture_url = request.data['poster_picture_url']
        overall_rating = request.data['overall_rating']
        censor_board_rating = request.data['censor_board_rating']
        genre_name = request.data['genre_name']
        genres = []


        for name in genre_name:
            genre_exists = Genre.objects.filter(name=genre_name).first()
            genres.append(genre_exists)
            movie_id = Movie.id
            genre_id = Genre.id


            new_genre = MovieGenre.objects.create(genre=genre_id,movie=movie_id)
        new_movie = Movie.objects.create(name=name, release_date=release_date, duration_in_minutes=duration_in_minutes , poster_picture_url=poster_picture_url,overall_rating=overall_rating,censor_board_rating=censor_board_rating,user_id=user_id)
        new_movie.save()
        return Response(MovieSerializer(instance=new_movie).data,{"genre":genre_id,"movie":movie_id},status=200,)
    else:
        return Response("You are not authorized to perform this action!")




@api_view(['POST'])
def review_movie(request):
    current_user = check_token(request)
    if current_user is not None:
       pass

    else:
        return Response("You are not authorized to perform this action!")





def check_token(request):
    token = request.META['HTTP_TOKEN']
    token_exist = AccessToken.objects.filter(access_token = token,is_valid=True).first()
    if not token_exist:
        return None
    else:
        return token_exist.users_id

