from django import forms


# Форма контрольной работы
class ControlWorkForm(forms.Form):
    query_1_answer = forms.CharField(required=False)
    query_2_answer = forms.CharField(required=False)
    query_3_answer = forms.CharField(required=False)
