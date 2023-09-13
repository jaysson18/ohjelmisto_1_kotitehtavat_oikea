import mysql.connector
import config

small_airports = []
medium_airports = []
large_airports = []
heliports = []

def search_airports(country_code):
    sql ="SELECT type FROM airport"
    sql +="WHERE iso_country=""+ country_code+"""
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if tulos is not None:
        for row in tulos:
            airport_type = row[0]
            if airport_type == "small_airport":
                small_airports.append(airport_type)
            if airport_type == "medium_airport":
                medium_airports.append(airport_type)
            if airport_type == "large_airport":
                large_airports.append(airport_type)
            if airport_type == "heliport":
                heliports.append(airport_type)

    else:
        print("Ei tuloksia annetulla koodilla.")
        print(f"Maassa on: {len(small_airports)} pientä lentokenttää \n{len(medium_airports)} keskikokoista lentokenttää \n{len(large_airports)} isoa lentokenttää \n{len(heliports)} helikopterikenttää")

        yhteys = mysql.connector.connect(
            host='localhost',
            port='3306',
            database='flight_game',
            user= config.user,
            password=config.pwd,
            autocommit=True
        )

        country_code_glb = input("Syötä etsimäsi maan maakoodi (FI/EN/SWE/etc.):")
        search_airports(country_code_glb)