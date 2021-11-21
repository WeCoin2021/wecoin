from django.contrib import admin
from .models import Crypto, Store ,Transaction_history

admin.site.register(Crypto)
admin.site.register(Store)
admin.site.register(Transaction_history)