import pymysql


connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="pokemones",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

if connection.open:
    print("the connection is opened")

def insert_data(table, query):
    try:
        with connection.cursor() as corsur:
            insert_query = "INSERT into " + table + " values" + query
            print(insert_query)
            corsur.execute(insert_query)
            connection.commit()
    except:
        print("error")

def query_data(query):
    result = {}
    try:
        with connection.cursor() as corsur:
            corsur.execute(query)
            result = corsur.fetchall()
    except:
        print("error")
    return result
