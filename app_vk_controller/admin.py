from django.contrib import admin

# Register your models here.
from app_vk_controller.models import Account, User, Message, Number



class AccountAdmin(admin.ModelAdmin):
    pass

class MessageInline(admin.TabularInline):
    model = Message

class UserAdmin(admin.ModelAdmin):
    inlines = (MessageInline, )
    pass




class MessageAdmin(admin.ModelAdmin):
    pass


class NumberAdmin(admin.ModelAdmin):
    pass


# Re-register UserAdmin
admin.site.register(Account, AccountAdmin)
admin.site.register(User, UserAdmin)

admin.site.register(Message, MessageAdmin)
admin.site.register(Number, NumberAdmin)
