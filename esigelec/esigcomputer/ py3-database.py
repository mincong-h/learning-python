#!/usr/bin/env python


"""
Basic MySQL database operations

Documentation : 
Python MySQLdb
http://mysql-python.sourceforge.net/MySQLdb.html
"""


import MySQLdb
import timeit
import random as rd


__author__ = "Yifan DU"
__version__ = "1.0.0"
__email__ = "yifan.du.14@gmail.com"


def db_connect(host):
    """
    Create a database connection
    """
    try:
        print ("Connecting to host = " + host + "...")
        conn = MySQLdb.connect (host = host,
                                user = "root",
                                passwd = "root",
                                db = "infostats")
    except MySQLdb.Error as e:
        print ("Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit (1)
    print  ("Connected.")
    return conn


def db_close(conn):
    """
    Close database connection
    """
    conn.close()
    print ("Connection closed.")


def get_dataset(conn):
    """
    SELECT.
    Get existing data (trace) from table <trace>
    """
    sql = "SELECT id, timestamp, total_distance, volume FROM trace ORDER BY timestamp ASC;"
    cursor = conn.cursor()
    cursor.execute(sql)
    dataset = cursor.fetchall()
    return dataset


def insert_data(conn):
    """
    INSERT.
    Track trace with INSERT statement. Insert given trace into table <trace>.
    """
    cursor = conn.cursor()
    new_d = rd.random() * 50
    new_v = rd.random() * 30
    try:
        cursor.execute("""INSERT INTO trace (timestamp, total_distance, volume) VALUES
                (%s, %s, %s)""", (timeit.default_timer(), new_d, new_v))
        conn.commit()
        print ("Row inserted.")
    except:
        conn.rollback()


def display(dataset):
    """
    Display input dataset.
    """
    print ("\n------------------ display ------------------")
    print ("        id    timestamp    total_d     volume")
    for row in dataset:
        print ("%10.0f %12.0f %10.2f %10.2f" % (row[0], row[1], row[2], row[3]))
    print ("---------------------------------------------")
    

def run_select_exmpl(host):
    """
    Senario SELECT
    """
    try:
        conn = db_connect(host)
        dataset = get_dataset(conn)
        display(dataset)
        db_close(conn)
    except MySQLdb.Error as e:
        print ("Senario SELECT failed.")
        print ("Error %d: %s" % (e.args[0], e.args[1]))


def run_insert_exmpl(host):
    """
    Senario INSERT
    """
    try:
        conn = db_connect(host)
        insert_data(conn)
        db_close(conn)
    except MySQLdb.Error as e:
        print ("Senario INSERT failed.")
        print ("Error %d: %s" % (e.args[0], e.args[1]))


#main
host = "127.0.0.1"
# performance calculation
start = timeit.default_timer()
# statements
run_insert_exmpl(host)
run_select_exmpl(host)
# performance calculation
stop = timeit.default_timer()
print ("runtime: %10.3fms" % ((stop - start) * 1000 ))

