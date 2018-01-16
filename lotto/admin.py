from django.contrib import admin

#from lotto.models import GuessNumbers : same package -> okay to write .models
from .models import GuessNumbers

# Register your models here.
admin.site.register(GuessNumbers)
