/**
 *  Login Controller to have all the login logic
 */
angular.module('nerdstacks', ['nerdstacks.services', 'ngCookies'])

 .controller('LoginController', ['$scope', '$cookies', 'Authenticate', function ($scope, $cookies, Authenticate) {

    $scope.loginCredentials = {};
    $scope.errorMessage = '';

    $scope.signIn = function () {

        Authenticate.login({
            'email': $scope.loginCredentials.email,
            'password': $scope.loginCredentials.password
        }, function (response) {
            $cookies['ns_claims'] = response.claims_token;
        }, function (error) {
            $scope.errorMessage = error.data.message;
        });

    };

 }]);