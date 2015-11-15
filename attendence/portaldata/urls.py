from django.conf.urls import include,patterns,url

urlpatterns = patterns('',
                       url(r'changeconducted/$','portaldata.views.changeconducted'),
                       url(r'addnewclass/$','portaldata.views.addnewclass'),
                       url(r'addattendance/$','portaldata.views.addattendance'),
                       )