import unittest
import os
import sys
import json
from unittest.mock import patch

testdir = os.path.dirname(__file__)
srcdir = ".."
fullpath = os.path.abspath(os.path.join(testdir, srcdir))
sys.path.insert(0, fullpath)

from modules.DBHandler.handler import MyDatabase
from models.model import TestModel


class TestHandler(unittest.TestCase):
    def setUp(self):
        self.db = MyDatabase()
        self.db.connect_db("../db/test.sqlite")

    def tearDown(self):
        self.db.disconnect_db()

    def test_select_all(self):
        data = json.loads(self.db.select_all(TestModel))
        for row in data:
            self.assertEqual(row["success"], True)

    def test_where_name_is(self):
        data = json.loads(self.db.select_where_name_is(TestModel, "test1"))
        for row in data:
            self.assertEqual(row["success"], True)


if __name__ == "__main__":
    unittest.main()
