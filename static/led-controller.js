(function(angular) {
  'use strict';
angular.module('led-controller', ['rzModule'])
  .controller('LedController', function($http, $scope) {
    $scope.create
    this.qty = 1;

    $scope.slider = {
        minValue: 10,
        maxValue: 90,
        options: {
            floor: 0,
            ceil: 100,
            step: 1
        }
    };

    this.on = function on() {

		var root = 'http://localhost:8000/';

		$http({
		  url: root + '/api',
		  data: '{"0":4094,"1":4094,"2":4094}',
		  method: 'POST'
		}).then(function successCallback(response) {
			console.log(response)
		  }, function errorCallback(response) {
		  	console.log("Error!")
		  	console.log(response)
		  });

	    window.alert("Everything turned on");
    };
  });
})(window.angular);