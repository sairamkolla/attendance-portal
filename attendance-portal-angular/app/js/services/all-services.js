/**
 * Created by umeshksingla on 1/11/15.
 */

App.factory('allServices', function (BaseUrl, $http) {

    return {

        //get room list
        getRoomsList: function () {
            return $http({
                "url": BaseUrl.url + 'returnAllRooms/',
                "method": "GET",
                "data": angular.toJson({}, false),
                "transformRequest": false,
                "headers": BaseUrl.headers
            });
        },

        //get courses list
        getCoursesList: function () {
            return $http({
                "url": BaseUrl.url + 'returnAllCourses/',
                "method": "GET",
                "data": angular.toJson({}, false),
                "transformRequest": false,
                "headers": BaseUrl.headers
            });
        },

        //get today's conducted classes list
        getTodayConductedClasses: function () {
            return $http({
                "url": BaseUrl.url + 'returnAllConductedClasses/',
                "method": "GET",
                "data": angular.toJson({}, false),
                "transformRequest": false,
                "headers": BaseUrl.headers
            });
        },

        //get a conducted class details
        getClassDetails: function (class_id) {
            return $http({
                "url": BaseUrl.url + 'returnConductedClassDetails/' + class_id,
                "method": "GET",
                "data": angular.toJson({}, false),
                "transformRequest": false,
                "headers": BaseUrl.headers
            });
        },

        // invert conducted
        changeConducted: function (obj) {
            return $http({
                "url": BaseUrl.url + 'changeconducted/',
                "method": "POST",
                "data": angular.toJson(obj, false),
                "transformRequest": false,
                "headers": BaseUrl.headers
            });
        },

        // add new class
        addNewClass: function (obj) {
            return $http({
                "url": BaseUrl.url + 'addnewclass/',
                "method": "POST",
                "data": angular.toJson(obj, false),
                "transformRequest": false,
                "headers": BaseUrl.headers
            });
        },

        // edit class details
        editClassDetails : function (obj) {
            return $http({
                "url": BaseUrl.url + 'updateClassDetails/',
                "method": "POST",
                "data": angular.toJson(obj, false),
                "transformRequest": false,
                "headers": BaseUrl.headers
            });
        },

        // add absentees list
        addAbsenteesList : function (obj) {
            return $http({
                "url": BaseUrl.url + 'addattendance/',
                "method": "POST",
                "data": angular.toJson(obj, false),
                "transformRequest": false,
                "headers": BaseUrl.headers
            });
        },

        // add default classes
        addDefault : function () {
            return $http({
                "url": BaseUrl.url + 'adddefaultclasses/',
                "method": "POST",
                "data": angular.toJson({}, false),
                "transformRequest": false,
                "headers": BaseUrl.headers
            });
        }
    }

});