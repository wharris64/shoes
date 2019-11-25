from django.forms import ModelForm
from ghostpost.models import RoastBoast

class RoastBoastAdd(ModelForm):
    class Meta:
        model = RoastBoast
        fields = ['roast', 'content']
