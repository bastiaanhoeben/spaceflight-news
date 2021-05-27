from psycopg2 import sql


class Parse:

    def __init__(self, file):
        self.file = file

    def parsing_json(self, conn, cur, tbname):
        countold = 0
        countnew = 0
        for article in self.file:
            article_id = article['id']
            article_url = article['url']
            article_pubdate = article['publishedAt']
            article_summary = article['summary']

            # try reading database for existing articles,
            # otherwise write new entry in database
            try:
                cur.execute(sql.SQL("SELECT article_url FROM {} "
                                    "WHERE article_id = %s LIMIT 1")
                            .format(sql.Identifier(tbname)), (article_id,))
                # next assignment fails in case of missing entry
                primary_key = cur.fetchone()[0]
                countold = countold + 1
            except:
                cur.execute(sql.SQL("INSERT INTO {} (article_id, article_url, "
                                    "article_pubdate, article_summary) "
                                    "VALUES (%s, %s, %s, %s)")
                            .format(sql.Identifier(tbname)),
                            (article_id, article_url, article_pubdate, article_summary))
                conn.commit()
                countnew = countnew + 1

        print(f"\n{countnew} newly added articles")
        print(f"{countold} old articles skipped")