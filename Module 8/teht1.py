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
    sql_command = "SELECT airport.ident, airport.name, country.name FROM airport, country " \
          "WHERE ident ='" + input + "' AND airport.iso_country = country.iso_country"
    cursor = connection.cursor()
    cursor.execute(sql_command)
    total = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in total:
            print(f"ICAO: {row[0]} \
            Airport name: {row[1]} \
            Country: {row[2]}")

while True:
    search_ICAO(input("Anna ICAO-koodi: "))
