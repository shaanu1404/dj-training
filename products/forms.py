from django import forms

from . import models


class ProductForm(forms.ModelForm):

    class Meta:
        model = models.Product
        fields = "__all__"

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3
            }),
            "price": forms.NumberInput(attrs={
                "class": "form-control",
                "step": 1
            }),
            "category": forms.Select(attrs={
                "class": "form-control"
            }),
        }

        help_texts = {
            'title': "Product name"
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise forms.ValidationError("Please enter title")
        return title

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("Price is less than 0")

        return price

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data['title']
        print(title)
        # Check validation
        return cleaned_data


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=20,
        required=True,
        help_text="Enter your name",
        label="Fullname",
        widget=forms.TextInput(attrs={
            "class": "form-control"
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "form-control"
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 3
        })
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['message'].help_text = "Enter your message"
