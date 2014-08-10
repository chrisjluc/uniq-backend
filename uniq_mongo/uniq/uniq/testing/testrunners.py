from django.test.simple import DjangoTestSuiteRunner
from mongoengine.python_support import PY3
from mongoengine import connect
from django.conf import settings

class MongoTestRunner(DjangoTestSuiteRunner):
    """
        A test runner that can be used to create, connect to, disconnect from, 
        and destroy a mongo test database for standard django testing.
    """

    mongodb_name = 'test_%s' % (settings.MONGO_DATABASE_NAME, )
    
    def setup_databases(self, **kwargs):
        from mongoengine.connection import connect, disconnect
        disconnect()
        connect(self.mongodb_name, port=settings.MONGO_PORT)
        print 'Creating mongo test database ' + self.mongodb_name
        return super(MongoTestRunner, self).setup_databases(**kwargs)

    def teardown_databases(self, old_config, **kwargs):
        from mongoengine.connection import get_connection, disconnect
        connection = get_connection()
        connection.drop_database(self.mongodb_name)
        print 'Dropping mongo test database: ' + self.mongodb_name
        disconnect()
        super(MongoTestRunner, self).teardown_databases(old_config, **kwargs)