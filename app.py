from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.route('/setcookies', methods=['POST'])
def set_cookies():
    cookie_value = request.json.get('cookie_data', 'default_value')
    response = make_response(jsonify({"message": "Cookie set"}))
    response.set_cookie('my_cookie', cookie_value)
    return response

@app.route('/getcookies', methods=['GET'])
def get_cookies():
    cookie_value = request.cookies.get('my_cookie', 'No cookie set')
    return jsonify({"my_cookie": cookie_value})

if __name__ == '__main__':
    app.run(debug=True)