/**
 * Common Nerdstacks Services
 */
angular.module('nerdstacks', ['ngResource'])

    .service('api', function ($location) {
        var base = '/api/:version';
        if (nerdstacks_base_url) {
            base = $location.protocol() + '://' + nerdstacks_base_url + '/api/:version';
        }
        var o = {
            version: 'v1_0',
            accounts: base + '/accounts/:account_guid',
            authenticate: base + '/authenticate'
        };

        return angular.extend(o, {
            account_users: o.accounts + '/users/:user_guid'
        });
    })