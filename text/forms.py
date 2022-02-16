from cProfile import label
from dataclasses import field
from pyexpat import model
from django import  forms
from .models import Studenttxt

class Generation(forms.ModelForm):
    # q_txt = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control','autofocus':True
    # }), label_suffix='')
    class Meta:
        model = Studenttxt
        fields = ['q_txt']
        labels= {'q_txt':'Text'}
        label_suffix = ''
        
        widgets = {
            'q_txt':forms.Textarea(attrs={'class':'form-control','autofocus':True}),
           }
    



# class StudentGeneralSearch(forms.ModelForm):
#     class Meta:
#         model = StudentSearch
#         fields = ['query']
#         labels = {'query':'Search'}
#         widgets = {
#             'query': forms.TextInput(attrs = {'class':'form-control', 'autofocus':True})
#             }



