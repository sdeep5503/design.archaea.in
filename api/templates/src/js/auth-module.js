

    angular.module('nerdstacks', ['ui.bootstrap', 'ui.router', 'ngCookies', 'nerdstacks.services'], function($interpolateProvider) {

        $interpolateProvider.startSymbol('[[');
        $interpolateProvider.endSymbol(']]');

    })

    .config(['$httpProvider',function($httpProvider) {
        $httpProvider.interceptors.push('httpInterceptor');
    }]);