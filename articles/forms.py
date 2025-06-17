from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'published']

    def clean_data(self):
        data = self.cleaned_data
        title = data.get('title')
        qs = Article.objects.filter(title__icontains=title)
        if qs.exists() :
            self.add_error('title', f"The {title} already exists") 
        # if not title :
        #     self.add_error('title', "Title cannot be empty")   
        return data
    
    # def clean_data(self):
    #     data = self.cleaned_data
    #     title = data.get('title')
    #     content = data.get('content')

    #     if title == content:
    #         raise forms.ValidationError("Title and content should not be the same")
        
    #     return data