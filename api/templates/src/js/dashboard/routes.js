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
            url: '/tables',
            templateUrl: 'tables.html'
        })
        .state('nerds', {
            url: '/nerds',
            templateUrl: 'manage-nerds.html'
        });
}]);
