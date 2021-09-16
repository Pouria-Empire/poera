from django import forms
from copo.models import Questions


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['title', 'description', 'test']
