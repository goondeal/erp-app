from django import forms

from .models import Branch


class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = '__all__' #['id', 'custom_number', 'arabic_name', 'arabic_description', 'english_name', 'english_description', 'notes', 'address']
        exclude = ['created_at']
        # labels = {
        #     'id': 'Branch',
        #     'custom_number': 'Custom No',
        # }
        # widgets = {
        #     'id': forms.TextInput(attrs={'readonly': 'readonly'}),
        # }
# readonly_field = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'readonly': 'readonly'})
#     )

# fields = ["name", "title", "birth_date"]
#         labels = {
#             "name": _("Writer"),
#         }
#         help_texts = {
#             "name": _("Some useful help text."),
#         }