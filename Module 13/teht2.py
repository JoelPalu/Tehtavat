from flask import Flask, jsonify
import mysql.connector

connection = mysql.connector.connect(
        host='26.83.105.196',
        port=3307,
        database='peli_projekti',
        user='code',
        password='1',
        autocommit=True
    )

app = Flask(__name__)
@app.route('/port/<ICAO>')
def search_ICAO(ICAO):
    sql_command = "SELECT airport.ident, airport.name, airport.municipality FROM airport WHERE ident ='" + ICAO + "'"
    cursor = connection.cursor()
    cursor.execute(sql_command)
    total = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in total:
            yep = {'ICAO': row[0], 'Airport name': row[1], 'Municipality': row[2]}
            return jsonify(yep)






if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)