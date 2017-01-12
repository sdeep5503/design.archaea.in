/**
 * Common Nerdstacks Services
 */
angular.module('nerdstacks.services', ['ngResource', 'ngCookies'])

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
            accounts: base + '/accounts/:account_guid',
            authenticate: base + '/authenticate',
            whoami: base + '/whoami'
        };

        return angular.extend(o, {
            account_users: o.accounts + '/users/:user_guid'
        });
    })

    .factory('Authenticate', function ($location, $resource, api, defaultRequestHeaders) {
        return $resource(api.authenticate, {version: api.version}, {
            login: {method: 'POST', headers: defaultRequestHeaders}
        });
    })

    .factory('Whoami', function ($resource, api, defaultRequestHeaders) {
        return $resource(api.whoami, {version: api.version}, {
            get: {method: 'GET', headers: defaultRequestHeaders}
        });
    })