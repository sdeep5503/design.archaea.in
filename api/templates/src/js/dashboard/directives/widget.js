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

        }
    }
}