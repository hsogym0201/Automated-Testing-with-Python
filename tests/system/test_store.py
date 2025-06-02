from models.item import ItemModel
from models.store import StoreModel
from tests.base_test import BaseTest
import json

class StoreTest(BaseTest):
    def test_create_store(self):
        with self.app() as client:
            with self.app_context():
                resp = client.post('/store/test')
                # /store/<string:name> 动态路径参数会自动从请求的URI中提取出来，并作为name参数传递给对应的资源方法Store post
                self.assertEqual(resp.status_code, 201) # 201: created
                self.assertIsNotNone(StoreModel.find_by_name("test"))
                self.assertDictEqual({'name': 'test', 'items': []},
                                     json.loads(resp.data))

    def test_create_duplicate_store(self):
        with self.app() as client:
            with self.app_context():
                # self.assertIsNone(StoreModel.find_by_name("test"))
                client.post('/store/test')
                # self.assertIsNotNone(StoreModel.find_by_name("test"))
                resp = client.post('/store/test')
                self.assertEqual(resp.status_code, 400)

    def test_delete_store(self):
        with self.app() as client:
            with self.app_context():
                # self.assertIsNone(StoreModel.find_by_name("test"))
                StoreModel("test").save_to_db() # independent, not "client.post('/store/test')"
                # self.assertIsNotNone(StoreModel.find_by_name("test"))
                resp = client.delete('/store/test')  # GET, POST, DELETE, PUT, PATCH, OPTIONS...
                # self.assertIsNone(StoreModel.find_by_name("test"))
                self.assertEqual(resp.status_code, 200)
                self.assertDictEqual(d1={'message': 'Store deleted'},
                                     d2=json.loads(resp.data))

    def test_find_store(self):
        with self.app() as client:
            with self.app_context():
                # self.assertIsNone(StoreModel.find_by_name("test"))
                StoreModel("test").save_to_db() # independent, not "client.post('/store/test')"
                # self.assertIsNotNone(StoreModel.find_by_name("test"))
                resp = client.get('/store/test')
                self.assertEqual(resp.status_code, 200)
                self.assertDictEqual({"name": "test", "items":[]},
                                     json.loads(resp.data))

    def test_store_not_found(self):
        with self.app() as client:
            with self.app_context():
                # self.assertIsNone(StoreModel.find_by_name("test"))
                resp = client.get('/store/test')
                self.assertEqual(resp.status_code, 404)
                self.assertDictEqual({'message': 'Store not found'},
                                     json.loads(resp.data))

    def test_store_with_items_found(self):
        with self.app() as client:
            with self.app_context():
                # self.assertIsNone(StoreModel.find_by_name("test"))
                StoreModel("test").save_to_db()
                # self.assertIsNotNone(StoreModel.find_by_name("test"))
                # self.assertIsNone(ItemModel.find_by_name("test_item"))
                ItemModel("test_item", 6.66,1).save_to_db()
                # self.assertIsNotNone(ItemModel.find_by_name("test_item"))

                resp = client.get('/store/test')
                self.assertEqual(resp.status_code, 200)
                self.assertDictEqual({"name": "test", "items":[{"name": "test_item", "price": 6.66}]},
                                     json.loads(resp.data))

    def test_store_list(self):
        with self.app() as client:
            with self.app_context():
                # self.assertIsNone(StoreModel.find_by_name("test"))
                StoreModel("test").save_to_db()
                # self.assertIsNotNone(StoreModel.find_by_name("test"))

                resp = client.get('/stores')
                self.assertEqual(resp.status_code, 200)
                self.assertDictEqual({"stores": [{"name": "test", "items":[]}]},
                                     json.loads(resp.data))

    def test_store_with_items_list(self):
        with self.app() as client:
            with self.app_context():
                # self.assertIsNone(StoreModel.find_by_name("test"))
                StoreModel("test").save_to_db()
                # self.assertIsNotNone(StoreModel.find_by_name("test"))

                # self.assertIsNone(ItemModel.find_by_name("test_item"))
                ItemModel("test_item", 6.66,1).save_to_db()
                # self.assertIsNotNone(ItemModel.find_by_name("test_item"))

                resp = client.get('/stores')
                self.assertEqual(resp.status_code, 200)
                self.assertDictEqual({"stores": [{"name": "test", "items":[{"name": "test_item", "price": 6.66}]}]},
                                     json.loads(resp.data))