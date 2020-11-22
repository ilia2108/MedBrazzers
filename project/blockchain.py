import json
from flask import Blueprint, render_template
from flask import Flask, Response, request, jsonify, redirect, url_for
from marshmallow import Schema, fields, ValidationError
from flask_cors import CORS, cross_origin
from web3 import Web3
from flask_login import login_required, current_user

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
blockchain = Blueprint('blockchain', __name__)

def get_patients_from_contract(contract):
    func_to_call = 'patientCount'
    contract_func = contract.functions[func_to_call]
    patientCount = contract_func().call()

    patients=[]
    for i in range(patientCount):
        p = contract.functions.patients(i+1).call()
        patients.append(p)
    return patients

@blockchain.route("/addPatient", methods=['GET'])
@login_required
def addPatient():
    return render_template('add_patient.html')

# api to set new user every api call
@blockchain.route("/addPatient", methods=['POST'])
@login_required
def transaction():
    w3.eth.defaultAccount = w3.eth.accounts[0]
    with open("./project/data.json", 'r') as f:
        datastore = json.load(f)
    abi = datastore["abi"]
    contract_address = datastore["contract_address"]

    # Create the contract instance with the newly-deployed address
    contract = w3.eth.contract(
        address=contract_address, abi=abi,
    )
    body = {'uid':'','name':'','surname':'','birthdate':'','drugs':'','allergenes':'','healthproblems':''}
    for key in body:
        body[key] = request.form.get(key)

    tx_hash = contract.functions.createpatient(
        body['uid'],body['name'], body['surname'],body['birthdate'],
        body['drugs'],body['allergenes'],body['healthproblems']
    )
    tx_hash = tx_hash.transact()
    w3.eth.waitForTransactionReceipt(tx_hash)

    patients = get_patients_from_contract(contract)
    keys = [i for i in range(1,len(patients)+1)]
    responsedict = dict(zip(keys, patients))

    return redirect(url_for('main.profile'))




@blockchain.route("/qr", methods=['GET'])
@login_required
def getQR():
    w3.eth.defaultAccount = w3.eth.accounts[0]
    with open("./project/data.json", 'r') as f:
        datastore = json.load(f)
    abi = datastore["abi"]
    contract_address = datastore["contract_address"]

    # Create the contract instance with the newly-deployed address
    contract = w3.eth.contract(address=contract_address,abi=abi)
    patients = get_patients_from_contract(contract)
    for p in patients:
        if p[1] == current_user.uid:
            qr = p
            break


    keys = ["id","uid","name","surname","birthdate","drugs","allergenes","healthproblems"]
    responsedict = dict(zip(keys, qr))

    return jsonify(responsedict), 200








#
