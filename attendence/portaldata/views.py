from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from collections import OrderedDict
from models import *
from serializers import *
from models import *
import json
import datetime
from django.http import HttpResponseRedirect
# Create your views here.
# api for requirement 5
@api_view(['GET','POST'])
def adddefaultclasses(request):
    try :
        a = defaults_added.objects.get(date = datetime.datetime.now().date())
        return Response({"response": "Scheduled classes already fetched for this date"})
    except:
        newDate = defaults_added()
        newDate.save()
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
        return Response({"response":"Scheduled classes added"})

@api_view(['POST'])
def updateClassDetails(request):
    """
    to update the details of a class in database
    :param request:
    :return:
    """
    postdata = json.loads(request.body)
    print(postdata)
    print(postdata['room'])
    print(int(postdata['room']))
    classToBeChanged = Conducted_Classes.objects.get(id = postdata['id'])
    classToBeChanged.from_time = postdata['from_time']
    classToBeChanged.to_time = postdata['to_time']
    classToBeChanged.room = ClassRoom.objects.get(id=int(postdata['room']))
    classToBeChanged.instructor = postdata['instructor']
    classToBeChanged.save(update_fields=["from_time","to_time","room","instructor"])
    return Response({"Response":"class details updated successfully"})

@api_view(['POST'])
def changeconducted(request):
    """
    :param request: classid , decision
    :return: message on getting successfully executed
    """
    postdata = json.loads(request.body)
    print(postdata['classid'])
    print("hello")
    classid = int(postdata['classid'])
    decision = int(postdata['decision'])
    print(decision)
    print(classid)
    requiredclass = Conducted_Classes.objects.get(id = classid)
    if decision == 1:
        requiredclass.is_conducted = True
    else:
        requiredclass.is_conducted = False
    requiredclass.save(update_fields=["is_conducted"])
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
    #     #semno = int(postdata['sem'])
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
    try:
        is_seated = int(postdata['is_seated'])
    except:
        is_seated = 0
    rollnumberstring = str(postdata['rollnumbers'])
    print(rollnumberstring)
    rollnumberstring = rollnumberstring.split(',')

    for rollnumber in rollnumberstring:
        newattendance = Attendance(conductedclass = classkey, student = Student.objects.get(rollno = int(rollnumber)))
        newattendance.save()

    return Response({"response":"all attendances are added"})


#api for requirement 1
@api_view(['GET','POST'])
def returnAllConductedClasses(request):
    print request.body
    try:
        fetchdate = str(json.loads(request.body)['fetchdate'])
        year = int(fetchdate.split('/')[0])
        month = int(fetchdate.split('/')[1])
        day = int(fetchdate.split('/')[2])
        fetchdate = datetime.date(year,month,day)
        print fetchdate
    except:
        fetchdate = datetime.datetime.now().date()
    if request.method == 'POST':
        listOfConductedClasses = Conducted_Classes.objects.filter(date = fetchdate)
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

@api_view(['GET'])
def returnConductedClassDetails(request, pk):
    """ get Details of a single class """
    print(pk)
    conducted_class = Conducted_Classes.objects.get(id=pk)
    print(conducted_class)
    print("yogesh")
    if request.method == 'GET':
        serializer = fetchConductedClasses(conducted_class)
        return Response(serializer.data)

#api for returning the list of days a student is absent
@api_view(['GET'])
def returnCoursesForStudent(request, studId):
    """
    :param request:
    :param studId:
    :return:
    """
    if request.method == 'GET':
        print(studId)
        courses = Student_Courses.objects.filter(student__rollno = studId)
        print(courses)
        serializer = fetchCoursesForStudent(courses, many=True)
        return Response(serializer.data)
