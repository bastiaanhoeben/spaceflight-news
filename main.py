from connection import Connection
from table import Table
from retrieval import Retrieval
from parse import Parse

def update_database():

    # open connection and obtain cursor
    connection = Connection()
    conn_instance = connection.connect()
    conn = conn_instance[0]
    cur = conn_instance[1]

    # print connection confirmation message
    print(f"Connecting to database with the following parameters:\n"
          f"Host: {connection.host}, Database: {connection.dbname}, "
          f"User: {connection.user}")

    # create table if no same exists
    table = Table('newsfeed')
    table.create_table(conn, cur)

    # extract latest articles from Spaceflight News in json file
    number_of_articles = input("How many latests articles would you like to "
                        "retrieve? ")
    url = 'https://spaceflightnewsapi.net/api/v2/articles'
    retrieval_order = Retrieval(url)
    data = retrieval_order.retrieve_json(number_of_articles)

    # parse json file and write new articles to database
    write = Parse(data)
    write.parsing_json(conn, cur, table.tbname)

    # close cursor and connection
    connection.close_conn(conn, cur)


if __name__ == '__main__':
    update_database()

