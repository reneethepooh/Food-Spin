from django import forms
from .models import Event

class EventForm(forms.ModelForm):
        class Meta:
            model = Event
            fields=[
                'name',
                'link',
                'status',
                'location',
                'radius'
            ]
# name = models.CharField(max_length=30),
# 	leader = models.ForeignKey(User, on_delete=models.CASCADE),
# 	followers = models.ManyToManyField(User),
# 	link = models.TextField(),
# 	status = models.CharField(max_length=15),
# 	location = models.CharField(max_length=30),
# 	radius = models.IntegerField()


    # event_name = forms.CharField(label='Group Name', max_length=100)
    # location=forms.CharField(label='Location ', max_length=100)
    # search_radius=forms.IntegerField(label='radius')




# For event submission form: 

#     food_query=forms.CharField(label='food', max_length=100)
#     restrictions=forms.CharField(label='restrictions', max_length=100)
#     open_to_all=forms.BooleanField(label='opentoall',required=False)
#     gender_neutral=forms.BooleanField(label='gender_neutral',required=False)
#     weel_chair=forms.BooleanField(label='weel_chair',required=False)
#     waitlist=forms.BooleanField(label='waitlist',required=False)
#     cashback=forms.BooleanField(label='cashback',required=False)
# # No leader needed
#  No followers as thats gonna be 
# 


# Change the url from pref to create evebnt
# Update links
# Forms need to post to the same url as event creation
# In views, handle post request to c reate a new event obeject
#     no worry about user
