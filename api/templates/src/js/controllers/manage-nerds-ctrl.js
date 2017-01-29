/**
 * Master Controller
 */
angular.module('nerdstacks')
    .controller('ManageNerdsCtrl', ['$scope', '$window', '$rootScope', 'Nerds', ManageNerdsCtrl]);

function ManageNerdsCtrl($scope, $window, $rootScope, Nerds) {

    $scope.nerds = [];

    Nerds.get({
        'account_guid': $rootScope.current.account.account_guid
    }, function (response) {
        $scope.nerds = response;
    }, function (error) {
        console.log(error.data.message)
    });

    $scope.navigateToAppManagement = function(nerd)
    {
        $rootScope.currentNerd = nerd.nerd_guid;
        $rootScope.current.nerd = nerd;
        $window.location.href = '#/nerds/' + nerd.nerd_guid + '/applications';
    }
}
