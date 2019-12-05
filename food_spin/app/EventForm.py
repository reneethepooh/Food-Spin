from django import forms

class EventForm(forms.Form):
    event_name = forms.CharField(label='eventname', max_length=100)
    nickname = forms.CharField(label='eventname', max_length=100)
    location=forms.CharField(label='eventname', max_length=100)
    search_radius=forms.IntegerField(label='radius')
    food_query=forms.CharField(label='food', max_length=100)
    restrictions=forms.CharField(label='restrictions', max_length=100)
    open_to_all=forms.BooleanField(label='opentoall',required=False)
    gender_neutral=forms.BooleanField(label='gender_neutral',required=False)
    weel_chair=forms.BooleanField(label='weel_chair',required=False)
    waitlist=forms.BooleanField(label='waitlist',required=False)
    cashback=forms.BooleanField(label='cashback',required=False)


