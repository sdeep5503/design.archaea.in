/**
 * Master Controller
 */
angular.module('nerdstacks')
    .controller('AppCreateEditCtrl', ['$scope', '$window', '$rootScope', 'Accounts', 'Applications', 'Applications2',  AppCreateEditCtrl]);

function AppCreateEditCtrl($scope, $window, $rootScope, Accounts, Applications, Applications2) {

    $scope.createMode = true;
    $scope.application = {};
    $scope.isLoading = false;
    $scope.algorithms = ['linear_regression', 'logistic_regression',
    'ridge_regression', 'neural_network', 'conv_neural_nets'];

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
            },

            'logistic_regression': {
                'penalty': "l2",
                'dual': false,
                'tol': 1e-4,
                'C': 1.0,
                'fit_intercept': true,
                'intercept_scaling': 1,
                'class_weight': null,
                'random_state': null,
                'solver': 'liblinear',
                'max_iter': 100,
                'multi_class': "ovr",
                'verbose': 0,
                'warm_start': false,
                'n_jobs': 1
            },

            'ridge_regression': {
                'alpha': 0.0001,
                'fit_intercept': true,
                'normalize': false,
                'copy_X': true,
                'max_iter': 5
            },

            'neural_network': {
                'dimension': [128, 64, 10]
            },

            'conv_neural_netsØ': {
                'layers': [{
                    'layer_name': 'input',
                    'layer_type': 'InputLayer',
                    'shape': [null, 1, 28, 28]
                }, {
                    'layer_name': 'conv2d1',
                    'layer_type': 'Conv2DLayer',
                    'num_filters': 32,
                    'filter_size': [5, 5],
                    'layer_nonlinearity': 'rectify',
                    'conv_window': 'glorotuniform'
                }, {
                    'layer_name': 'maxpool1',
                    'layer_type': 'MaxPool2DLayer',
                    'pool_size': [2, 2]
                }, {
                    'layer_name': 'conv2d2',
                    'layer_type': 'Conv2DLayer',
                    'num_filters': 32,
                    'filter_size': [5, 5],
                    'layer_nonlinearity': 'rectify',
                    'conv_window': null
                }, {
                    'layer_name': 'maxpool2',
                    'layer_type': 'MaxPool2DLayer',
                    'pool_size': [2, 2]
                }, {
                    'layer_name': 'dropout1',
                    'layer_type': 'DropoutLayer',
                    'dropout_pivot': 0.5
                }, {
                    'layer_name': 'dense',
                    'layer_type': 'DenseLayer',
                    'num_units': 256,
                    'layer_nonlinearity': 'rectify'
                }, {
                    'layer_name': 'dropout2',
                    'layer_type': 'DropoutLayer',
                    'dropout_pivot': 0.5
                }, {
                    'layer_name': 'output',
                    'layer_type': 'DenseLayer',
                    'num_units': 10,
                    'layer_nonlinearity': 'softmax'
                }],
                'update': 'nesterov_momentum',
                'update_learning_rate': 0.01,
                'update_momentum': 0.9,
                'max_epochs': 1,
                'verbose': 1
            }
        }

        metadata = metadataMapper[algorithm];
        if (!metadata) {
            metadata = {}
        }
        return metadata;

    }


    Accounts.get(function(response) {
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
    }, function() {
        console.log(error.data.message);
    });

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
