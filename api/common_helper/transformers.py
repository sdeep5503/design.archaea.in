from json import loads


class Transformer:

    def __init__(self):
        pass

    @staticmethod
    def account_to_json(account=None):
        return {

            'account_id': account.account_id,
            'account_guid': account.account_guid,
            'account_name': account.account_name,
            'account_type': account.account_type,
            'is_active': account.is_active,
            'is_deleted': account.is_deleted,
            'created_at': str(account.created_at),
            'updated_at': str(account.updated_at)

        }

    @staticmethod
    def nerd_to_json(nerd=None):
        return {

            'nerd_id': nerd.nerd_id,
            'nerd_guid': nerd.nerd_guid,
            'account_id': nerd.account_id,
            'nerd_name': nerd.nerd_name,
            'nerd_url': nerd.nerd_url,
            'is_active': nerd.is_active,
            'is_deleted': nerd.is_deleted,
            'created_at': str(nerd.created),
            'updated_at': str(nerd.updated)

        }

    @staticmethod
    def account_list_to_json_array(accounts=None):
        account_list = []
        for account in accounts:
            account_list.append(Transformer.account_to_json(account))
        return account_list

    @staticmethod
    def nerd_list_to_json_array(nerds=None):
        nerd_list = []
        for nerd in nerds:
            nerd_list.append(Transformer.nerd_to_json(nerd))
        return nerd_list


