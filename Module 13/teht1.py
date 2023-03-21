from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/al/<int:e>')
def alkuluku(e):

    total = 0
    for n in range(1, e):
        if e % n == 0:
            total = total + 1

    if total <= 1:
        return jsonify({"Num" : e, "prime" : True })
    else:
        return jsonify({"Num" : e, "prime": False })






if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)