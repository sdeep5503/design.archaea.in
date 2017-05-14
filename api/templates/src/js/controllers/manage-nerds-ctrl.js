/**
 * Master Controller
 */
angular.module('nerdstacks')
    .controller('ManageNerdsCtrl', ['$scope', '$window', '$rootScope', 'Nerds', 'Accounts', ManageNerdsCtrl]);

function ManageNerdsCtrl($scope, $window, $rootScope, Nerds, Accounts) {

    $scope.nerds = [];

    $scope.alerts = [];

    $scope.addAlert = function(alert) {
        $scope.alerts.push(alert);
    };

    $scope.closeAlert = function(index) {
        $scope.alerts.splice(index, 1);
    };

    Nerds.get({
        'account_guid': $rootScope.current.account.account_guid
    }, function (response) {
        $scope.nerds = response;
        if ($scope.nerds.length == 0) {
            $scope.addAlert({
                type: 'danger',
                msg: 'There are no nerds in this account that you have access to. Please contact your administrator'
            });
        }
    }, function (error) {
        console.log(error.data.message)
    });

    $scope.navigateToAppManagement = function(nerd)
    {
        $rootScope.current.nerd = nerd;
        $window.location.href = '#/nerds/' + nerd.nerd_guid + '/applications';
    }
}
