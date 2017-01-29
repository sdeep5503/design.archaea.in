/**
 * Master Controller
 */
angular.module('nerdstacks')
    .controller('ManageAppsCtrl', ['$scope', '$window', '$rootScope', 'Applications',  ManageAppsCtrl]);

function ManageAppsCtrl($scope, $window, $rootScope, Applications) {

    var currentUrlPath = $window.location.href;
    var nerdGuid = currentUrlPath.split('/')[currentUrlPath.split('/').length - 2];

    Applications.get({
        'account_guid': $rootScope.current.account.account_guid,
        'nerd_guid': $rootScope.currentNerd
    }, function (response) {

    }, function (error) {

    });

    $scope.navigateToAppCreateEditPage = function(applicationGuid)
    {
        $rootScope.currentApplication = applicationGuid;
        var appGuid = '';
        if (applicationGuid) {
            appGuid = '/' + applicationGuid
        }
        $window.location.href = '#/nerds/' + $rootScope.currentNerd + '/applications' + appGuid;
    }
}
