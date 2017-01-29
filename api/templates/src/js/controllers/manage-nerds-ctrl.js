/**
 * Master Controller
 */
angular.module('nerdstacks')
    .controller('ManageNerdsCtrl', ['$scope', '$window', '$rootScope', 'Nerds', ManageNerdsCtrl]);

function ManageNerdsCtrl($scope, $window, $rootScope, Nerds) {

    Nerds.get({
        'account_guid': $rootScope.current.account.account_guid
    }, function (response) {
        $rootScope.current.nerd = response[0];
    }, function (error) {

    });

    $scope.navigateToAppManagement = function(nerdGuid)
    {
        $rootScope.currentNerd = nerdGuid;
        $window.location.href = '#/nerds/' + nerdGuid + '/applications';
    }
}
