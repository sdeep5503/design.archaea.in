import unittest
from models.users import Users
from api.services.account_service import AccountsService
from tests.service_tests.test_data import TEST_USER


class AccountServiceTests(unittest.TestCase):

    def create_account_test(self):

        owner = Users(user_guid=TEST_USER['user_guid'],
                      email=TEST_USER['email'],
                      password=TEST_USER['password'],
                      first_name=TEST_USER['first_name'],
                      last_name=TEST_USER['last_name'],
                      company=TEST_USER['company']
                      )
        AccountsService.create_account(user=owner,
                                       account_name='Test Account',
                                       is_trail=1,
                                       is_enterprise=0)
