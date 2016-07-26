import unittest
from models.users import Users
from dal.user_adapter import UserAdapter
from dal.accounts_adapter import AccountsAdapter
from dal.account_user_adapter import AccountUserAdapter


class DALCRUDUnitTests(unittest.TestCase):

    def create_new_user_with_account_tests(self):
        users = UserAdapter.read({
            'email': 'satis.vis2nu@gmail.com'
        })
        if len(users) == 0:
            AccountsAdapter.create(
                account_name='satis.vishnu',
                account_guid='1213-1231-2132',
                is_active=False,
                is_trail=True,
                is_enterprise=False,
                is_deleted=False,
                owner=Users(
                    user_guid='321-233-2223432-33',
                    email='satis.vis2nu@gmail.com',
                    password='vizdssiz',
                    first_name='viz',
                    last_name='satizwd',
                    company='kokny'
                )
            )
        accounts = AccountsAdapter.read({
            'account_guid': '123-123-432-123'
        })
        AccountUserAdapter.update({
            'account_guid': '123-123-432-123',
            'user_guid': '321-233-222-33',
        }, permission='owner')
#       self.assertEqual(len(accounts), 1)

    @staticmethod
    def get_accounts_by_guid_list_test():
        AccountUserAdapter.read({
            'user_guid': '321-233-222-33'
        })
        #list = ['1213-1231-2132','123-123-432-123']
        #print AccountsAdapter.read_accounts_by_guids(list)

