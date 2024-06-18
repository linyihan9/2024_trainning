import pytest
from core.db.connection import getDb

class TestDBConfig:
    USER = 'test_user'
    PWD = 'test_password'
    HOST = 'localhost'
    PORT = '3306'
    DATABASE = 'test_db'

# def test_getDb():

