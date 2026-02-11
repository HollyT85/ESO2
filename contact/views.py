from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm



def contact(request):
    success = False

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            send_mail(
                subject="New Contact Form Submission",
                message=f"From: {email}\n\nMessage:\n{message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=["your@email.com"],  # change this
            )

            success = True
            form = ContactForm()  # reset form after sending

    else:
        form = ContactForm()

    return render(request, "contact/contact.html", {
        "form": form,
        "success": success
    })




