from django import forms
from django.contrib import admin
from django.urls import path  # Add this import
from django.http import HttpResponseRedirect
from .models import Coupon
from django.urls import reverse
from django.utils.html import format_html
from django.http import HttpResponseNotFound
from django.views.decorators.http import require_POST


class UsageStatusFilter(admin.SimpleListFilter):
    title = 'Usage Status'  # Displayed filter title in the admin
    parameter_name = 'usage_status'  # URL parameter name for filtering

    def lookups(self, request, model_admin):
        # Define filter options and their human-readable labels
        return (
            ('used', 'Used'),
            ('not_used', 'Not Used'),
        )

    def queryset(self, request, queryset):
        # Apply the filter based on the selected option
        if self.value() == 'used':
            return queryset.filter(is_used=True)
        if self.value() == 'not_used':
            return queryset.filter(is_used=False)



class CouponBurnForm(forms.Form):
    coupon_code = forms.CharField(label="Coupon burn", max_length=6, required=True, widget=forms.TextInput(attrs={'size': '10'}))




class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount','customer_email', 'is_used','created_date', 'expiration_date')
    list_filter = ('is_used', 'expiration_date')  # Add filters for created_date and expiration_date
    search_fields = ('code', 'customer_email')  # Add search fields for code and customer_email
    date_hierarchy = 'created_date'  # Add date hierarchy for created_date
    ordering = ('-created_date',)  # Order by created_date in descending order

    


admin.site.register(Coupon, CouponAdmin)

