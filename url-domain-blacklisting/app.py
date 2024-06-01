from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

def is_url_blacklisted(url):
    domain = url.split('/')[2]
    conn = psycopg2.connect("dbname=blacklist_db user=trevorphilips password=*")
    cur = conn.cursor()
    cur.execute("SELECT * FROM blacklisted_urls WHERE url = %s OR domain = %s", (url, domain))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result is not None

@app.route('/check-url', methods=['POST'])
def check_url():
    data = request.get_json()
    url = data['url']
    if is_url_blacklisted(url):
        return jsonify({"message": "Warning: The URL is flagged as suspicious."})
    else:
        return jsonify({"message": "The URL is safe to access."})

if __name__ == '__main__':
    app.run(debug=True)

