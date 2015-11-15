
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
        serializer = fetchRooms(listOfRooms)
        return Response(serializer.data)

#api for requirement 4
@api_view(['GET','POST'])
def returnAllCourses(request):
    if request.method == 'GET':
        listOfCourses = Course.objects.all()
        serializer = fetchCourses(listOfCourses)
        return Response(serializer.data)