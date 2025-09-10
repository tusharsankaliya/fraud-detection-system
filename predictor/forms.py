from django import forms

class TransactionForm(forms.Form):
    type = forms.ChoiceField(choices=[('CASH_OUT', 'CASH_OUT'), ('TRANSFER', 'TRANSFER'), ('PAYMENT', 'PAYMENT'), ('CASH_IN', 'CASH_IN'), ('DEBIT', 'DEBIT')])
    amount = forms.FloatField()
    oldbalanceOrg = forms.FloatField()
    newbalanceOrig = forms.FloatField()  # <-- Make sure this matches!
    oldbalanceDest = forms.FloatField()
    newbalanceDest = forms.FloatField()