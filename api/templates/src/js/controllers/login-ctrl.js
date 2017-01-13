/**
 *  Login Controller to have all the login logic
 */
angular.module('nerdstacks')

 .controller('LoginController', ['$scope', '$cookieStore',  '$window', 'Authenticate',
     function ($scope, $cookieStore, $window, Authenticate) {

        $scope.loginCredentials = {};
        $scope.errorMessage = '';

        $scope.signIn = function () {

            Authenticate.login({
                'email': $scope.loginCredentials.email,
                'password': $scope.loginCredentials.password
            }, function (response) {
                $cookieStore.put('ns_claims', response.claims_token);
                $window.location.href = "/#/dashboard";
            }, function (error) {
                $scope.errorMessage = error.data.message;
            });

        };

 }]);