from flask import Flask, jsonify
import mysql.connector
import config

app = Flask(__name__)
yhteys = mysql.connector.connect(
    host= '127.0.0.1',
    port= '3306',
    database= 'flight_game',
    user= config.user,
    password= config.pwd,
    autocommit= True
)


def hae_lentokenttätiedot(icao):
    sql = "SELECT ident, name, municipality FROM Airport WHERE ident = %s"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, (icao,))
    tulos = kursori.fetchone()
    kursori.close()
    return tulos


@app.route('/kenttä/<string:icao>', methods=['GET'])
def get_airport(icao):
    data = hae_lentokenttätiedot(icao)
    if data:
        vastaus = {
            "ICAO": data["ident"],
            "Name": data["name"],
            "Municipality":data["municipality"]
        }
        return jsonify(vastaus)
    else:
        return jsonify({"error"}), 404

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)