from django import forms

class EventForm(forms.Form):
    event_name = forms.CharField(label='Group Name', max_length=100)
    location = forms.CharField(label='Location ', max_length=100)
    search_radius = forms.IntegerField(label='radius')

class RestrictionForm(forms.Form):
    restriction = forms.CharField(label='New Restriction', max_length=20)

class SubmissionForm(forms.Form):
    preference = forms.CharField(label='Preference', max_length=20)