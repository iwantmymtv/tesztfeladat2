from django.forms import ModelForm, fields
from .models import RecommendedProduct

class RecommendProductForm(ModelForm):
    class Meta:
        model = RecommendedProduct
        fields = ['name','image','description','category']