/**
 * Created by umeshksingla on 15/11/15
 */

App.controller('addDefaultController', ['allServices', '$scope', '$stateParams', function (allServices, $scope, $stateParams, $http, $cookies, $cookieStore, BaseUrl, $state) {

    console.log("inside adddefault controller");
    $scope.addDefault = function () {
        allServices.addDefault().then(function (data) {
            console.log(data);
            swal(data.data.response || "Done!");
        }, function (error) {
           sweetAlert("Oops..", "Some Error Occurred", "error");
        });
    }
}]);