/**
 *  Login Controller to have all the login logic
 */
angular.module('nerdstacks', ['nerdstacks.services'])

 .controller('LoginController', ['$scope', 'Authenticate', function ($scope, Authenticate) {

    $scope.loginCredentials = {};

    $scope.signIn = function () {
        Authenticate.login({
            'email': $scope.loginCredentials.email,
            'password': $scope.loginCredentials.password
        }, function (response) {
            console.log(JSON.stringify(response));
        }, function (error) {
            console.log(JSON.stringify(error));
        });
    }

 }]);