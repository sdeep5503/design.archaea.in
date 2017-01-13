/**
 * Master Controller
 */
angular.module('nerdstacks')
    .controller('ManageAppsCtrl', ['$scope', '$window', '$rootScope', 'Applications',  ManageAppsCtrl]);

function ManageAppsCtrl($scope, $window, $rootScope, Applications) {

    Applications.get({
        'account_guid': $rootScope.current.account.account_guid,
        'nerd_guid': ''
    }, function (response) {

    }, function (error) {

    });

    $scope.navigateToAppCreateEditPage = function(applicationGuid)
    {
        $rootScope.currentApplication = applicationGuid;
        $window.location.href = '#/nerds/' + $rootScope.currentNerd + '/applications/' + applicationGuid;
    }
}
