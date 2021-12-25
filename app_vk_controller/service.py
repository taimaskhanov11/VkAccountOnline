from enum import Enum, auto


class MessageColumnEnum(Enum):
    Account = 1
    User = 2
    Text = 3
    Answer = 4
    Template = 5
    Date = 6
    Account_ID = 10
    User_ID = 11


class VkAccountDataMixin:
    column_enum = MessageColumnEnum

    extra_context = {'vk_accounts_active': 'active',
                     'vk_accounts_show': 'show',
                     'table_fields': column_enum._member_names_[:6]
                     }

# print(MessageColumnEnum.User_ID == MessageColumnEnum(2))

