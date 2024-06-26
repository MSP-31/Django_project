from django import forms
from .models import Intro,Instructors

class IntroForm(forms.ModelForm):
    class Meta:
        model = Intro
        fields = ['title', 'contents','image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'width'}),
            'contents': forms.Textarea(attrs={'class': 'width'}),
            'image': forms.FileInput(attrs={'required': False}),
        }

class InstructorsForm(forms.ModelForm):
    class Meta:
        model = Instructors
        fields = ['name', 'contents','image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'width'}),
            'contents': forms.Textarea(attrs={'class': 'width'}),
            'image': forms.FileInput(attrs={'required': False}),
        }
        labels = {
            'name': '강사명',
            'contents': '내용',
            'image': '이미지',
        }
        error_messages = {
            'name' : {
                'required' : '제목을 입력해주세요',
                'max_length' : '제목은 50 글자 이하로 입력해야 합니다.',
            },
            'contents' : {
                'required' : '내용을 입력해주세요.',
                'max_length' : '내용은 3000 글자 이하로 입력해야 합니다.',
            },
        }