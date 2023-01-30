import mysql.connector

connection = mysql.connector.connect(
    host ='127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = '',
    autocommit = True
)
def search_ICAO(input):
    small = 0
    medium = 0
    large = 0
    heli = 0
    closed = 0


    sql_command = "SELECT airport.type FROM airport WHERE iso_country ='" + input + "'"
    cursor = connection.cursor()
    cursor.execute(sql_command)
    total = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in total:
            if "small_airport" == row[0]:
                small += 1
            elif "medium_airport" == row[0]:
                medium += 1
            elif "large_airport" == row[0]:
                large += 1
            elif "heliport" == row[0]:
                heli += 1
            else:
                closed +=1
        print(f"Lentokenttien kokonais määrä: {small+medium+large+heli+closed} Iso lentokenttä: {large}  Keski lentokenttä {medium}  Pieni lentokenttä {small}  Helipädit {heli}  Kiinni olevat {closed}")

while True:
    search_ICAO(input("Anna maankoodi: "))
