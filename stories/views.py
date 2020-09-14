from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
import datetime


def index(request):
    data = dict()
    stories = story.objects.all()
    data["stories"] = stories
    data['title'] = "All stories"
    return render(request, template_name='detail/dashboard.html', context=data)


def storyDetail(request, pk):
    data = dict()
    storyObj = story.objects.get(pk=pk)
    data["story"] = storyObj
    if request.user.id not in storyObj.viewedBy:
        storyObj.viewedBy.append(request.user.id)
        storyObj.save()
    print(storyObj.viewedBy)
    data['reads'] = len(storyObj.viewedBy) - 1
    logs.objects.filter(timestamp__lt=datetime.datetime.now() - datetime.timedelta(seconds=5)).delete()
    logs.objects.create(storyId=pk,userId=request.user.id, timestamp=datetime.datetime.now())
    getViews = logs.objects.filter(storyId=pk,
                                   timestamp__lte=datetime.datetime.now(),
                                   timestamp__gte=datetime.datetime.now() - datetime.timedelta(seconds=5)) \
        .values('userId').distinct().count()
    data['views'] = getViews
    return render(request, template_name='detail/storyDetail.html', context=data)


class storyLiveViews(APIView):
    def get(self, request, pk, userId):
        logs.objects.filter(timestamp__lt=datetime.datetime.now() - datetime.timedelta(seconds=5)).delete()
        logs.objects.create(storyId=pk, userId=userId, timestamp=datetime.datetime.now())
        getViews = logs.objects.filter(storyId=pk,
                                       timestamp__lte=datetime.datetime.now(),
                                       timestamp__gte=datetime.datetime.now() - datetime.timedelta(seconds=5)) \
            .values('userId').distinct().count()
        data = dict()
        data['views'] = getViews
        return Response(data, status=status.HTTP_200_OK)
