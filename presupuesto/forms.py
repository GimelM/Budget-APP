from django import forms

class ExpenseForm(forms.Form):
    titulo = forms.CharField()
    monto = forms.IntegerField()
    categoria = forms.CharField()