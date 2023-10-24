from django import forms
class inputform(forms.Form):
    name=forms.CharField(max_length=15)
    roll_no=forms.IntegerField(help_text="Enter five digit roll no: ")
    password=forms.CharField(widget=forms.PasswordInput())
    