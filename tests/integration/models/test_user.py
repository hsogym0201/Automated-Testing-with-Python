from tests.base_test import BaseTest
from models.user import UserModel

class UserTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            user =  UserModel("test", "test_pwd")
            self.assertIsNone(UserModel.find_by_username("test"))
            self.assertIsNone(UserModel.find_by_id(1))

            user.save_to_db()
            self.assertIsNotNone(UserModel.find_by_username("test"))
            self.assertIsNotNone(UserModel.find_by_id(1))