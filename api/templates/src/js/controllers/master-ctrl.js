/**
 * Master Controller
 */
angular.module('nerdstacks')
    .controller('MasterCtrl', ['$scope', '$rootScope', '$cookieStore', '$window', 'Whoami', 'Accounts', MasterCtrl]);

function MasterCtrl($scope, $rootScope, $cookieStore, $window, Whoami, Accounts) {
    /**
     * Sidebar Toggle & Cookie Control
     *
     */
    var mobileView = 992;
    $scope.user = {};
    $scope.accounts = [];
    $scope.currentAccount = {};
    $rootScope.current = {};
    $scope.currentPageName = 'Nerd Console';
    $scope.currentPageDescription = 'Manage all your nerd clouds and apps give life to your apps';

    Whoami.get(function(response) {
        $scope.user = response;
    }, function(error) {
        console.log(error.data.message);
    });

    Accounts.get(function(response) {
        $scope.accounts = response;
        $rootScope.current.account = $scope.accounts[0];
        $scope.currentAccount = $scope.accounts[0];
    }, function() {
        console.log(error.data.message);
    });

    $scope.getWidth = function() { return window.innerWidth; };

    $scope.$watch($scope.getWidth, function(newValue, oldValue)
    {
        if(newValue >= mobileView)
        {
            if(angular.isDefined($cookieStore.get('toggle')))
            {
                if($cookieStore.get('toggle') == false)
                {
                    $scope.toggle = false;
                }
                else
                {
                    $scope.toggle = true;
                }
            }
            else
            {
                $scope.toggle = true;
            }
        }
        else
        {
            $scope.toggle = false;
        }

    });

    $scope.toggleSidebar = function()
    {
        $scope.toggle = ! $scope.toggle;

        $cookieStore.put('toggle', $scope.toggle);
    };

    window.onresize = function() { $scope.$apply(); };

    $scope.changePageInfoHeader = function (pageName)
    {
      /**var url = $window.location.href;
      var urlPath = url.split('/');
      var moduleName = urlPath[urlPath.length - 1]

      var headerMap = {
        'dashboard': 'Dashboard',
        'nerds': 'Manage Nerds',
        'users': 'Manage Users',
        'tables': 'Manage Tables',
        'applications': 'Manage Applications',
        'createUpdateApp': 'Create/Update Applications',
        'documentations': 'Documentations'
      }

      var descriptionMap = {
        'dashboard': 'Latest updates from Nerdstacks',
        'nerds': 'Manage all your nerd clouds and use them to give life to your apps',
        'users': 'Manage all the users in this account',
        'tables': 'Manage Tables',
        'applications': 'Manage Applications',
        'createUpdateApp': 'Create/Update Applications',
        'documentations': 'All the important documentations that you need'
      }

      $scope.currentPageName = headerMap[pageName ? pageName : moduleName];
      $scope.currentPageDescription = descriptionMap[pageName ? pageName : moduleName];**/
    }

    $scope.logout = function () {
        // TODO clear client side tokens
        $window.location.href = '/login';
    }

    //$scope.changePageInfoHeader();
}
