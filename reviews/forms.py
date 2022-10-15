from django.forms import ModelForm
from .models import Reviews


class ReviewsForm(ModelForm):
    class Meta:
        model = Review
        fields = ('content', )