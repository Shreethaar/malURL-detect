from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/capture_url',methods=['POST'])
def capture_url():
    data=request.get_json()
    url=data.get('url')
    # URL goes to database
    return jsonify({"status":"success"}),200

if __name__ == '__main__':
    app.run(debug=True)

