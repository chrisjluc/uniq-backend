from mongoengine import connect
from rest_framework.test import APITestCase

from django.conf import settings
from django.core.cache import caches

class MongoTestCase(APITestCase):
    """
        TestCase class that clear the collection between the tests
    """
    mongodb_name = settings.MONGO_DATABASE_NAME
    
    def _pre_setup(self):
        from mongoengine.connection import connect, disconnect
        disconnect()
        connect(self.mongodb_name, port=settings.MONGO_PORT)
        super(MongoTestCase, self)._pre_setup()

    def _post_teardown(self):
        from mongoengine.connection import get_connection, disconnect
        connection = get_connection()
        connection.drop_database(self.mongodb_name)
        disconnect()
        caches['default'].clear()
        caches['school'].clear()
        caches['faculty'].clear()
        caches['program'].clear()
        caches['school_explore'].clear()
        caches['faculty_explore'].clear()
        caches['program_explore'].clear()
        super(MongoTestCase, self)._post_teardown()