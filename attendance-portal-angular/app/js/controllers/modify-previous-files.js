/**
 * Created by umeshksingla on 15/11/15
 */

App.controller('modifyPreviousController', ['allServices', '$scope', 'ngDialog', function (allServices, $scope, ngDialog ,$http, $cookies, $cookieStore, BaseUrl, $state) {

    console.log("inside modifyPreviousController");

    $scope.newclass = {
        courseid : '',
        roomid : '',
        who : '',
        fromtime : '',
        totime : '',
        date : $scope.date,
        conducted : 'YES',
        is_conducted : true
    };



    $scope.fetchdate = new Date();
    $scope.date = new Date();

    $scope.roomList = [];
    $scope.conductedClassesList = [];
    $scope.coursesList = [];

    $scope.message = '';
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

    $scope.getToBeConductedClasses = function () {

        $scope.conductedClassesList = [];
        $scope.submitting = true;

        allServices.getTodayConductedClasses({fetchdate : $scope.fetchdate.toISOString().slice(0,10)}).then(function(data){

            console.log($scope.fetchdate.toISOString().slice(0,10));
            console.log(data);

            $scope.conductedClassesList = [];

            if(data.data.length){
                $scope.date = data.data[0]["date"];
                var obj;
                data.data.forEach(function (c) {
                    obj = c;
                    obj["coursename"] = $scope.coursesList[c["course"]-1]["coursename"];
                    obj["roomname"] = $scope.roomList[c["room"]-1]["room"];
                    obj["conducted"] = obj["is_conducted"] ? 'YES' : 'NO';
                    obj["editable"] = obj["is_conducted"] ? true: false;
                    $scope.conductedClassesList.push(obj);
                })
            }

        }, function(error) {

            console.log(error);
            $scope.message = error;
            $scope.submitting = false;

        });
    };

    $scope.changeConducted = function (classid, index, decision) {
        var obj = {
            classid : classid,
            decision : decision
        };
        console.log(obj);
        allServices.changeConducted(obj).then(function (data) {

            console.log(data);

            if(decision == 1){
                $scope.conductedClassesList[index]["conducted"] = 'YES';
                $scope.conductedClassesList[index]["is_conducted"] = true;
                $scope.conductedClassesList[index]["editable"] = true;
            }
            else {
                $scope.conductedClassesList[index]["conducted"] = 'NO';
                $scope.conductedClassesList[index]["is_conducted"] = false;
                $scope.conductedClassesList[index]["editable"] = false;
            }

            swal("changed successfully");
        }, function (error) {
            sweetAlert("Oops..", "Can't Change", "error");
        })
    };

    $scope.openExtraClassDialog = function () {

        $scope.newclass = {
            courseid : '',
            roomid : '',
            who : '',
            fromtime : '',
            totime : '',
            date : $scope.date,
            conducted : 'YES',
            is_conducted : true
        };

        ngDialog.open({
            template: 'addExtraClassId',
            className: 'ngdialog-theme-default',
            scope: $scope
        });
    };

    $scope.addExtraClass = function () {
        $scope.newclass.date = $scope.date;
        console.log($scope.newclass);
        allServices.addNewClass($scope.newclass).then(function (data) {

            console.log(data);
            var obj = $scope.newclass;
            obj["coursename"] = $scope.coursesList[obj["courseid"]-1]["coursename"];
            obj["roomname"] = $scope.roomList[obj["roomid"]-1]["room"];
            obj["conducted"] = "YES";
            obj["editable"] = true;
            obj["from_time"] = obj["fromtime"];
            obj["to_time"] = obj["totime"];
            obj["instructor"] = obj["who"];

            $scope.conductedClassesList.push(obj);
            swal("added successfully");

        }, function (error) {
            sweetAlert("Oops..", "Can't Add", "error");
        })
    };
    //$scope.getToBeConductedClasses();
}]);

