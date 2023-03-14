import mysql.connector

connection = mysql.connector.connect(
    host ='127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'code',
    password = '',
    autocommit = True
)
def search_ICAO(input):
    sql_command = "SELECT airport.type, count(*) FROM airport WHERE iso_country ='" + input + "'GROUP BY type"
    cursor = connection.cursor()
    cursor.execute(sql_command)
    total = cursor.fetchall()
    if cursor.rowcount > 0:
        print(f"Lentokenttien kokonais määrä: {total[0]} Iso lentokenttä:  Keski lentokenttä Pieni lentokenttä HelipäditKiinni olevat ")

while True:
    search_ICAO(input("Anna maankoodi: "))
