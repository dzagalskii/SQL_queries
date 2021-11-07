from django import forms


# Форма контрольной работы
class ControlWorkForm(forms.Form):
    first_query_answer = forms.CharField(required=False)
    second_query_answer = forms.CharField(required=False)
    third_query_answer = forms.CharField(required=False)
