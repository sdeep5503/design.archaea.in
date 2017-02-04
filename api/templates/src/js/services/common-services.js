/**
 * Common Nerdstacks Services
 */
angular.module('nerdstacks.services', ['ngResource', 'ngCookies'])

    .factory('httpInterceptor', function ($window) {
        return {
            response: function (response) {
                if (response.status == 401 || response.status == 403) {
                    // TODO logout flow
                    $window.location.href = '/login';
                }
                return response;
            }
        }
    })

    .service('defaultRequestHeaders', function($cookieStore) {
        return {
            'Content-Type': 'application/json',
            'X-Request-Id': 'edjoijnpoi',
            'X-NS-Authorization': $cookieStore.get('ns_claims')
        }
    })

    .service('api', function ($location) {
        var base = '/api/:version';
        if (nerdstacks_base_url) {
            base = $location.protocol() + '://' + nerdstacks_base_url + '/api/:version';
        }
        var o = {
            version: 'v1_0',
            authenticate: base + '/authenticate',
            whoami: base + '/whoami',
            accounts: base + '/accounts',
            account: base + '/accounts/:account_guid'
        };

        return angular.extend(o, {
            nerds: o.account + '/nerds',
            applications: o.account + '/nerds/:nerd_guid/applications/:application_guid'
        });
    })

    .factory('Authenticate', function ($resource, api, defaultRequestHeaders) {
        return $resource(api.authenticate, {version: api.version}, {
            login: {method: 'POST', headers: defaultRequestHeaders}
        });
    })

    .factory('Whoami', function ($resource, api, defaultRequestHeaders) {
        return $resource(api.whoami, {version: api.version}, {
            get: {method: 'GET', headers: defaultRequestHeaders}
        });
    })

    .factory('Accounts', function ($resource, api, defaultRequestHeaders) {
        return $resource(api.accounts, {version: api.version}, {
            get: {method: 'GET', headers: defaultRequestHeaders, isArray: true}
        });
    })

    .factory('Nerds', function($resource, api, defaultRequestHeaders) {
        return $resource(api.nerds, {version: api.version}, {
            get: {method: 'GET', headers: defaultRequestHeaders, isArray:true}
        })
    })

    .factory('Applications', function($resource, api, defaultRequestHeaders) {
        return $resource(api.applications, {version: api.version}, {
            get: {method: 'GET', headers: defaultRequestHeaders, isArray:true},
            save: {method: 'POST', headers: defaultRequestHeaders},
            update: {method: 'PUT', headers: defaultRequestHeaders}
        })
    })

    .factory('Applications2', function($resource, api, defaultRequestHeaders) {
        return $resource(api.applications, {version: api.version}, {
            get: {method: 'GET', headers: defaultRequestHeaders}
        })
    })