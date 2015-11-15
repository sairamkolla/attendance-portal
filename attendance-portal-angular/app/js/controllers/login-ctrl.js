/**
 * Created by umeshksingla on 10/27/15.
 */
App.controller('LoginController', function ($scope, $http, $cookies, $cookieStore, BaseUrl, $state) {
    //initially set those objects to null to avoid undefined error
    // place the message if something goes wrong
    $scope.account = {};
    $scope.authMsg = '';

    $scope.loginAdmin = function () {

        if($scope.account.email === 'umesh' && $scope.account.password === 'umesh') {
            var someSessionObj = {'accesstoken': "fake"};
            $cookieStore.put('obj', someSessionObj);
            $state.go('app.dashboard');
        }
        else{
            $scope.authMsg = 'Wrong Credentials';
        }
        /*$scope.authMsg = '';
        $.post(BaseUrl.url + '/admin_login',
            {
                email: $scope.account.email,
                password: $scope.account.password
            }).then(
            function (data) {
                data = JSON.parse(data);

                if (data.status != 200) {
                    $scope.authMsg = data.message.toString();
                    $scope.$apply();
                } else {
                    var someSessionObj = {'accesstoken': data.data.access_token};
                    $cookieStore.put('obj', someSessionObj);
                    $state.go('app.dashboard');
                }
            });*/
    };

    $scope.recover = function () {

        $.post(BaseUrl.url + '/forgot_password',
            {
                email: $scope.account.email
            }).then(
            function (data) {
                data = JSON.parse(data);
                console.log(data);
                if (data.status == 200) {
                    $scope.successMsg = data.message.toString();
                } else {
                    $scope.errorMsg = data.message.toString();

                }
                $scope.$apply();
            })
    };

    $scope.logout = function () {
        $cookieStore.remove('obj');
        $state.go('page.login');
    }
});

