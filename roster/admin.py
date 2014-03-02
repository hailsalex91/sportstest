from django.contrib import admin
from models import athlete, school, coach

# Register your models here.
class athleteAdmin(admin.ModelAdmin):
    search_fields = ('firstName',)
admin.site.register(athlete, athleteAdmin)
class schoolAdmin(admin.ModelAdmin):
    search_fields = ('name',)
admin.site.register(school, schoolAdmin)
class coachAdmin(admin.ModelAdmin):
    search_fields = ('name',)
admin.site.register(coach, coachAdmin)