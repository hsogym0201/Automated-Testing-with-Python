from models.item import ItemModel
from tests.base_test import BaseTest
from models.store import StoreModel


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            store =  StoreModel("test")
            store.save_to_db()
            item = ItemModel('test', 19.99,1)

            self.assertIsNone(ItemModel.find_by_name('test'),
                              "Found an item with name {}, but expected not to.".format(item.name))

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('test'))

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('test'))

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel("test_store")
            item = ItemModel("test", 6.66, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(item.store.name, "test_store") #外码约束测试

