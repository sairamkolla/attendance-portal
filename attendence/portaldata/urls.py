from django.conf.urls import include,patterns,url

urlpatterns = patterns('',
                       url(r'^changeconducted/$','portaldata.views.changeconducted'),
                       url(r'^addnewclass/$','portaldata.views.addnewclass'),
                       url(r'^addattendance/$','portaldata.views.addattendance'),
                       url(r'^returnAllConductedClasses/$','portaldata.views.returnAllConductedClasses'),
                       url(r'^returnAllRooms/$','portaldata.views.returnAllRooms'),
                       url(r'^returnAllCourses/$','portaldata.views.returnAllCourses'),
                       url(r'adddefaultclasses/$','portaldata.views.adddefaultclasses'),
                       )