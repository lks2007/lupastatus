import requests
import sqlite3
from datetime import datetime
import time


def incident(path, platform):
    con = sqlite3.connect('/var/www/lupastatus/db.sqlite3')
    cur = con.cursor()

    global r

    try:
        r = requests.get("https://www.lupa.com"+path, verify=False)

        elapse = r.elapsed
        date = datetime.strptime(str(elapse), "%H:%M:%S.%f")
        
        mc = int(date.microsecond)
        ms = mc / 1000

        if r.status_code == 502 or r.status_code == 503:
            cur.execute("INSERT INTO app_incident(name, type, platform, latency, hour) VALUES ('Web Server down', 2, '"+platform+"', '"+str(ms)+"', '"+str(datetime.now())+"')")
        else:
            if ms > 1000:
                cur.execute("INSERT INTO app_incident(name, type, platform, latency, hour) VALUES ('Latency', 1, '"+platform+"', , '"+str(ms)+"', '"+str(datetime.now())+"')")
            else:
                cur.execute("INSERT INTO app_incident(name, type, platform, latency, hour) VALUES ('No Problem', 0, '"+platform+"', '"+str(ms)+"', '"+str(datetime.now())+"')")
    except requests.ConnectionError:
        cur.execute("INSERT INTO app_incident(name, type, platform, latency, hour) VALUES ('DNS down', 3, '"+platform+"', '1000', '"+str(datetime.now())+"')")
    
    con.commit()

def main():
    while True:
        incident('/', 'Lupa')
        incident('/api/', 'Api')
        time.sleep(3600)

if __name__ == "__main__":
    main()