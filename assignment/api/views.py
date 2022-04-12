from django.template.response import TemplateResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .seriliazer import UserSeriliazer
from rest_framework import serializers
from rest_framework import status
from django.shortcuts import get_object_or_404



def index(request):
    context = {}
    return TemplateResponse(request, "users/index.html", context=context)
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'view': '/view',
        'Add': '/add',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }

    return Response(api_urls)


@api_view(['POST'])
def add(request):
    item = UserSeriliazer(data=request.data)

    # validating for already existing data
    if User.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view(request):

    if request.query_params:
        items = User.objects.filter(**request.query_param.dict())
    else:
        items = User.objects.all()

    serializer = UserSeriliazer(items, many=True)

    if items:
        data = UserSeriliazer(items)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update(request, pk):
    item = User.objects.get(pk=pk)
    data = UserSeriliazer(instance=item, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete(request, pk):
    item = get_object_or_404(User, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)