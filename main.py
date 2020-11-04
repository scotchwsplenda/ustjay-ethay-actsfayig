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
    address = str(r.url)

    return '\n'.join([factstring, address])


@app.route('/')
def home():
    fact = get_fact().strip()
    address = pig_it(fact)

    return address

print(pig_it(get_fact()))
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

'''
General
    Request URL: http://hidden-journey-62459.herokuapp.com/piglatinize/
    Request Method: POST
    Status Code: 302 FOUND
    Remote Address: 52.200.31.227:80
    Referrer Policy: strict-origin-when-cross-origin
Response Headers
    Connection: keep-alive
    Content-Length: 293
    Content-Type: text/html; charset=utf-8
    Date: Wed, 04 Nov 2020 17:20:11 GMT
    Location: http://hidden-journey-62459.herokuapp.com/esultray/d60fad8e26807b03bb6347ca10c97cfa/
    Server: Werkzeug/0.14.1 Python/3.6.5
    Via: 1.1 vegur
Request Headers
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
    Accept-Encoding: gzip, deflate
    Accept-Language: en-US,en;q=0.9
    Cache-Control: max-age=0
    Connection: keep-alive
    Content-Length: 23
    Content-Type: application/x-www-form-urlencoded
    Host: hidden-journey-62459.herokuapp.com
    Origin: http://hidden-journey-62459.herokuapp.com
    Referer: http://hidden-journey-62459.herokuapp.com/
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36
Form Data
    input_text=I+am+sending
'''

'''
Use request library to send 
form data is a key value pair

General
    Request URL: http://hidden-journey-62459.herokuapp.com/piglatinize/
    Request Method: POST
Form Data
    input_text: I am sending
    '''