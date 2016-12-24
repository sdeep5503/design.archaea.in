angular
	.module('Dashboard')
	.directive('rdWidget', rdWidget)
	.directive('pageHeader', pageHeader);

function rdWidget () {
	var directive = {
		transclude: true,
        template: '<div class="widget" ng-transclude></div>',
        restrict: 'EA'
    };
    return directive;

    function link(scope, element, attrs) {
      /* */
    }
};


function pageHeader ()
{
    return {
        restrict: 'A',
        replace: true,
        templateUrl: "page-header.html",
        link: function ($scope) {
            scope.currentPageName = '';
            scope.currentPageDescription = '';
            scope.changePageInfoHeader = function (pageName)
            {
              var url = $window.location.href;
              var urlPath = url.split('/');
              var moduleName = urlPath[urlPath.length - 1]

              var headerMap = {
                'dashboard': 'Dashboard',
                'nerds': 'Manage Nerds',
                'tables': 'Manage Tables',
                'applications': 'Manage Applications'
              }

              var descriptionMap = {
                'dashboard': 'Latest updates from Nerdstacks',
                'nerds': 'Manage all your nerd clouds and use them to give life to your apps',
                'tables': 'Manage Tables',
                'applications': 'Manage Applications'
              }

              scope.currentPageName = headerMap[pageName ? pageName : moduleName];
              scope.currentPageDescription = descriptionMap[pageName ? pageName : moduleName];
            }
            scope.changePageInfoHeader();
        }
    }
}