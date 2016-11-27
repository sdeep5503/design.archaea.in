import unittest
from models.users import Users
from api.services.nerd_service import BotService
from api.services.user_service import UserService
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
                                       account_name='Test Account')

        BotService.create_bot(account_guid='3d20edea-75f3-11e6-9737-08002713549c',
                              bot_guid='f02fb3d6-9f75-4f99-8bec-647a2b790d39',
                              bot_name='Batista',
                              bot_description='Unda',
                              is_deleted=False,
                              is_active=True,
                              bot_metadata='{cdmm:cnjd}',
                              bot_secret='nejkdne2122ne3kenkj3nj32o',
                              bot_key='1321322134332424',
                              user=UserService.get_user_by_email('system')[0])
