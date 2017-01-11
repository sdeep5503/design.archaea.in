angular.module('nerdstacks', ['ui.bootstrap', 'ui.router', 'ngCookies'], function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});