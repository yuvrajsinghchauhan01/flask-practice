from flask import Flask
import pickle
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return "<h1>Loan Application</h1>"

with open("classifier.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    loan_req = request.get_json()

    if loan_req['Gender'] == "Male":
        Gender = 0
    else:
        Gender = 1

    if loan_req['Married'] == "Unmarried":
        Married = 0
    else:
        Married = 1

    ApplicantIncome = loan_req['ApplicantIncome']
    # CoapplicantIncome = loan_req['CoapplicantIncome']
    LoanAmount = loan_req['LoanAmount']
    # Loan_Amount_Term = loan_req['Loan_Amount_Term']
    Credit_History = loan_req['Credit_History']

    prediction = model.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])
    if prediction == 1:
        pred =  "Loan Approved"
    else:
        pred =  "Loan Rejected"

    return {"prediction": pred}
