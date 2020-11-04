import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()

def pig_it(pig):
    payload = dict(input_text=pig)
    r = requests.post('http://hidden-journey-62459.herokuapp.com/piglatinize/', data=payload)
    soup = BeautifulSoup(r.content, "html.parser")
    facts = soup.text
    factstring = str(facts.rsplit('Esultray')[1]).strip()
    return factstring

@app.route('/')
def home():
    fact = get_fact().strip()
    pigged = pig_it(fact)
    return pigged


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

'''
Use request library to send 
form data is a key value pair

General
    Request URL: http://hidden-journey-62459.herokuapp.com/piglatinize/
    Request Method: POST
Form Data
    input_text: I am sending
    '''