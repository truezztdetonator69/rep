from django.contrib import admin
from django.db import models

from .models import Team, Person

admin.site.register(Team)
admin.site.register(Person)

