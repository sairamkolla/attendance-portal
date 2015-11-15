/**
 * Created by umeshksingla on 15/11/15
 */

App.controller('EditClassController', ['allServices', '$scope', '$stateParams', function (allServices, $scope, $stateParams, $http, $cookies, $cookieStore, BaseUrl, $state) {

    console.log("inside EditClass controller");

    $scope.date = new Date();

    $scope.class_id = $stateParams.class_id;

    $scope.roomList = [];
    $scope.coursesList = [];
    $scope.absentees = [];

    $scope.message = '';
    $scope.class = {
        course: '',
        date: '',
        from_time: '',
        id : '',
        instructor: '',
        is_conducted: '',
        room: '',
        to_time: '',
        coursename : '',
        roomname : ''
    };

    $scope.submitting = false;

    allServices.getRoomsList().then(function(data){

        console.log(data);
        $scope.roomList = data.data;

    }, function(error) {

        console.log(error);
        $scope.message = error;
        $scope.submitting = false;

    });

    allServices.getCoursesList().then(function(data){

        console.log(data);
        $scope.coursesList = data.data;

    }, function(error) {

        console.log(error);
        $scope.message = error;
        $scope.submitting = false;

    });

    allServices.getClassDetails($stateParams.class_id).then(function(data){

        var obj = {
            id:'',
            course: '',
            date: '',
            from_time: '',
            instructor: '',
            is_conducted: '',
            room: '',
            to_time: ''
        };
        obj = data.data;
        for(var i in obj){
            $scope.class[i] = obj[i];
        }

        $scope.class['coursename'] = $scope.coursesList[obj['course']-1]["coursename"];
        $scope.class['roomname'] = $scope.roomList[obj['room']-1]["room"];

    }, function(error) {

        console.log(error);
        $scope.message = error;
        $scope.submitting = false;

    });
    
    $scope.editClass = function () {
        console.log($scope.class);
        allServices.editClassDetails($scope.class).then(function(data){

            console.log(data);
            $scope.addAbsentees($scope.class['id']);

        }, function(error) {

            console.log(error);
            $scope.message = error;
            $scope.submitting = false;
        });
    };

    $scope.addAbsentees = function (classid) {
        console.log(classid, $scope.absentees);
        var rollnumbers = '';
        $scope.absentees.forEach(function (obj) {
            rollnumbers += obj["text"] + ',';
        });
        rollnumbers = rollnumbers.slice(0, rollnumbers.lastIndexOf(','));

        allServices.addAbsenteesList({ "classid" : classid, rollnumbers : rollnumbers }).then(function(data){
            console.log(data);
        }, function(error) {

            console.log(error);
            $scope.message = error;
            $scope.submitting = false;

        });
    }

}]);

