/**
 * Master Controller
 */
angular.module('Dashboard')
    .controller('MasterCtrl', ['$scope', '$cookieStore', '$window', MasterCtrl]);

function MasterCtrl($scope, $cookieStore, $window) {
    /**
     * Sidebar Toggle & Cookie Control
     *
     */
    var mobileView = 992;

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
      var url = $window.location.href;
      var urlPath = url.split('/');
      var moduleName = urlPath[urlPath.length - 1]

      var headerMap = {
        'dashboard': 'Dashboard',
        'nerds': 'Manage Nerds',
        'tables': 'Manage Tables',
        'applications': 'Manage Applications',
        'createUpdateApp': 'Create/Update Applications'
      }

      var descriptionMap = {
        'dashboard': 'Latest updates from Nerdstacks',
        'nerds': 'Manage all your nerd clouds and use them to give life to your apps',
        'tables': 'Manage Tables',
        'applications': 'Manage Applications',
        'createUpdateApp': 'Create/Update Applications'
      }

      $scope.currentPageName = headerMap[pageName ? pageName : moduleName];
      $scope.currentPageDescription = descriptionMap[pageName ? pageName : moduleName];
    }

    $scope.changePageInfoHeader();
}
