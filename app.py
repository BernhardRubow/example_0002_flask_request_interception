from flask import Flask, request, abort, jsonify

app = Flask(__name__)

@app.before_request
def check_token():
    try:
        payload = request.get_json()
        if "token" not in payload:
            abort(401)
        if payload["token"] != '1234567':
            abort(401)
        return None
    except:
        abort(401)


@app.route("/login", methods=["POST"])
def login():
    if request.method == 'POST':
        print("Request login received")
        payload = request.get_json()
        if(payload['user'] == 'brubow' and payload['password']=='test1234!'):
            return '12345657'
        abort(401)


@app.route("/api", methods=["POST"])
def handle_request():
    payload = { 
        "data": "the data",
        "request": request.get_json()
    }
    return jsonify(payload)
    

if __name__ == "__main__":
    app.run("0.0.0.0", port=5001)
