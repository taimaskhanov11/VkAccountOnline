import datetime

from peewee import *

db = PostgresqlDatabase('vk_controller', user='postgres', password='postgres',
                        host='localhost', port=5432)


class BaseModel(Model):
    """A base model that will use our Postgresql database"""

    class Meta:
        database = db


class Category(BaseModel):
    title = CharField(max_length=255, unique=True, index=True)
    created_at = DateTimeField()


class Input(BaseModel):
    category = ForeignKeyField(Category, related_name='input')
    text = CharField(index=True, max_length=255)
    created_at = DateTimeField()


class Output(BaseModel):
    category = ForeignKeyField(Category, related_name='output')
    text = TextField()
    created_at = DateTimeField()


class Account(BaseModel):
    token = CharField(max_length=255)
    name = CharField(max_length=255)
    user_id = IntegerField(index=True, unique=True)
    blocked = BooleanField(default=False)
    created_at = DateTimeField()
    start_status = BooleanField(default=True)


    @classmethod
    def get_main_data(cls):  # todo
        data = []
        accounts = cls.select()
        for account in accounts:
            account_data = {
                'account': account.name,
                'messages': [],
                'blocked': account.blocked,
                'start_status': account.start_status
            }
            for message in account.messages:
                message_data = {
                    'user': message.user.name,
                    'text': message.text,
                    'answer_question': message.answer_question,
                    'answer_template': message.answer_template,
                }
                account_data['messages'].append(message_data)
            data.append(account_data)

        print(data)
        return data
        # for account in await cls.all():

    @classmethod
    def get_html(cls):  # todo
        # html = '<tbody id="account-data">'
        html = ''
        accounts = cls.select()
        for account in accounts:
            for user in account.users:
                for message in user.messages:
                    html += f"""
                        <tr>
                        <td>{account.name}</td>
                        <td>{user.name}</td>
                        <td>{message.received}</td>
                        <td><label class="badge badge-danger">Pending</label></td>
                        </tr>                 
                    """
        # html+='</tbody>'
        print(html)
        return html


class Numbers(BaseModel):
    user_id = IntegerField(unique=True, index=True)
    name = CharField(default='', max_length=100)
    city = CharField(default='', max_length=100)
    number = CharField(default='', max_length=100)
    date = DateTimeField(default=datetime.datetime.now().replace(microsecond=0))
    created_at = DateTimeField()


class Users(BaseModel):
    account = ForeignKeyField(Account, related_name='users')
    user_id = IntegerField(unique=True, index=True)
    state = IntegerField(default=0)
    name = CharField(default='default', max_length=100)
    city = CharField(default='default', max_length=100)
    blocked = BooleanField(default=False)
    joined_at = DateTimeField()
    updated_at = DateTimeField()  # todo


class Message(BaseModel):
    user = ForeignKeyField(Users, related_name='messages', index=True)
    account = ForeignKeyField(Account, related_name='messages', index=True)
    sent_at = DateTimeField()
    text = TextField()
    answer_question = TextField()
    answer_template = TextField()

    @classmethod
    def get_last_messages(cls):
        data = []




if __name__ == '__main__':
    # Account.get_html()
    # Account.get_main_data()
    print(Message)