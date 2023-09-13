import config
import mysql.connector
from geopy.distance import geodesic



def calculateDistance(port1, port2):
    search1 = f"SELECT latitude_deg, longitude_deg FROM airport"
    search1 += f" WHERE ident = '{port1}';"
    search2 = f"SELECT latitude_deg, longitude_deg FROM airport"
    search2 += f" WHERE ident = '{port2}';"
    kursori = yhteys.cursor()
    kursori.execute(search1)
    tulos1 = kursori.fetchall()
    kursori.execute(search2)
    tulos2 = kursori.fetchall()
    distance = geodesic(tulos1, tulos2).km
    return distance

yhteys = mysql.connector.connect(
    host='localhost',
    port='3306',
    database='flight_game',
    user= config.user,
    password=config.pwd,
    autocommit = True
)

print("Tämä ohjelma laskee kahden syöttämiesi lentoasemien etäisyyden.")
port1 = input("Syötä ensimmäinen lentoaseman ICAO-koodi:")
port2 = input("Syötä toisen lentoaseman ICAO-koodi:")
distance = int(calculateDistance(port1, port2))
print(f"Etäisyys näiden lentoasemien välillä on: {distance} kilometers")
