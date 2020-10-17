from flask import Flask, render_template, redirect, request, url_for, session
from flask import json
from flask import jsonify
import requests
import os
from pprint import pprint

app = Flask(__name__)
subscription_key = "10ed6ba7b3d4497096beabf32a4c9d39"
endpoint = "https://nrrecluters.cognitiveservices.azure.com/"
language_api_url = endpoint + "/text/analytics/v3.0/languages"

def detectar(texto):
    documents = {"documents": [
        {"id": "1", "text": texto}
    ]}
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    response = requests.post(language_api_url, headers=headers, json=documents)
    languages = response.json()
    pprint(languages)
    return languages    

@app.route('/',methods=['GET','POST'])
def Index():
    if request.method == 'POST':
        print("detectando idioma")
        Bomba = request.form['Bomba']
        res=detectar(Bomba)
        return json.dumps(res)

    else:
        return render_template('Rusia.html')

'''
@app.route('/Rusia', methods=['GET','POST'])
def Rusia():
    if request.method == 'POST':
        print("acac form")
        Bomba = request.form['Bomba']
        res=detectar(Bomba)
        return jsonify(res)

    else:
        return render_template('Rusia copy.html')
'''
if __name__ == '__main__': 
    app.run(debug=True)






#print("teamovic")


