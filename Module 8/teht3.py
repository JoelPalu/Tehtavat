import geopy.distance
import mysql.connector

connection = mysql.connector.connect(
    host ='127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = '',
    autocommit = True
)
def search_ICAO(input1, input2):
    sql_command = "SELECT airport.latitude_deg, airport.longitude_deg FROM airport WHERE ident ='" + input1 + "' OR ident = '" + input2 + "'"
    airport = ()
    cursor = connection.cursor()
    cursor.execute(sql_command)
    total = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in total:
            airport += row[0], row[1]
    return airport



while True:
    ICAO1,ICAO2= input("Anna ekan kentän ISCO: "), input("Anna tokan kentän ISCO: ")
    cordinates = search_ICAO(ICAO1,ICAO2)
    place1 = cordinates[0],cordinates[1]
    place2 = cordinates[2], cordinates[3]
    print(f"Lentokenttien etäisyys on: {geopy.distance.distance(place1,place2).km:1.2f}km")

