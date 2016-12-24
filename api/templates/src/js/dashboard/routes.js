/**
 * Route configuration for the Dashboard module.
 */
angular.module('Dashboard').config(['$stateProvider', '$urlRouterProvider',
    function($stateProvider, $urlRouterProvider) {

    // For unmatched routes
    $urlRouterProvider.otherwise('/dashboard');

    // Application routes
    $stateProvider
        .state('dashboard', {
            url: '/dashboard',
            templateUrl: 'dashboard.html'
        })
        .state('tables', {
            url: '/nerds/:nerd_guid/applications',
            templateUrl: 'manage-applications.html'
        })
        .state('nerds', {
            url: '/nerds',
            templateUrl: 'manage-nerds.html'
        });
}]);
