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
        .state('nerds', {
            url: '/nerds',
            templateUrl: 'manage-nerds.html'
        })
        .state('applications', {
            url: '/nerds/:nerd_guid/applications',
            templateUrl: 'manage-applications.html'
        })
        .state('edit-applications', {
            url: '/nerds/:nerd_guid/applications/:application_guid',
            templateUrl: 'design-applications.html'
        });
}]);
