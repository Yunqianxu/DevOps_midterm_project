# Import ModelForm
from django.forms import ModelForm, forms
from django.contrib.auth.forms import UserCreationForm
# Import movie
from .models import Weight

class WeightForm(ModelForm):
    class Meta:
        model = Weight
        fields="__all__"
        exclude=["created_at"]
        
        