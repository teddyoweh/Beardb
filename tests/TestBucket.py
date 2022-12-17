import unittest
import uuid
import os
import base64
from cryptography.fernet import Fernet
import ast
from src.Beardb.Bucket import Bucket
class TestBucket(unittest.TestCase):
    def setUp(self):
        self.key = open('key.key','rb').read()
        self.fernet = Fernet(self.key)
        self.project = object()
        self.project.project = 'test_project'
        self.project.database = 'test_database'
        self.bucket_name = 'test_bucket'
        self.bucket = Bucket(self.project, self.bucket_name)

    def test_insert(self):
 
        data = {'name': 'John', 'age': 30}
        self.bucket.insert(data)

        
        json_file = open(self.bucket.path_(self.project.database+'/'+self.bucket_name+'.bdb'),'rb').read()
        data_list = self.fernet.decrypt(json_file).decode()
        data_list = ast.literal_eval(data_list)
        self.assertEqual(len(data_list), 1)
        self.assertEqual(data_list[0]['name'], 'John')
        self.assertEqual(data_list[0]['age'], 30)
    def test_fetchManybyId(self):
        # Test fetching multiple items by id from the bucket
        data1 = {'name': 'John', 'age': 30, 'id': str(uuid.uuid1())}
        data2 = {'name': 'Jane', 'age': 25, 'id': str(uuid.uuid1())}
        self.bucket.insert(data1)
        self.bucket.insert(data2)

        # Verify that the correct items are fetched
        result = self.bucket.fetchManybyId([data1['id'], data2['id']])
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['name'], 'John')
        self.assertEqual(result[0]['age'], 30)
        self.assertEqual(result[1]['name'], 'Jane')
        self.assertEqual(result[1]['age'], 25)
    def test_fetchbyId(self):
        # Test fetching an item by id from the bucket
        data1 = {'name': 'John', 'age': 30, 'id': str(uuid.uuid1())}
        data2 = {'name': 'Jane', 'age': 25, 'id': str(uuid.uuid1())}
        self.bucket.insert(data1)
        self.bucket.insert(data2)

        # Verify that the correct item is fetched
        result = self.bucket.fetchbyId(data1['id'])
        self.assertEqual(result['name'], 'John')
        self.assertEqual(result['age'], 30)

        # Verify that an exception is raised when the item is not found
        with self.assertRaises(Exception):
            result = self.bucket.fetchbyId(str(uuid.uuid1()))
    def test_update(self):
        # Test updating an item in the bucket
        data1 = {'name': 'John', 'age': 30, 'id': str(uuid.uuid1())}
        self.bucket.insert(data1)

        # Update the item and verify that it was updated correctly
        data1['name'] = 'Jane'
        self.bucket.update(data1['id'], data1)
        result = self.bucket.fetchbyId(data1['id'])
        self.assertEqual(result['name'], 'Jane')
        self.assertEqual(result['age'], 30)

        # Verify that an exception is raised when the item is not found
        with self.assertRaises(Exception):
            self.bucket.update(str(uuid.uuid1()), data1)

    def test_updatebyId(self):
        # Test updating an item by id in the bucket
        data1 = {'name': 'John', 'age': 30, 'id': str(uuid.uuid1())}
        data2 = {'name': 'Jane', 'age': 25, 'id': str(uuid.uuid1())}
        self.bucket.insert(data1)
        self.bucket.insert(data2)

        # Update the first item
        self.bucket.updatebyId(data1['id'], {'name': 'John', 'age': 35})

        # Verify that the item was updated
        json_file = open(self.bucket.path_(self.project.database+'/'+self.bucket_name+'.bdb'),'rb').read()
        data_list = self.fernet.decrypt(json_file).decode()
        data_list = ast.literal_eval(data_list)
        self.assertEqual(len(data_list), 2)
        self.assertEqual(data_list[0]['name'], 'John')
        self.assertEqual(data_list[0]['age'], 35)
        self.assertEqual(data_list[1]['name'], 'Jane')
    def test_fetchData(self):
        # Test fetching all data from the bucket
        data1 = {'name': 'John', 'age': 30, 'id': str(uuid.uuid1())}
        data2 = {'name': 'Jane', 'age': 25, 'id': str(uuid.uuid1())}
        self.bucket.insert(data1)
        self.bucket.insert(data2)

        # Verify that all data is fetched
        result = self.bucket.fetchData()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['name'], 'John')
        self.assertEqual(result[0]['age'], 30)
        self.assertEqual(result[1]['name'], 'Jane')
        self.assertEqual(result[1]['age'], 25)
    def test_deleteData(self):
        # Test deleting an item from the bucket
        data1 = {'name': 'John', 'age': 30, 'id': str(uuid.uuid1())}
        data2 = {'name': 'Jane', 'age': 25, 'id': str(uuid.uuid1())}
        self.bucket.insert(data1)
        self.bucket.insert(data2)

        # Delete one of the items and verify that it was removed
        self.bucket.deleteData(data1['id'])
        json_file = open(self.bucket.path_(self.project.database+'/'+self.bucket_name+'.bdb'),'rb').read()
        data_list = self.fernet.decrypt(json_file).decode()
        data_list = ast.literal_eval(data_list)
        self.assertEqual(len(data_list), 1)
        self.assertEqual(data_list[0]['name'], 'Jane')
        self.assertEqual(data_list[0]['age'], 25)

        # Verify that an exception is raised when the item is not found
        with self.assertRaises(Exception):
            self.bucket.deleteData(str(uuid.uuid1()))



 

