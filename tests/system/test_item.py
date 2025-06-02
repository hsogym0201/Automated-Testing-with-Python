from tests.base_test import BaseTest
from models.item import ItemModel
from models.store import StoreModel
from models.user import UserModel
import json

class ItemTest(BaseTest):
    def setUp(self):
        super(ItemTest, self).setUp()
        with self.app() as c:
            with self.app_context():
                UserModel('test', '1234').save_to_db()
                auth_request = c.post('/auth', data=json.dumps({'username': 'test', 'password': '1234'}),
                                      headers={'Content-Type': 'application/json'})
                auth_token = json.loads(auth_request.data)['access_token']
                self.access_token = f"JWT {auth_token}"

    # Why failed?
    def test_get_item_no_auth(self):
        with self.app() as client:
            with self.app_context():
                resp = client.get('/item/test')
                print("Status Code:", resp.status_code)
                print("Response Data:", resp.data)
                self.assertEqual(resp.status_code, 401)

    def test_get_item_not_found(self):
        with self.app() as client:
            with self.app_context():
                resp = client.get('/item/test', headers={'Authorization': self.access_token})
                self.assertEqual(resp.status_code, 404)

    def test_get_item(self):
        with self.app() as client:
            with self.app_context():
                # StoreModel('test').save_to_db() # optional
                ItemModel("test_item", 6.66, 1).save_to_db()
                resp = client.get('/item/test_item', headers={'Authorization': self.access_token})
                self.assertEqual(resp.status_code, 200)
                self.assertDictEqual({"name": "test_item", "price":6.66},
                                     json.loads(resp.data))

    def test_delete_item(self):
        with self.app() as client:
            with self.app_context():
                # StoreModel("test").save_to_db() # optional
                # self.assertIsNone(ItemModel.find_by_name("test_item"))
                ItemModel("test_item", 6.66, 1).save_to_db()
                # self.assertIsNotNone(ItemModel.find_by_name("test_item"))

                resp = client.delete('/item/test_item')
                # self.assertIsNone(ItemModel.find_by_name("test_item"))
                self.assertEqual(resp.status_code, 200)
                self.assertDictEqual(d1={"message": "Item deleted"},
                                     d2=json.loads(resp.data))

    def test_create_item(self):
        with self.app() as client:
            with self.app_context():
                # StoreModel("test").save_to_db() # optional
                # self.assertIsNone(ItemModel.find_by_name("test_item"))
                resp = client.post('/item/test_item', data = json.dumps({"price": 6.66, "store_id": 1}),
                                                      headers={'Content-Type': 'application/json'})
                self.assertEqual(resp.status_code, 201) # 201: created
                # self.assertIsNotNone(ItemModel.find_by_name("test_item"))
                self.assertDictEqual({'name': 'test_item', 'price': 6.66},
                                     json.loads(resp.data))

    def test_create_duplicate_item(self):
        with self.app() as client:
            with self.app_context():
                # StoreModel("test").save_to_db() # optional
                # self.assertIsNone(ItemModel.find_by_name("test_item"))
                client.post('/item/test_item', data = json.dumps({"price": 6.66, "store_id": 1}),
                                               headers={'Content-Type': 'application/json'})
                # self.assertIsNotNone(ItemModel.find_by_name("test_item"))

                resp = client.post('/item/test_item', data = json.dumps({"price": 6.66, "store_id": 1}),
                                                      headers={'Content-Type': 'application/json'})
                self.assertEqual(resp.status_code, 400)
                self.assertDictEqual({'message': "An item with name \'test_item\' already exists."},
                                     json.loads(resp.data))

    def test_put_item(self):
        with self.app() as client:
            with self.app_context():
                # StoreModel("test").save_to_db() # optional
                # self.assertIsNone(ItemModel.find_by_name("test_item"))
                resp = client.put('/item/test_item', data = json.dumps({"price": 6.66, "store_id": 1}),
                                                      headers={'Content-Type': 'application/json'})
                self.assertEqual(resp.status_code, 200)
                # self.assertIsNotNone(ItemModel.find_by_name("test_item"))
                # self.assertEqual(ItemModel.find_by_name('test_item').price, 6.66)
                self.assertDictEqual({'name': 'test_item', 'price': 6.66},
                                     json.loads(resp.data))

    def test_put_update_item(self):
        with self.app() as client:
            with self.app_context():
                # StoreModel("test").save_to_db() # optional
                self.assertIsNone(ItemModel.find_by_name("test_item"))
                ItemModel("test_item", 8.88,1).save_to_db()
                self.assertEqual(ItemModel.find_by_name('test_item').price, 8.88)
                self.assertIsNotNone(ItemModel.find_by_name("test_item"))
                resp = client.put('/item/test_item', data = json.dumps({"price": 6.66, "store_id": 1}),
                                                      headers={'Content-Type': 'application/json'})
                self.assertEqual(resp.status_code, 200)
                self.assertEqual(ItemModel.find_by_name('test_item').price, 6.66)
                self.assertDictEqual({'name': 'test_item', 'price': 6.66},
                                     json.loads(resp.data))

    def test_item_list(self):
        with self.app() as client:
            with self.app_context():
                # StoreModel("test").save_to_db() # optional
                # self.assertIsNotNone(ItemModel.find_by_name("test_item"))
                ItemModel("test_item", 6.66,1).save_to_db()
                # self.assertIsNotNone(ItemModel.find_by_name("test_item"))

                resp = client.get('/items')
                self.assertEqual(resp.status_code, 200)
                self.assertDictEqual({"items": [{"name": "test_item", "price": 6.66}]},
                                     json.loads(resp.data))