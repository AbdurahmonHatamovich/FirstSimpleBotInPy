import psycopg2 as db
class Database:
    @staticmethod
    def connect(query,query_type):
        database = db.connect(
            database = "n37",
            user = "postgres",
            host = "localhost",
            password = "abdu200400"
        )

        cursor = database.cursor()
        cursor.execute(query)
        data = ["insert","create"]
        if query_type == "insert":
            database.commit()
            if query_type == "insert":
                return "inserted"
            elif query_type == "create":
                return "created"

        else:
            return cursor.fetchall()

