/**
 * Master Controller
 */
angular.module('nerdstacks')
    .controller('ManageNerdsCtrl', ['$scope', '$window', '$rootScope', ManageNerdsCtrl]);

function ManageNerdsCtrl($scope, $window, $rootScope) {

    $scope.navigateToAppManagement = function(nerdGuid)
    {
        $rootScope.currentNerd = nerdGuid;
        $window.location.href = '#/nerds/' + nerdGuid + '/applications';
    }
}
