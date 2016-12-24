/**
 * Master Controller
 */
angular.module('Dashboard')
    .controller('ManageNerdsCtrl', ['$scope', '$window', '$rootScope', ManageNerdsCtrl]);

function ManageNerdsCtrl($scope, $window, $rootScope) {

    $scope.navigateToAppManagement = function(nerdGuid)
    {
        $rootScope.currentNerd = nerdGuid;
        $window.location.href = '#/nerds/' + nerdGuid + '/applications';
    }
}
