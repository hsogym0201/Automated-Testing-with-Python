from tests.base_test import BaseTest
from models.user import UserModel

class UserTest(BaseTest):
    def test_create_user(self):
        user = UserModel("test","test_pwd")
        self.assertEqual(user.username, "test",
                         "The name of the user after creation does not equal the constructor argument.")
        self.assertEqual(user.password, "test_pwd",
                         "The password of the user after creation does not equal the constructor argument.")