angular.module('Dashboard', ['ui.bootstrap', 'ui.router', 'ngCookies'])

.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('[[').endSymbol(']]');
    });
