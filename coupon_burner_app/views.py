# views.py
from django.http import JsonResponse
from django.core.mail import send_mail
from .models import Coupon  # Import your Coupon model

def handle_google_form_submission(request):
    if request.method == 'POST':
        # Parse form data from the POST request
        email = request.POST.get('email')  # Replace 'email' with the actual form field name

        # Generate a coupon (You can use your existing Coupon model)
        coupon = Coupon.objects.create(code='your_generated_code', discount='10%', customer_email=email)

        # Send the coupon to the user's email
        send_coupon_to_email(coupon)

        # Respond to the Google Form submission
        return JsonResponse({'message': 'Coupon sent successfully'})

    # Handle other HTTP methods or invalid requests
    return JsonResponse({'error': 'Invalid request'}, status=400)

def send_coupon_to_email(coupon):
    # Use Django's send_mail function or an email service to send the coupon to the user's email
    subject = 'Your Coupon'
    message = f'Here is your coupon code: {coupon.code}'
    from_email = 'your_email@example.com'  # Change this to your sender email
    recipient_list = [coupon.customer_email]

    send_mail(subject, message, from_email, recipient_list)
