import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode


def convertToBinaryData(filename):
    #Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


def insertdata(id, name, dt, image):
    print("Inserting Data")

    try:
        connection = mysql.connector.connect(host='localhost',
                             database ='suraj',
                             user ='root',
                             password ='root')

        cursor = connection.cursor(prepared=True)

        sql_insert_blob_query = """ INSERT INTO `test`
                          (`id`, `name`, `dt`, `image`) VALUES (%s,%s,%s,%s)"""

        empPicture = convertToBinaryData(image)


        # Convert data into tuple format
        insert_blob_tuple = (id, name, dt, empPicture)

        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into python_employee table", result)

    except mysql.connector.Error as error:
        connection.rollback()
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


#insertBLOB(78999, "ghkll", "2019-02-09 17:28:32", "C:\\Users\My Lappy\Pictures\Jim.jpg")
