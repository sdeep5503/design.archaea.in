/**
 * Master Controller
 */
angular.module('nerdstacks')
    .controller('ManageAppsCtrl', ['$scope', '$window', '$modal', '$rootScope', 'Accounts', 'Applications', 'Applications2', 'Nerds2',  ManageAppsCtrl])
    .controller('ApiPopUpCtrl', ['$scope', '$modal', '$rootScope', '$modalInstance'], ApiPopUpCtrl);

function ManageAppsCtrl($scope, $window, $modal, $rootScope, Accounts, Applications, Applications2, Nerds2) {

    $scope.applications = [];
    $scope.apiApp = {};

    var currentUrlPath = $window.location.href;
    var nerdGuid = currentUrlPath.split('/')[currentUrlPath.split('/').length - 2];

    if ($rootScope.current.nerd) {
        nerdGuid = $rootScope.current.nerd.nerd_guid;
    }

    $scope.alerts = [];

    $scope.addAlert = function(alert) {
        $scope.alerts.push(alert);
    };

    $scope.closeAlert = function(index) {
        $scope.alerts.splice(index, 1);
    };

    Applications.get({
        'account_guid': $rootScope.current.account.account_guid,
        'nerd_guid': nerdGuid
    }, function (response) {
        $scope.applications = response;
    }, function (error) {
        console.log('We are unable to get the applications from this nerd. Please check whether the nerd is up and running.');
        $scope.addAlert({
            msg: 'We are unable to get the applications from this nerd. Please check whether the nerd is up and running.',
            type: 'danger'
        });
    });

    $scope.navigateToAppCreateEditPage = function(applicationGuid)
    {
        $rootScope.currentApplication = applicationGuid;
        var appGuid = '';
        if (applicationGuid) {
            appGuid = '/' + applicationGuid
        }
        $window.location.href = '#/nerds/' + nerdGuid + '/applications' + appGuid;
    }

    $scope.open = function (appGuid) {

        Applications2.get({
            'account_guid': $rootScope.current.account.account_guid,
            'nerd_guid': nerdGuid,
            'application_guid': appGuid
        }, function (response) {
            $rootScope.current.apiApp = response;
            $modal.open({
                templateUrl: 'api-list-popup.html',
                scope: $scope,
                controller: ApiPopUpCtrl
            });
        }, function (error) {

        });

    }
}

function ApiPopUpCtrl($scope, $modal, $rootScope, $modalInstance) {

    $scope.apiApp = $rootScope.current.apiApp;
    $scope.nerd = $rootScope.current.nerd;

    $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
    };

}
