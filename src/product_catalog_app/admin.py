from importlib.resources import read_text
from django.contrib import admin

from .models import Item, OrderItem, Order, UserProfile, CATEGORY_CHOICES


class myModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(myModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        
        return qs.filter(author=request.user)

def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)


make_refund_accepted.short_description = 'Update orders to refund granted'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                    ]
    list_display_links = [
        'user',
   
    ]
    list_filter = ['ordered',
                    ]
    search_fields = [
        'user__username',
        'ref_code'
    ]



  





admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(UserProfile)
admin.site.register(CATEGORY_CHOICES)
admin.site.register(Order, OrderAdmin)
