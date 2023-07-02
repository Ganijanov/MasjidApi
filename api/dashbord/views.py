from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers
from main import models

@api_view(['POST'])
def create_country(request):
    try:
        name = request.data['name']
        models.Cauntry.objects.create(
            name=name
        )
        data = {'success':True}
    except:
        data = {'success':False}
    return Response(data)


@api_view(["POST"])
def update_country(request, pk):
    country = models.Cauntry.objects.get(pk=pk)
    
    country.name = request.data['name']
    country.save()
    data = {'success':True}
    return Response(data)


@api_view(['GET'])
def delate_country(request, pk):
    country = models.Cauntry.objects.get(pk=pk)
    try:
        country.delete()
        data = {'success':True}
    except:
        data = {'success':False}
    return Response(data)


@api_view(['POST'])
def create_city(request):
    try:
        name = request.data['name']
        country = models.Cauntry.objects.get(name=request.data['country'])
        models.City.objects.create(
            name=name,
            cauntry=country
        )
        data = {'success':True}
    except:
        data = {'success':False}
    return Response(data)


@api_view(["POST"])
def update_city(request, pk):
    city = models.City.objects.get(pk=pk)
    try:
        city.name = request.data['name']
        city.cauntry = models.Cauntry.objects.get(name=request.data['country'])
        city.save()
    except:
        data = {'success':False}
    return Response(data)


@api_view(['GET'])
def delate_city(request, pk):
    city = models.City.objects.get(pk=pk)
    try:
        city.delete()
        data = {'success':True}
    except:
        data = {'success':False}
    return Response(data)



@api_view(['POST'])
def create_masque(request):
    try:
        admin = models.User.objects.get(username=request.user.username)
        name = request.data['name']
        city = models.City.objects.get(name=request.data['city'])
        capacity = request.data['capacity']
        bio = request.data['bio']
        models.Masque.objects.create(
            admin=admin, 
            name=name,
            city=city,
            capacity=capacity,
            bio=bio
        )
        data = {"Success": True}
    except:
        data = {"Success": False}
    return Response(data)


@api_view(['POST'])
def update_masque(request, pk):
    masque = models.Masque.objects.get(pk=pk)

    if masque.admin == request.user:
        masque.name = request.data['name']
        masque.city = models.City.objects.get(name=request.data['city'])
        masque.capacity = request.data['capacity']
        masque.bio = request.data['bio']
        masque.save()
        data = {"Success":True}
    else:
        data = {"Success": False}
    return Response(data)


@api_view(['GET'])
def delate_masque(request, pk):
    masque = models.Masque.objects.get(pk=pk)

    if masque.admin == request.user:
        masque.delete()
        data = {"Success":True}
    else:
        data = {"Success": False}
    return Response(data)