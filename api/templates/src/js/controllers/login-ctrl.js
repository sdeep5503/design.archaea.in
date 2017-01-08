/**
 *  Login Controller to have all the login logic
 */
angular.module('nerdstacks').controller('LoginController', ['$scope', LoginController]);

function LoginController($scope) {

    $scope.loginCredentials = {};

    $scope.signIn = function () {
        console.log('Trying to login : ' + $scope.loginCredentials.email);
    }
}