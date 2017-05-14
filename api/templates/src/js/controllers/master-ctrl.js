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
    $scope.currentPageName = 'Nerd Console';
    $scope.currentPageDescription = 'Manage all your nerd clouds and apps give life to your apps';

    $scope.$on('GetAccountsSuccess', function() {
        $scope.accounts = $rootScope.accounts;
        $scope.currentAccount = $rootScope.current.account;
    });

    $scope.$on('WhoAmICallSuccess', function() {
        $scope.user = $rootScope.current.user;
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

    }

    $scope.logout = function () {
        // TODO clear client side tokens
        $window.location.href = '/login';
    }

    //$scope.changePageInfoHeader();
}
