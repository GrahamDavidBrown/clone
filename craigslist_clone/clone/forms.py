from django import forms

class CityForm(forms.Form):
    your_city = forms.CharField(label='Select', max_length=100)


class RegistrationForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label='Password')


class NewListingForm(forms.Form):
    title = forms.CharField(label='title')
    description = forms.CharField(label='desctiption')
    picture_link = forms.CharField(label='picture link')
