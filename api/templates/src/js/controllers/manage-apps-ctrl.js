/**
 * Master Controller
 */
angular.module('nerdstacks')
    .controller('ManageAppsCtrl', ['$scope', '$window', '$modal', '$rootScope', 'Accounts', 'Applications', 'Applications2', 'Nerds2',  ManageAppsCtrl]);

function ManageAppsCtrl($scope, $window, $modal, $rootScope, Accounts, Applications, Applications2, Nerds2) {

    $scope.applications = [];
    $scope.apiApp = {};

    var currentUrlPath = $window.location.href;
    var nerdGuid = currentUrlPath.split('/')[currentUrlPath.split('/').length - 2];

    if ($rootScope.current.nerd) {
        nerdGuid = $rootScope.current.nerd.nerd_guid;
    }

    Nerds2.get({
        'account_guid': $rootScope.current.account.account_guid,
        'nerd_guid': nerdGuid
    }, function (response) {
        $scope.nerd = response;
    }, function (error) {
        console.log(error.data.message)
    });

    Applications.get({
        'account_guid': $rootScope.current.account.account_guid,
        'nerd_guid': nerdGuid
    }, function (response) {
        $scope.applications = response;
    }, function (error) {

    });

    $scope.navigateToAppCreateEditPage = function(applicationGuid)
    {
        $rootScope.currentApplication = applicationGuid;
        var appGuid = '';
        if (applicationGuid) {
            appGuid = '/' + applicationGuid
        }
        $window.location.href = '#/nerds/' + $rootScope.current.nerd.nerd_guid + '/applications' + appGuid;
    }

    $scope.open = function (appGuid) {

        Applications2.get({
            'account_guid': $rootScope.current.account.account_guid,
            'nerd_guid': nerdGuid,
            'application_guid': appGuid
        }, function (response) {
            $scope.apiApp = response;
            $modal.open({
                templateUrl: 'api-list-popup.html',
                scope: $scope,
                resolve: {
                    apiApp: function() {
                      return $scope.apiApp
                    },
                    nerd: function() {
                       return $scope.nerd
                    }
                }
            });
        }, function (error) {

        });

    }
}
