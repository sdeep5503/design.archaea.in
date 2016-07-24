import unittest
from models.users import Users
from dal.user_adapter import UserAdapter
from dal.accounts_adapter import AccountsAdapter
from dal.account_user_adapter import AccountUserAdapter


class DALCRUDUnitTests(unittest.TestCase):

    def create_new_user_with_account_tests(self):
        users = UserAdapter.read({
            'email': 'satis.vishnu@gmail.com'
        })
        if len(users) == 0:
            AccountsAdapter.create(
                account_name='satis.vishnu',
                account_guid='123-123-432-123',
                is_active=False,
                is_trail=True,
                is_enterprise=False,
                is_deleted=False,
                owner=Users(
                    user_guid='321-233-222-33',
                    email='satis.vishnu@gmail.com',
                    password='vizdsatiz',
                    first_name='viz',
                    last_name='satiz',
                    company='kony'
                )
            )
        accounts = AccountsAdapter.read({
            'account_guid': '123-123-432-123'
        })
        AccountUserAdapter.update({
            'account_guid': '123-123-432-123',
            'user_guid': '321-233-222-33',
        }, {
            'permission': 'owner'
        })
        self.assertEqual(len(accounts), 1)
