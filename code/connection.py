import psycopg2


class Connection:
    """Class for handling database connections"""
    def __init__(self, host="postgres", dbname="spaceflightnews",
                 user="postgres", password="password"):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password

    def __str__(self):
        return f"Create connection instance with {self.dbname}" \
               f" on host IP {self.host}."

    def connect(self):
        """Connects to a database, returns connection and cursor"""
        conn_pars = f"host = {self.host} dbname = {self.dbname}" \
                    f" user = {self.user} password = {self.password}"
        # alternative notation: conn_pars = "user:pass@ip:port/database"
        conn = psycopg2.connect(conn_pars)
        cur = conn.cursor()
        return [conn, cur]

    def close_conn(self, conn, cur):
        """Takes database connection and cursor, closes database connection"""
        cur.close()
        conn.close()
        return f"Connection to {self.dbname} closed"
