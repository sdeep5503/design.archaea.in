

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
    def bot_to_json(bot=None):
        return {

            'bot_id': bot.bot_id,
            'bot_guid': bot.bot_guid,
            'account_id': bot.account_id,
            'bot_name': bot.bot_name,
            'is_active': bot.is_active,
            'is_deleted': bot.is_deleted,
            'bot_metadata': bot.metadata,
            'created_at': str(bot.created_at),
            'updated_at': str(bot.updated_at)

        }

    @staticmethod
    def bot_list_to_json_array(accounts=None):
        account_list = []
        for account in accounts:
            account_list.append(Transformer.account_to_json(account))
        return account_list

    @staticmethod
    def account_list_to_json_array(bots=None):
        bot_list = []
        for bot in bots:
            bot_list.append(Transformer.account_to_json(bot))
        return bot_list


