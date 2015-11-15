from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from collections import OrderedDict
from models import *

import json

# Create your views here.
@api_view(['POST'])
def changeconducted(request):
    postdata = json.loads(request.body)
    classid = int(postdata['classid'])
    decision = int(postdata['decision'])
    requiredclass = Conducted_Classes.objects.get(id = classid)
    if decision == 1:
        requiredclass.is_conducted = True
    else:
        requiredclass.is_conducted = False

    return Response({"Response":"Change to the particular class made sucessfully"})
##assuming time is of the format 12:00,23:32...etc
@api_view(['POST'])
def addnewclass(request):
    postdata = json.loads(request.body)
    #yearno = int(postdata['year'])
    #semno = int(postdata['sem'])
    fromtime = str(postdata['fromtime']) + ':00'
    totime = str(postdata['totime']) + ':00'
    who = postdata['who']
    roomkey = ClassRoom.objects.get(id = int(postdata['roomid']))
    coursekey = Course.objects.get(id = int(postdata['courseid']))

    newclass = Conducted_Classes( from_time = fromtime, to_time = totime,room = roomkey , course = coursekey)
    newclass.save()

    return Response({'response':'newclass added sucessfully'})
@api_view(['POST'])
def addattendance(request):
    postdata = json.loads(request.body)
    classkey = Conducted_Classes.objects.get(id = int(postdata['classid']))
    rollnumberstring = str(postdata['rollnumbers'])

    rollnumberstring = rollnumberstring.split(',')

    for rollnumber in rollnumberstring:
        newattendance = Attendance(conductedclass = classkey, student = Student.objects.get(rollno = int(rollnumber)))
        newattendence.save()

    return Response({"response":"all attendances are added"})
