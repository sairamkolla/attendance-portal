from django.db import models
import datetime
# Create your models here.

class Student(models.Model):
    rollno = models.IntegerField(default=0)
    def __unicode__(self):
        return unicode(self.rollno)

class Course(models.Model):
    coursename = models.CharField(max_length=50)
    year = models.IntegerField(default = 0)
    sem = models.IntegerField(default = 0)

    def __unicode__(self):
        return unicode(self.id)


class Student_Courses(models.Model):
    course = models.ForeignKey(Course)
    student = models.ForeignKey(Student)
    def __unicode__(self):
        return unicode(str(self.student.rollno) +  ' || ' + self.course.coursename)

class ClassRoom(models.Model):
    room = models.CharField(max_length = 30)
    def __unicode__(self):
        return unicode(self.room)

class Schedule(models.Model):
    course = models.ForeignKey(Course)
    #year = models.IntegerField(default=0)
    #sem = models.IntegerField(default=0)
    #date = models.DateField(auto_now_add=True)
    from_time = models.TimeField()
    to_time = models.TimeField()
    room = models.ForeignKey(ClassRoom)
    day = models.IntegerField(default=0) ### This Field takes values from 1 to 7 representing sunday-saturday respectively
    instructor = models.CharField(max_length=30)
    def __unicode__(self):
        return unicode(self.course.coursename + ' || ' + self.instructor + ' || ' + str(self.day) )

class Seating_Arrangement(models.Model):
    course = models.ForeignKey(Course)
    student = models.ForeignKey(Student)
    seat = models.CharField(max_length=6)

    def __unicode__(self):
        return unicode(str(self.student.rollno) +  ' || ' + self.course.coursename +  ' || ' + self.seat)

class Conducted_Classes(models.Model):
    course = models.ForeignKey(Course)
    date = models.DateField(default = datetime.datetime.now().date())
    from_time = models.TimeField()
    to_time = models.TimeField()
    room = models.ForeignKey(ClassRoom)
    instructor = models.CharField(max_length=30)
    is_conducted = models.BooleanField(default = True)

class Attendance(models.Model):
    conductedclass = models.ForeignKey(Conducted_Classes)
    student = models.ForeignKey(Student)
    is_absent = models.BooleanField(default=True)

class defaults_added(models.Model):
    date = models.DateField(auto_now=True)

