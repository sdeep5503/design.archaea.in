/**
 * Master Controller
 */
angular.module('Dashboard')
    .controller('ManageNerdsCtrl', ['$scope', '$window', ManageNerdsCtrl]);

function ManageNerdsCtrl($scope, $window) {

    $scope.navigateToAppManagement = function(nerdGuid)
    {
        $window.location.href = '#/nerds/' + nerdGuid + '/applications';
    }
}
