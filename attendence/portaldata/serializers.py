from rest_framework import serializers
from models import *

class fetchConductedClasses(serializers.ModelSerializer):
    """
        returns all the columns of the table Conducted_classes
    """
    class Meta:
        model = Conducted_Classes
        fields = ('id','course','date', 'from_time', 'to_time', 'room', 'instructor')

class fetchRooms(serializers.ModelSerializer):
    """
        fetches rooms from table ClassRoom
    """
    class Meta:
        model = ClassRoom
        fields = ('id','room')

class fetchCourses(serializers.ModelSerializer):
    """
        fetches all the courses from table Course
    """
    class Meta:
        model = Course
        fields = ('id','coursename')

class fetchRollNum(serializers.ModelSerializer):
    """
        fetches the roll numbers from student table
    """
    class Meta:
        model = Student
        fields = ('id','rollno')


class fetchSeatNumber(serializers.ModelSerializer):
    """
        fetches seat number of a given student for particular course
    """
    class Meta:
        model = Seating_Arrangement
        fields = ('id', 'course', 'student', 'seat')

class fetchAttendance(serializers.ModelSerializer):
    """
        fetches the attendence for the conducted classes with is_absent flag
    """
    class Meta:
        model = Attendance
        fields = ('id', 'conductedclass', 'student', 'is_absent')

class fetchSchedule(serializers.ModelSerializer):
    """
        fetches the schedule for the classes
    """
    class Meta:
        model = Schedule
        fields = ('id', 'course', 'data', 'from_time', 'to_time', 'room', 'day', 'instructor')
