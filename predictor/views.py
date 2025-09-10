import joblib
import numpy as np
from django.shortcuts import render
from .forms import TransactionForm
import os

model_path = os.path.join(os.path.dirname(__file__), 'model', 'fraud_detection_model.pkl')
model = joblib.load(model_path)

def predict(request):
    result = None
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
  
            X = [[
                data['type'],
                data['amount'],
                data['oldbalanceOrg'],
                data['newbalanceOrig'],  
                data['oldbalanceDest'],
                data['newbalanceDest'],
            ]]
           
            import pandas as pd
            columns = ['type', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest']
            X_df = pd.DataFrame(X, columns=columns)
            print(X_df) 
            prediction = model.predict(X_df)[0]
            result = "Fraud" if prediction == 1 else "Not Fraud"
    else:
        form = TransactionForm()
    return render(request, 'predictor/predict.html', {'form': form, 'result': result})