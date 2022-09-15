import mysql.connector
from mysql.connector import Error
import CTC_Training

def connect_db():
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='sakila',
                                            user='root',
                                            password='xxxxxx')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
        return connection, cursor


    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            print("MySQL connection is closed")


def create_table(connection, curr):
    try:
        table="""CREATE TABLE Applicant ( 
                             applicant_Id int,
                             first_name varchar(25) NOT NULL,
                             last_name varchar(25) NOT NULL,
                             phone_number varchar(10) NOT NULL,
                             city varchar(20) NOT NULL,
                             salary int NOT NULL,
                             department varchar (20));"""
        curr.execute(table)
    except Error as e:
        print("ERROR| Error occured during creation of table", e)
    finally:
        print("Table has created Sucessfully")
        connection.commit()

def insert_value(connection, curr, lst):
    try:
        
        mySql_insert_query = f"INSERT INTO Applicant (applicant_id, first_name, last_name,phone_number, city, salary, department) VALUES(null, '{lst[0]}', '{lst[1]}', '{lst[2]}', '{lst[3]}','{lst[4]}','{lst[5]}');"
        curr.execute(mySql_insert_query)
        connection.commit()
        print(curr.rowcount, "Record inserted successfully into Applicant table")

    except mysql.connector.Error as error:
        print("Failed to insert record into Applicant table {}".format(error))

    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

conn, curr=connect_db()

create_table(conn, curr)
Applicant=CTC_Training.registration()
insert_value(conn, curr, Applicant)




    

