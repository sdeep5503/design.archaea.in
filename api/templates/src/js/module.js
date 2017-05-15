

    angular.module('nerdstacks', ['ui.bootstrap', 'ui.router', 'ngCookies', 'nerdstacks.services'], function($interpolateProvider) {

        $interpolateProvider.startSymbol('[[');
        $interpolateProvider.endSymbol(']]');

    })

    .config(['$httpProvider',function($httpProvider) {
        $httpProvider.interceptors.push('httpInterceptor');
    }])

    .run(function($rootScope, Accounts, Whoami) {
      if (!$rootScope.current) {
         $rootScope.current = {};
      }

      Accounts.get(function (response) {
        $rootScope.accounts = response;
        $rootScope.current.account = response[0];
        $rootScope.$broadcast("GetAccountsSuccess");
      }, function (error) {
        console.log(error.data.message);
      });

      Whoami.get(function(response) {
        $rootScope.current.user = response;
        $rootScope.$broadcast("WhoAmICallSuccess");
      }, function(error) {
        console.log(error.data.message);
      });

    });

