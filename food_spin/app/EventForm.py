from django import forms

class EventForm(forms.Form):
    event_name = forms.CharField(label='Group Name', max_length=100)
    location=forms.CharField(label='Location ', max_length=100)
    search_radius=forms.IntegerField(label='radius')



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
