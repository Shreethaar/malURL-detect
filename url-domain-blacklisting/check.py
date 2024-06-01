import psycopg2

def is_url_blacklisted(url):
    domain = url.split('/')[2]
    conn = psycopg2.connect("dbname=blacklist_db user=trevorphilips password=*")
    cur = conn.cursor()
    cur.execute("SELECT * FROM blacklisted_urls WHERE url = %s OR domain = %s", (url, domain))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result is not None

url = "http://example.com/malicious-path"
if is_url_blacklisted(url):
    print("Warning: The URL is flagged as suspicious.")
else:
    print("The URL is safe to access.")

