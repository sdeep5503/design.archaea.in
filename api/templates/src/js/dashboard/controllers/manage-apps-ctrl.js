/**
 * Master Controller
 */
angular.module('Dashboard')
    .controller('ManageAppsCtrl', ['$scope', '$window', '$rootScope', ManageAppsCtrl]);

function ManageAppsCtrl($scope, $window, $rootScope) {

    $scope.navigateToAppCreateEditPage = function(applicationGuid)
    {
        $rootScope.currentApplication = applicationGuid;
        $window.location.href = '#/nerds/' + $rootScope.currentNerd + '/applications/' + applicationGuid;
    }
}
