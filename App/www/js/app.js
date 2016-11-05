// Ionic Starter App

angular.module('starter', ['ionic', 'starter.controllers'])

.run(function($ionicPlatform) {
  $ionicPlatform.ready(function() {
    // Hide the accessory bar by default (remove this to show the accessory bar above the keyboard
    // for form inputs)
    if (window.cordova && window.cordova.plugins && window.cordova.plugins.Keyboard) {
      cordova.plugins.Keyboard.hideKeyboardAccessoryBar(true);
      cordova.plugins.Keyboard.disableScroll(true);

    }
    if (window.StatusBar) {
      // org.apache.cordova.statusbar required
      StatusBar.styleDefault();
    }

    var notificationOpenedCallback = function(jsonData) {
      console.log('notificationOpenedCallback: ' + JSON.stringify(jsonData));
    };

    var notificationReceivedCallback = function(jsonData) {
      console.log('notificationOpenedCallback: ' + JSON.stringify(jsonData));
    };

    window.plugins.OneSignal
      .startInit("<APP_ID>", "<GOOGLE_ID>")
      //.inFocusDisplaying(window.plugins.OneSignal.OSInFocusDisplayOption.None)
      // .handleNotificationOpened(notificationOpenedCallback)
      // .handleNotificationReceived(notificationReceivedCallback)
      .endInit();

      //window.plugins.OneSignal.setLogLevel({logLevel: 6, visualLevel: 4});

  });
})

.config(function($stateProvider, $urlRouterProvider) {

  // Ionic uses AngularUI Router which uses the concept of states
  // Learn more here: https://github.com/angular-ui/ui-router
  // Set up the various states which the app can be in.
  // Each state's controller can be found in controllers.js
  $stateProvider

  // setup an abstract state for the tabs directive
    .state('tab', {
    url: '/tab',
    abstract: true,
    templateUrl: 'templates/tabs.html'
  })

  // Each tab has its own nav history stack:

  .state('tab.config', {
    url: '/config',
    views: {
      'tab-config': {
        templateUrl: 'templates/tab-config.html',
        controller: 'ConfigCtrl'
      }
    }
  })

  .state('tab.temperatura', {
    url: '/temperatura',
    views: {
      'tab-temperatura': {
        templateUrl: 'templates/tab-temperatura.html',
        controller: 'TemperaturaCtrl'
      }
    }
  });

  // if none of the above states are matched, use this as the fallback
  $urlRouterProvider.otherwise('/tab/temperatura');

});
