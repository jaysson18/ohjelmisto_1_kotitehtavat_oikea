import mysql.connector
import config

def hae_kentta_icao_koodilla(icao):
    sql = f'SELECT name, municipality FROM airport WHERE ident="{icao}"'
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos


yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    user= config.user,
    password=config.pwd,
    database='flight_game',
    autocommit=True
)

icao = input("Anna kentän ICAO-koodi:")
kenttä = hae_kentta_icao_koodilla(icao)
print(kenttä)
print(f'Kentän nimi: {kenttä[0][0]}, sijainti kunnassa {kenttä[0][1]}')