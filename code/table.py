from psycopg2 import sql


class Table:
    """Class for handling SQL tables"""
    def __init__(self, tbname):
        self.tbname = tbname

    def __str__(self):
        return f"Create table with name{self.tbname}."

    def create_table(self, conn, cur):
        """Takes database connection and cursor as input and creates table in database"""
        cur.execute(sql.SQL("CREATE TABLE IF NOT EXISTS {} "
                            "(article_id TEXT UNIQUE, article_url TEXT, "
                            "article_pubdate TIMESTAMPTZ, article_summary TEXT)")
                    .format(sql.Identifier(self.tbname)))
        conn.commit()

    def drop_table(self, conn, cur):
        """Takes database connection and cursor as input and drops table in database"""
        cur.execute(sql.SQL("DROP TABLE IF EXISTS {}")
                    .format(sql.Identifier(self.tbname)))
        conn.commit()