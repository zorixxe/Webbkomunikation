from flask import Flask, request, jsonify
from flask_cors import CORS 


app = Flask(__name__)
CORS(app) # Tillåt cross-origin requests

@app.route("/")
def hello():
    ip_addr = request.remote_addr
    return "my ip! " + ip_addr

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8440, debug=True)


# Instruktioner
#
# FÖRSTA GÅNGEN:
# - I denna katalog, kör: pip install -r requirements.txt
# - Kopiera/byt namn på .env-example ==> .env
# - I .env, byt FLASK_RUN_PORT=8000 till din egen portnummer (se itslearning!)
# 
# STARTA APPEN:
# flask run


# ALTERNATIVT SÄTT: Uncommenta följande, ändra port, och kör direkt med python

#if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=8000, debug=True)
