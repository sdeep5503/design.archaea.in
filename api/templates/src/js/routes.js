/**
 * Route configuration for the Dashboard module.
 */
angular.module('nerdstacks').config(['$stateProvider', '$urlRouterProvider',
    function($stateProvider, $urlRouterProvider) {

    // For unmatched routes
    $urlRouterProvider.otherwise('/nerds');

    // Application routes
    $stateProvider
        /*.state('dashboard', {
            url: '/dashboard',
            templateUrl: 'dashboard.html'
        })*/
        .state('nerds', {
            url: '/nerds',
            templateUrl: 'manage-nerds.html'
        })
        .state('manage-users', {
            url: '/users',
            templateUrl: 'manage-users.html'
        })
        .state('documentation', {
            url: '/documentations',
            templateUrl: 'documentations.html'
        })
        .state('applications', {
            url: '/nerds/:nerd_guid/applications',
            templateUrl: 'manage-applications.html'
        })
        .state('edit-applications', {
            url: '/nerds/:nerd_guid/applications/:application_guid',
            templateUrl: 'design-applications.html'
        })
        .state('create-applications', {
            url: '/nerds/:nerd_guid/applications/create',
            templateUrl: 'design-applications.html'
        });
}]);
