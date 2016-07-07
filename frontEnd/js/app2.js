'use strict';

angular.module('myApp', [])
  .controller('MovieController', function($scope, $http){
    $scope.$watch('search', function() {
      fetch();
    });

    $scope.search = 'http://www.nltk.org/book/ch03.html';
    $scope.summary = '';

    function fetch(){
        $http.post('http://192.168.0.101:6166/keywords/', {'search': $scope.search})
          .then(function(response) {$scope.related = response.data;});

        $http.post('http://192.168.0.101:6166/summary/', {'search': $scope.search})
          .then(function(response) {$scope.summary = response.data;});
    };

//    function fetch(){
//    $http.post('http://127.0.0.1:6166/keywords/?search=' + encodeURIComponent($scope.search))
//    .then(function(response){ $scope.related = response.data; });
//    };

    $scope.update = function(movie){
      $scope.search = movie.Title;
    };

    $scope.select = function(){
      this.setSelectionRange(0, this.value.length);
    }
  });
