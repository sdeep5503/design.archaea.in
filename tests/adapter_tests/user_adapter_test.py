import unittest
from dal.user_adapter import UserAdapter


class UserAdapterTests(unittest.TestCase):

    def __init__(self):
        super(UserAdapterTests, self).__init__()

    def sql_exception_handling_test(self):
        try:
            UserAdapter.create(user_guid='hiknhk',
                               email=None,
                               password=None,
                               first_name='vuhvj',
                               last_name='fyugu',
                               is_system=False,
                               company='jfyugub')
        except Exception as e:
            print e.message

        try:
            UserAdapter.create(user_guid='hiknhk',
                               email=None,
                               password=None,
                               first_name='vuhvj',
                               last_name='fyugu',
                               is_system=False,
                               company='jfyugub')
        except Exception as e:
            print e.message

