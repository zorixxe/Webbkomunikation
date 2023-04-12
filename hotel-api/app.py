from flask import Flask, request, jsonify
from flask_cors import CORS 


app = Flask(__name__)
CORS(app) # Tillåt cross-origin requests

rooms_list = [
    {"number": 101, "type": "single", "price": 1000},
    {"number": 102, "type": "double", "price": 2000},
    {"number": 103, "type": "single", "price": 1000},
    {"number": 104, "type": "double", "price": 2000},
    {"number": 105, "type": "single", "price": 1000}
]

@app.route("/")
def index():
    return "Use endpoints /rooms or /bookings"

@app.route("/rooms")
def rooms():
    return {
        "rooms": rooms_list,
        "room_count": len(rooms_list)
    }

@app.route("/rooms/<int:id>")
def ru(id):
    try:
        return rooms_list[id]
    except:
        return "No room with that id"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8442, debug=True)


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
