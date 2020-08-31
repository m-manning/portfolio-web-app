from django import forms

from .models import Post, CV

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CvForm(forms.ModelForm):

    class Meta:
        model = CV
        fields = ('education', 'tech_skills', 'work_experience', 'additional_skills',)