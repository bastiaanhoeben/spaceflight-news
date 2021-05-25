import connection
from table import Table
from retrieval import Retrieval
from parse import Parse


# define connection parameters
connection = connection.Connection("127.0.0.1", "spaceflightnews", "postgres",
                         "password")

# open connection and obtain cursor
conn_instance = connection.connect()
conn = conn_instance[0]
cur = conn_instance[1]

# create table if no same exists
table = Table('newsfeed')
table.drop_table(conn, cur)
table.create_table(conn, cur)

# extract latest articles from Spaceflight News in json file
url = 'https://spaceflightnewsapi.net/api/v2/articles'
retrieval_order = Retrieval(url)
data = retrieval_order.retrieve_json(20)

# parse json file and write new articles to database
write = Parse(data)
write.parsing_json(conn, cur, table.tbname)

# close cursor and connection
connection.close_conn(conn, cur)
