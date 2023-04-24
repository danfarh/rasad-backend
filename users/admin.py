from django.contrib import admin
from .models import (CustomUser,Activity,Company)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
	list_display = [
                    "email",
                    "first_name",
                    "last_name",
                    "phone_number",
                    "date_joined",
                    ]
	list_filter = ['date_joined',
                    'user_type',
                   ]
	fieldsets = (
        (None, {'fields': (
                        'first_name',
                        'last_name',
                        'email',
						'phone_number',
                        'password',
                        'user_type',
                        'boss_id',
                        )}),
        ('Permissions', {'fields': ('is_active',)}),
        ('coordinates', {'fields': ('center_x','center_y','radius')}),
    )
	search_fields = ['first_name',
                     'last_name',
                     'email',
                     'user_type',
                     ]
	ordering = ('email',)
	add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password'),
        }),
    )

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    pass
	
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ['category']
    list_display = ('id', 'name', 'category', 'boss_id')                
	