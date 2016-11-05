angular.module('starter.controllers', [])

.controller('ConfigCtrl', function($scope) {
  //alert('asdasd');

  $scope.config = {
    "intervaloMonitoramento": "Carregando...",
    "valorAlertaTemperaturaMaxima": "Carregando...",
    "valorAlertaTemperaturaMinima": "Carregando...",
    "valorAlertaUmidadeMaxima": "Carregando...",
    "valorAlertaUmidadeMinima": "Carregando..."
  };

  $scope.$on('$ionicView.enter', function(e) {
    var x = firebase.database().ref('config').once('value').then(function(d) {
      $scope.config = d.val(); 
      if (!$scope.$$phase)
        $scope.$apply();
      })
  });


  $scope.atualizar = function()
  {
       firebase.database().ref('config').set($scope.config).then(function (a,b) {
          alert('Valores atualizados!');
      });
  };
})

.controller('TemperaturaCtrl', function($scope) {

  $scope.inicio = {};
  $scope.fim = {};

  // $scope.inicio.date = new Date(2016,9,23);
  // $scope.inicio.data = formataData($scope.inicio.date);
  // $scope.fim.date = new Date(2016,9,24);
  // $scope.fim.data = formataData($scope.fim.date);

  $scope.$on('$ionicView.enter', function(e) {
    var x = firebase.database().ref('temperaturas')
                               .orderByChild("data")
                               .on('value', function(d) {
                                 $scope.temperaturas = ordenaValoresDecrescente(d.val()); 
                                  if (!$scope.$$phase)
                                     $scope.$apply();});
  });

  $scope.pesquisar = function() {
    if ($scope.inicio.date && $scope.fim.date)
    {
      firebase.database().ref('temperaturas').off('value');
      firebase.database().ref('temperaturas')
                        .orderByChild("data")
                        .startAt(dateToString($scope.inicio.date))
                        .endAt(dateToString($scope.fim.date))
                        .on('value', function(d) {
                          $scope.temperaturas = ordenaValoresDecrescente(d.val());
                          if (!$scope.$$phase)
                            $scope.$apply();
                    });
    }
  };

  function ordenaValoresDecrescente(obj) {
    var values = [];
    for (var key in obj) {
      if (Object.prototype.hasOwnProperty.call(obj, key))
          values.push(obj[key]);
    }
    return values.reverse();
  }

  function dateToString(x) {
    var mes = (x.getMonth() + 1);
    var dia = x.getDate();
    return x.getFullYear() + '-' + (mes < 10 ? "0"+mes : mes) + '-' + (dia <10 ? "0"+dia : dia);
  }

  function formataData(date) {
    var _date = new Date(date);
    var day = _date.getDate();
    var monthIndex = _date.getMonth() + 1;
    var year = _date.getFullYear();

    if (day < 10) {
        day = '0' + day;
    }
    if (monthIndex < 10) {
        monthIndex = '0' + monthIndex;
    }

    return day + '/' + monthIndex + '/' + year;
  }

  $scope.onDate = function (obj) {
            //Date
            var options = {
                date: new Date(),
                mode: 'date'
            };

            function onSuccessDate(date) {
                obj.date = date;
                obj.data = formataData(date);

                if (!$scope.$$phase)
                    $scope.$apply();
            }

            function onErrorDate(error) {
                
            }

            cordova.plugins.Keyboard.close();

            datePicker.show(options, onSuccessDate, onErrorDate);
  };

  $scope.settings = {
    enableFriends: true
  };
});
