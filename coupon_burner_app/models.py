from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime, timedelta



class Coupon(models.Model):
    code = models.CharField(unique=True, max_length=6)
   # Custom validator for discount field
    discount_validator = RegexValidator(
        regex='^(100|[1-9][0-9]|[1-9])%$',
        message='Discount must be between 1% and 100%.',
        code='invalid_discount'
    )

    discount = models.CharField(
        max_length=4,  # Limit to 4 characters (e.g., "100%")
        validators=[discount_validator],  # Apply custom validator
        blank=True,  # Allow blank values
    )
    is_used = models.BooleanField(default=False)
    created_date = models.DateTimeField (auto_now_add=True)
    expiration_date = models.DateField(default=(datetime.now() + timedelta(days=30)).date())
    customer_email = models.EmailField(null=True, blank=True) # Add unique=True

    def __str__(self):
        return str(self.code)

