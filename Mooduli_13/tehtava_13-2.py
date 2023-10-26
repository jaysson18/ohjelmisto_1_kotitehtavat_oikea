import json
from flask import Flask, request

app = Flask(__name__)

# tietokanta
lentokentat = {
    "EFHK": {"Name": "Helsinki Vantaa Airport", "Municipality": "Helsinki"},
    "EGLL": {"Name": "Heathrow Airport", "Municipality": "London"},
    "KJFK": {"Name": "John F. Kennedy International Airport", "Municipality": "New York"},
}

@app.route('/kenttä/<icao>', methods=['GET'])
def hae_lentokentta(icao):
    if icao in lentokentat:
        lentokentta_tiedot = {
            "ICAO": icao,
            "Name": lentokentat[icao]["Name"],
            "Municipality": lentokentat[icao]["Municipality"]
        }
        return json.dumps(lentokentta_tiedot)
    else:
        return "Lentokenttää ei löydy", 404

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)

    #muista laitta url kenttään tämä url: http://127.0.0.1:3000/kenttä/EFHK jotta helsinki näkyy ja vaihda icao koodi muihin
