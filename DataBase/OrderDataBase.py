class OrderDataBase:

    db_connect = create_engine('sqlite:///itn.db')

    def __init__(self):
        self.conn = db_connect.connect()  # connect to database

    def get_all_orders(self):
        query = self.conn.execute("select * from orders")
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return result