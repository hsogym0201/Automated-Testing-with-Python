from models.item import ItemModel
from tests.base_test import BaseTest
from models.store import StoreModel

class StoreTest(BaseTest):
    def test_create_store(self):
        store = StoreModel('test')
        self.assertEqual(store.items.all(), [],
                         "The store's items length was not 0 even though no items were added.")

    def test_crud(self):
        with self.app_context():
            store =  StoreModel("test")
            self.assertIsNone(StoreModel.find_by_name("test"))

            store.save_to_db()
            self.assertIsNotNone(StoreModel.find_by_name("test"))

            store.delete_from_db()
            self.assertIsNone(StoreModel.find_by_name("test"))

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel("test")
            item = ItemModel("test_item", 6.66, 1)

            store.save_to_db()
            item.save_to_db()
            self.assertEqual(store.items.count(), 1)  # 外码约束测试
            self.assertEqual(store.items.first().name, "test_item") #外码约束测试

    def test_store_json(self):
        with self.app_context():
            store = StoreModel("test")
            item = ItemModel("test", 6.66, 1)

            store.save_to_db()
            item.save_to_db()

            expected = {
                "name": "test",
                "items": [{
                    "name": "test",
                    "price": 6.66,
                }]
            }
            self.assertEqual(store.json(), expected)
