from django.contrib import admin
from .models import TodoItem
from .models import Artists
from .models import Concerts
from .models import client
from .models import payment
from .models import myTickets
from .models import cart


# Register your models here.
admin.site.register(TodoItem)
admin.site.register(Artists)
admin.site.register(Concerts)
admin.site.register(client)
admin.site.register(payment)
admin.site.register(myTickets)
admin.site.register(cart)