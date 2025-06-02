from tests.base_test import BaseTest
from models.user import UserModel
import json

class UserTest(BaseTest):
    def test_register_user(self):
        with self.app() as client:
            with self.app_context():
                self.assertIsNone(UserModel.find_by_username('test'))
                # response = client.post('/register', data = {'username': 'test', 'password': 'test_pwd'}) # not pass
                # reqparse（来自 flask_restful）默认会从这些地方找参数（按顺序）：
                # request.json, request.values（包含了 request.form + request.args）
                # Flask把data放进了request.form，而reqparse会在某些情况下忽略它，尤其当没有明确设置location = 'form'时

                # parser.add_argument('username', type=str, required=True, location='form')
                # parser.add_argument('password', type=str, required=True, location='form')
                response = client.post('/register',
                                      data = json.dumps({'username': 'test', 'password': 'test_pwd'}),
                                      headers={'Content-Type': 'application/json'})
                # response = client.post('/register', json = {'username': 'test', 'password': 'test_pwd'}) # equal
                self.assertEqual(response.status_code, 201)
                # print(f"\n Status code returned: {request.status_code}")
                self.assertIsNotNone(UserModel.find_by_username('test'))
                self.assertDictEqual({'message': 'User created successfully.'},
                                     json.loads(response.data))

    def test_register_and_login(self):
        with self.app() as client:
            with self.app_context():
                client.post('/register',
                            data = json.dumps({'username': 'test', 'password': 'test_pwd'}),
                            headers={'Content-Type': 'application/json'})
                auth_response = client.post('/auth',
                                           data = json.dumps({'username': 'test', 'password': 'test_pwd'}),
                                           headers={'Content-Type': 'application/json'})
                # 检查字典的键中是否包含 'access_token' 这个键
                self.assertIn('access_token', json.loads(auth_response.data).keys())

    def test_register_duplacate_user(self):
        with self.app() as client:
            with self.app_context():
                self.assertIsNone(UserModel.find_by_username("test"))
                client.post('/register',
                            data=json.dumps({'username': 'test', 'password': 'test_pwd'}),
                            headers={'Content-Type': 'application/json'})
                self.assertIsNotNone(UserModel.find_by_username("test"))
                response= client.post('/register',
                                      data = json.dumps({'username': 'test', 'password': 'test_pwd'}),
                                      headers={'Content-Type': 'application/json'})
                self.assertEqual(response.status_code, 400)
                self.assertDictEqual({'message': 'A user with that username already exists'},
                                     json.loads(response.data))
