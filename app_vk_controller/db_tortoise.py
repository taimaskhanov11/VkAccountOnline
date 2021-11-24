import asyncio
import datetime

from tortoise.models import Model
from tortoise import fields, Tortoise


class Category(Model):
    title = fields.CharField(max_length=255, unique=True, index=True)
    created_at = fields.DatetimeField(auto_now_add=True)


class Input(Model):
    category = fields.ForeignKeyField('models.Category', related_name='input')
    text = fields.CharField(index=True, max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)


class Output(Model):
    category = fields.ForeignKeyField('models.Category', related_name='output')
    text = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)


class Account(Model):
    token = fields.CharField(max_length=255)
    name = fields.CharField(max_length=255)
    user_id = fields.IntField(index=True, unique=True)
    blocked = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)

    @classmethod
    async def get_data(cls):  # todo
        data = {}
        accounts = await cls.all().prefetch_related('users')
        for account in accounts:
            data[account.name] = []
            for user in await account.users.all():
                user_data = {user.name: []}
                for message in await user.messages.all():
                    # user_data
                    user_data[user.name].append(message.received)
                    # print(account.name)
                    # print(user.name)
                    # print(message.received)
                data[account.name].append(user_data)
        print(data)
        return data
        # for account in await cls.all():

    @classmethod
    async def get_html(cls):  # todo
        # html = '<tbody id="account-data">'
        html = ''
        accounts = await cls.all().prefetch_related('users')
        for account in accounts:
            for user in await account.users.all():
                for message in await user.messages.all():
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


class Numbers(Model):
    user_id = fields.IntField(unique=True, index=True)
    name = fields.CharField(default='', max_length=100)
    city = fields.CharField(default='', max_length=100)
    number = fields.CharField(default='', max_length=100)
    date = fields.DatetimeField(default=datetime.datetime.now().replace(microsecond=0))
    created_at = fields.DatetimeField(auto_now_add=True)


class Users(Model):
    account = fields.ForeignKeyField('models.Account', related_name='users')
    user_id = fields.IntField(unique=True, index=True)
    state = fields.IntField(default=0)
    name = fields.CharField(default='default', max_length=100)
    city = fields.CharField(default='default', max_length=100)
    blocked = fields.BooleanField(default=False)
    joined_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now_add=True)  # todo


class Message(Model):
    user = fields.ForeignKeyField('models.Users', related_name='messages', index=True)
    sent_at = fields.DatetimeField(auto_now_add=True)
    received = fields.TextField()
    sent_by_bot = fields.TextField()


async def init():
    # Here we create a SQLite DB using file "db.sqlite3"
    # also specify the app name of "models"
    # which contain models from "app.models"
    await Tortoise.init(
        db_url='postgres://postgres:postgres@localhost:5432/vk_controller',
        # modules={'models': ['__main__']}
        modules={'models': ['app_vk_controller.database']}
    )
    # await Account.get_html()
    return await Account.get_html()

def main():
    loop = asyncio.new_event_loop()
    loop.run_until_complete(init())

if __name__ == '__main__':
    asyncio.run(init())
    pass
