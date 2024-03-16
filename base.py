import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("Order.db")
        self.cursor = self.connection.cursor()
        self.create_table()
        self.create_kfc_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE if NOT EXISTS user (
                id INTEGER PRIMARY KEY ,
                username VARCHAR UNIQUE NOT NULL,
                password VARCHAR NOT NULL ,
                email VARCHAR NOT NULL ,
                age INTEGER ,
                phone_number VARCHAR NOT NULL 
                )
        """)


    def create_kfc_table(self):
        self.cursor.execute("""
            create table if not exists foods (
                food integer primary key ,
                fast_food_name varchar not null ,
                price integer not null ,
                how_much varchar not null ,
                total integer not null ) 
        """)

    def insert_user(self, username, password, email, age, phone_number):
        self.cursor.execute(
            "insert into user (username, password, email, age, phone_number) values (?, ?, ?, ?, ?)",
            (username, password, email, age, phone_number))
        self.connection.commit()

    def login_user(self, username, password):
        user = self.cursor.execute("select * from user where username=? and password=?",
                                   (username, password)).fetchone()
        return user

    def insert_food(self, fast_food_name, price, how_much, total):
        self.cursor.execute(
            "insert into foods (fast_food_name, price, how_much, total) values (?, ?, ?, ?)",
            (fast_food_name, price, how_much, total))
        self.connection.commit()

    def read_all_user(self):
        users = self.cursor.execute("select * from user where -1 ").fetchall()
        return users

    def delete_user(self, id):
        self.cursor.execute("delete from user where id=?", (id,))
        self.connection.commit()
