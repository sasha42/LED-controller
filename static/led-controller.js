(function(angular) {
  'use strict';
angular.module('led-controller', [])
  .controller('LedController', function($http) {
    this.qty = 1;

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