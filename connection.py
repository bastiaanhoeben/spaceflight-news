import psycopg2


class Connection:

    def __init__(self, host="127.0.0.1", dbname="spaceflightnews",
                 user="postgres", password="password"):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password

    def __str__(self):
        return f"Create connection instance with {self.dbname}" \
               f" on host IP {self.host}."

    def connect(self):
        conn_pars = f"host = {self.host} dbname = {self.dbname}" \
                    f" user = {self.user} password = {self.password}"
        # alternative notation: conn_pars = "user:pass@ip:port/database"
        conn = psycopg2.connect(conn_pars)
        cur = conn.cursor()
        return [conn, cur]

    def close_conn(self, conn, cur):
        cur.close()
        conn.close()
        return f"Connection to {self.dbname} closed"
