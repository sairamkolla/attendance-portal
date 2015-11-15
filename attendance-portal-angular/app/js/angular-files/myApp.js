/**
 * Created by umeshksingla on 15/11/15.
 */

App.config(['$stateProvider', '$locationProvider', '$urlRouterProvider', 'RouteHelpersProvider',
    function ($stateProvider, $locationProvider, $urlRouterProvider, helper) {
        'use strict';

        // Set the following to true to enable the HTML5 Mode
        // You may have to set <base> tag in index and a routing configuration in your server
        $locationProvider.html5Mode(false);

        // default route
        $urlRouterProvider.otherwise('/page/login');

        //
        // Application Routes
        // -----------------------------------
        $stateProvider
            //
            // Single Page Routes
            // -----------------------------------
            .state('page', {
                url: '/page',
                templateUrl: 'app/pages/page.html',
                resolve: helper.resolveFor('modernizr', 'icons', 'parsley'),
                controller: ["$rootScope", function ($rootScope) {
                    $rootScope.app.layout.isBoxed = false;
                }]
            })
            .state('page.login', {
                url: '/login',
                title: "Login",
                templateUrl: 'app/pages/login.html'
            })
            /*.state('page.register', {
                url: '/register',
                title: "Register",
                templateUrl: 'app/pages/register.html'
            })
            .state('page.recover', {
                url: '/recover',
                title: "Recover",
                templateUrl: 'app/pages/recover.html'
            })
            .state('page.terms', {
                url: '/terms',
                title: "Terms & Conditions",
                templateUrl: 'app/pages/terms.html'
            })
            .state('page.404', {
                url: '/404',
                title: "Not Found",
                templateUrl: 'app/pages/404.html'
            })*/

            //App routes
            .state('app', {
                url: '/app',
                abstract: true,
                templateUrl: helper.basepath('app.html'),
                controller: 'AppController',
                resolve: helper.resolveFor('modernizr', 'icons', 'screenfull')
            })
            .state('app.dashboard', {
                url: '/dashboard',
                title: 'Dashboard',
                templateUrl: helper.basepath('dashboard.html'),
                resolve: helper.resolveFor('ngDialog')
            })
            .state('app.edit_class', {
                url: '/editClass/{class_id}',
                title: 'Edit Class Details',
                templateUrl: helper.basepath('edit-class.html')
            })
            .state('app.adddefaultclasses', {
                url: '/addDefaultClasses',
                title: "Add Today's Scheduled Classes",
                templateUrl: helper.basepath('add-default-classes.html')
            })
            .state('app.modifyPrevious', {
                url: '/modifyPreviousClasses',
                title: 'Modify Previous Classes',
                templateUrl: helper.basepath('modify-previous-classes.html'),
                resolve: helper.resolveFor('ngDialog')
            })
            .state('app.viewAttendance', {
                url: '/viewAttendance',
                title: 'View Attendance',
                templateUrl: helper.basepath('view-attendance.html')
            })

    }]);
