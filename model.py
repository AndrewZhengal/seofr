import datetime
import peewee_async
from peewee import *


connection = {
    'user': 'root',
    'password': '@SbbxrvbvSyarnzdj<',
    'host': 'localhost',
    'port': 3306,
}

db = peewee_async.MySQLDatabase('library2', autorollback=True, **connection)


class Page(Model):
    title = CharField(max_length=1024)
    title_len = IntegerField()
    response_time = FloatField()
    domain = CharField(max_length=1024, index=True)
    description = CharField(max_length=2024)
    description_len = IntegerField()
    h1 = CharField(max_length=1024)
    url = CharField(max_length=1024)
    scanned = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
        table_name = 'less_27'


objects = peewee_async.Manager(db)


if __name__ == '__main__':

    #db.drop_tables([Page])

    db.create_tables([Page])
