import mysql.connector


class Curd:
    def __init__(self):
        self.connection = mysql.connector.connect(host='localhost', user='root', password='EncourageStudy1@',
                                                  database='makeup_store')
        self.cursor = self.connection.cursor()

    def add_data(self, query, values):
        self.connection = mysql.connector.connect(host='localhost', user='root', password='EncourageStudy1@',
                                                  database='makeup_store')
        self.cursor = self.connection.cursor()
        self.cursor.execute(query, values)
        self.connection.commit()
        # self.fetch_data()

    def fetch_data(self, query):
        self.connection = mysql.connector.connect(host='localhost', user='root', password='EncourageStudy1@',
                                                  database='makeup_store')
        self.cursor = self.connection.cursor()
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        return self.rows

    def update_data(self, query, values):
        self.connection = mysql.connector.connect(host='localhost', user='root', password='EncourageStudy1@',
                                                  database='makeup_store')
        self.cursor = self.connection.cursor()
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_data(self, query, values):
        self.connection = mysql.connector.connect(host='localhost', user='root', password='EncourageStudy1@',
                                                  database='makeup_store')
        self.cursor = self.connection.cursor()
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_data_issue(self, query, values):
        self.connection = mysql.connector.connect(host='localhost', user='root', password='EncourageStudy1@',
                                                  database='makeup_store')
        self.cursor = self.connection.cursor()
        self.cursor.execute(query, values)
        self.connection.commit()

