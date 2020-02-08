from src.masonite.orm.grammer.mysql_grammer import MySQLGrammer 
from src.masonite.orm.builder.QueryBuilder import QueryBuilder
from src.masonite.orm.grammer.GrammerFactory import GrammerFactory
from src.masonite.orm.models.Model import Model
import unittest

class MockUser(Model):

    __table__ = 'users'

class TestMySQLSelectConnection(unittest.TestCase):

    def setUp(self):
        self.builder = QueryBuilder(GrammerFactory.make('mysql'), table='users')

    def test_can_compile_select(self):
        to_sql = MockUser.where('id', 1).to_sql()

        sql = "SELECT * FROM `users` WHERE `id` = '1'"
        self.assertEqual(to_sql, sql)

    def test_can_get_first_record(self):
        user = MockUser.where('id', 1).first()
        self.assertEqual(user['id'], 1)

    def test_can_find_first_record(self):
        user = MockUser.find(1)
        self.assertEqual(user['id'], 1)

    def test_can_get_all_records(self):
        users = MockUser.all()
        print(users)
        self.assertGreater(len(users), 1)