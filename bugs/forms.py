from django import forms
from .models import Bug, BugComment

class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields=('name','description','status','upvotes','views','author')
        
class BugCommentForm(forms.ModelForm):
    class Meta:
        model = BugComment
        fields=('description',)