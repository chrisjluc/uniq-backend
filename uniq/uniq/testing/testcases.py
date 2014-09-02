from mongoengine import connect
from rest_framework.test import APITestCase
from django.conf import settings

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
        super(MongoTestCase, self)._post_teardown()