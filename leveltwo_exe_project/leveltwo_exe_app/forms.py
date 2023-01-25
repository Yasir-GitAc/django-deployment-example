from django import forms
from leveltwo_exe_app.models import User

class NewUserForm(forms.ModelForm):
  #if u want to do your custom validation fields will be here.(first_name=forms.Charfield(validators[])).

  class Meta():
    model = User
    fields = '__all__'

