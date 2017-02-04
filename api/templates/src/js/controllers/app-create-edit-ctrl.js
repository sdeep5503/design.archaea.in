/**
 * Master Controller
 */
angular.module('nerdstacks')
    .controller('AppCreateEditCtrl', ['$scope', '$window', '$rootScope', 'Applications', 'Applications2',  AppCreateEditCtrl]);

function AppCreateEditCtrl($scope, $window, $rootScope, Applications, Applications2) {

    $scope.createMode = true;
    $scope.application = {};
    $scope.isLoading = false;
    $scope.algorithms = ['linear_regression', 'logistic_regression'];

    var currentUrlPath = $window.location.href;
    var appGuid = currentUrlPath.split('/')[currentUrlPath.split('/').length - 1];
    var nerd_guid = currentUrlPath.split('/')[currentUrlPath.split('/').length - 3];

    $scope.alerts = [];

    $scope.addAlert = function(alert) {
        $scope.alerts.push(alert);
    };

    $scope.closeAlert = function(index) {
        $scope.alerts.splice(index, 1);
    };

    var getMetadataForAlgorithm = function (algorithm) {

        var metadataMapper = {
            'linear_regression': {
                'fit_intercept': true,
                'normalize': false,
                'copy_X': true,
                'n_jobs': 1
            }
        }

        metadata = metadataMapper[algorithm];
        if (!metadata) {
            metadata = {}
        }
        return metadata;

    }

    if (appGuid != 'create') {
       // TODO populate $scope.application
       $scope.createMode = false;
       Applications2.get({
            'account_guid': $rootScope.current.account.account_guid,
            'nerd_guid': nerd_guid,
            'application_guid': appGuid
        }, function (response) {
            $scope.application.name = response.application_name;
            $scope.application.algorithm = response.algorithm;
            $scope.application.app_metadata = JSON.stringify(response.parameters);
            $scope.application.secret = response.application_secret;
            $scope.application.key = response.application_key;
        }, function (error) {
            $scope.addAlert({
                type: 'danger',
                msg: error.data.message
            });
        });
    } else {

    }

    $scope.save = function () {
        $scope.isLoading = true;
        if ($scope.createMode) {
            // TODO validate the input before saving
            Applications.save({
                'account_guid': $rootScope.current.account.account_guid,
                'nerd_guid': nerd_guid
            }, {
                'name': $scope.application.name,
                'algorithm': $scope.application.algorithm,
                'app_metadata': JSON.parse($scope.application.app_metadata)
            }, function (response){
                $scope.isLoading = false;
                $scope.application.key = response.application_key;
                $scope.application.secret = response.application_secret;
                $scope.addAlert({
                    type: 'success',
                    msg: 'Your app has been created successfully. Use the app key and app secret to use the APIs'
                });
            }, function (error) {
                $scope.addAlert({
                    type: 'danger',
                    msg: error.data.message
                });
            });
        } else {
            // TODO validate input and update the app
        }
    }

    $('#algorithm_selector').change(function () {
        var selectedAlgorithm = $scope.algorithms[$('#algorithm_selector')[0].value];
        $scope.application.app_metadata = JSON.stringify(getMetadataForAlgorithm(selectedAlgorithm));
    });

}
