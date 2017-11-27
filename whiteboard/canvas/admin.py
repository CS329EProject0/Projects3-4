from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User, Group, Permission
from .models import *

# Register your models here.
admin.site.register(Skill)
admin.site.register(Question)
admin.site.register(Quest)
admin.site.register(Quiz)
admin.site.register(SkillPoints)
admin.site.register(Assignment)
admin.site.register(Part)
admin.site.register(Score)
admin.site.register(Guild)