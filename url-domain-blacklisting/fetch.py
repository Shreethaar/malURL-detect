import requests
import psycopg2

def fetch_phishtank_data():
    url = "https://data.phishtank.com/data/online-valid.csv"
    response = requests.get(url)
    data = response.content.decode('utf-8')
    return data.splitlines()

def update_database(data):
    conn = psycopg2.connect("dbname=blacklist_db user=trevorphilips password=*")
    cur = conn.cursor()
    for line in data:
        fields = line.split(',')
        url = fields[1]
        domain = url.split('/')[2]
        reason = 'PhishTank'
        try:
            cur.execute("""
                INSERT INTO blacklisted_urls (url, domain, reason)
                VALUES (%s, %s, %s)
                ON CONFLICT (url) DO NOTHING
            """, (url, domain, reason))
        except Exception as e:
            print(f"Error inserting data: {e}")
    conn.commit()
    cur.close()
    conn.close()

data = fetch_phishtank_data()
update_database(data)

