/**
 *  Login Controller to have all the login logic
 */
angular.module('nerdstacks')

 .controller('RegistrationController', ['$scope', '$window', 'Registration',
     function ($scope, $window, Registration) {

        $scope.registrationData = {};
        $scope.errorMessage = '';
        $scope.userRegistrationSuccess = false;

        $scope.registerUser = function () {

            Registration.register({
                'email': $scope.registrationData.email,
                'password': $scope.registrationData.password,
                'first_name': $scope.registrationData.firstName,
                'last_name': $scope.registrationData.lastName,
                'company': $scope.registrationData.company
            }, function (response) {
                $scope.userRegistrationSuccess = true;
            }, function (error) {
                $scope.errorMessage = error.data.message;
            });

        };

        $scope.toSignInPage = function () {
            $window.location.href = "/login";
        }

 }]);