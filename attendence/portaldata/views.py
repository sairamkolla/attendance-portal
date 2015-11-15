from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from collections import OrderedDict
from models import *
from serializers import *
from models import *
import json

# Create your views here.
# api for requirement 5

def adddefaultclasses(request):
    presentyear = datetime.datetime.now().year
    temp = datetime.datetime.now().month
    if temp > 7 :
        presentsem = 1
    else:
        presentsem = 2
    presentday = datetime.datetime.now().strftime("%A")
    days = [['Sunday','1'],['Monday','2'],['Tuesday','3'],['Wednesday','4'],['Thursday','5'],['Friday','6'],['Saturday','7']]
    for day in days :
        if presentday == day[0]:
            presentday = int(day[1])
            break
    defaultclasses = Schedule.objects.filter(course__year = presentyear,course__sem = presentsem,day = presentday)

    for defaultclass in defaultclasses:
        newclass = Conducted_Classes(course = defaultclass.course,from_time = defaultclass.from_time, to_time = defaultclass.to_time, date = str(datetime.datetime.now().date()), room = defaultclass.room, instructor = defaultclass.instructor)
        newclass.save()

        return HttpResponseRedirect()
@api_view(['POST'])
def changeconducted(request):
    """
    :param request: classid , decision
    :return: message on getting successfully executed
    """
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
# api for requirement 6
@api_view(['POST'])
def addnewclass(request):
    """
    :param request: fromtime,totime,who,roomid,courseid
    :return: message on sucesss
    """
    postdata = json.loads(request.body)
    #yearno = int(postdata['year'])
    #semno = int(postdata['sem'])
    fromtime = str(postdata['fromtime']) + ':00'
    totime = str(postdata['totime']) + ':00'
    who = postdata['who']
    roomkey = ClassRoom.objects.get(id = int(postdata['roomid']))
    coursekey = Course.objects.get(id = int(postdata['courseid']))

    newclass = Conducted_Classes( from_time = fromtime, to_time = totime,room = roomkey , course = coursekey, instructor = who)
    newclass.save()

    return Response({'response':'newclass added sucessfully'})
# api for requirement 7
@api_view(['POST'])
def addattendance(request):
    """

    :param request: classid,rollnumberstring
    :return: message on success
    """
    postdata = json.loads(request.body)
    classkey = Conducted_Classes.objects.get(id = int(postdata['classid']))
    rollnumberstring = str(postdata['rollnumbers'])

    rollnumberstring = rollnumberstring.split(',')

    for rollnumber in rollnumberstring:
        newattendance = Attendance(conductedclass = classkey, student = Student.objects.get(rollno = int(rollnumber)))
        newattendence.save()

    return Response({"response":"all attendances are added"})


#api for requirement 1
@api_view(['GET','POST'])
def returnAllConductedClasses(request):
    if request.method == 'GET':
        listOfConductedClasses = Conducted_Classes.objects.all()
        serializer = fetchConductedClasses(listOfConductedClasses, many=True)
        return Response(serializer.data)

#api for requirement 2
@api_view(['GET','POST'])
def returnAllRooms(request):
    if request.method == 'GET':
        listOfRooms = ClassRoom.objects.all()
        serializer = fetchRooms(listOfRooms, many=True)
        return Response(serializer.data)

#api for requirement 4
@api_view(['GET','POST'])
def returnAllCourses(request):
    if request.method == 'GET':
        listOfCourses = Course.objects.all()
        serializer = fetchCourses(listOfCourses, many=True)
        return Response(serializer.data)
