from django import forms
from .widgets import CustomClearableFileInput
from .models import Clwb


class ClwbForm(forms.ModelForm):

    class Meta:
        model = Clwb
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        clwbs = Clwb.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in clwb]

        self.fields['clwb'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
