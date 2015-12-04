var my_app = angular.module('myApp', []).config(function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});

my_app.controller('HelloController', function($scope, $http) {
        $scope.myData = {};
        $scope.user_text = '';
        $scope.result = '';
        $scope.rot = 0;
        $scope.reverse = {value: '', name: 'Transit', class: 'transit'};
        $scope.errors = '';
        $scope.legend = '';
        $scope.letters = '';
        $scope.test = 'test';
        $scope.showDiagram = function() {
            var revenueChart = new FusionCharts({
                    "type": "column2d",
                    "renderAt": "chartContainer",
                    "width": "100%",
                    "height": "300",
                    "dataFormat": "json",
                    "dataSource": {
                      "chart": {
                          "caption": "Analyzing your text",
                          "subCaption": "Count your char",
                          "xAxisName": "Your letter(s)",
                          "yAxisName": "Count(s)",
                          "theme": "fint"
                       },
                      "data": $scope.letters
                    }
                });
            revenueChart.render();
        }
        $scope.postAjax = function(event) {
            
            var ajaxSetting = {                    
                method: 'POST',
                url: '/',
                params: {
                    text: $scope.user_text,
                    rot: $scope.rot,
                    reverse: $scope.reverse.value,
                    legend: $scope.legend
                },
                cache: false,
            };

            var responsePromise = $http(ajaxSetting);

            responsePromise.success(function(data) {
                $scope.result = data.result;
                $scope.letters = data.letters;
                $scope.errors = '';
                $scope.showDiagram();
            });

            responsePromise.error(function(data) {
                $scope.errors = data;
            });
        };
        $scope.changeButt = function(event) {
            $scope.reverse.value = ($scope.reverse.value == '') ? true : '';
            $scope.reverse.name = ($scope.reverse.name == 'Transit') ? 'Encrypt' : 'Transit';
            $scope.reverse.class = ($scope.reverse.class == 'transit') ? 'encrypt' : 'transit';
        }
    });
        