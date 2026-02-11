from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(
        label="Email address",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "name@example.com"
        })
    )

    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 4
        })
    )

    human_check = forms.BooleanField(
        label="I am human",
        required=True
    )
