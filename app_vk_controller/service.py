from enum import Enum, auto


class VkAccountDataMixin:
    extra_context = {'vk_accounts_active': 'active',
                     'vk_accounts_show': 'show'}


class MessageColumnEnum(Enum):
    Account = auto()
    User = auto()
    Incoming = auto()
    Answer = auto()
    Template = auto()
    Date = auto()
