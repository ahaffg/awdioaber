from django import forms
from .widgets import CustomClearableFileInput
from .models import category


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        blog_categories = Blog_category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in blog_categories]

        self.fields['blog_category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
