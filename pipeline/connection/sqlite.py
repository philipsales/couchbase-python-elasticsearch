import sqlite3

from settings import base_conf
import logs.logging_conf, logging
logger = logging.getLogger("sqlite.sqlite")

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def _create_table(conn):
    cursor = conn.cursor()
    try:
        query = ("CREATE TABLE IF NOT EXISTS "
            + base_conf.SQLITE_DATABASE_NAME
            + "(id INTEGER PRIMARY KEY, kobo_id TEXT, "
            + "cb_id TEXT, rev_id TEXT)")

        cursor.execute(query)
        
        conn.commit()
    except Exception as e:
        # Roll back any change if something goes wrong
        conn.rollback()
        raise e

def _insert_data(conn, kobo_id):
    cursor = conn.cursor()
    try:
        query = ("INSERT INTO " 
            + base_conf.SQLITE_DATABASE_NAME  
            + "(kobo_id, cb_id, rev_id) "
            + "VALUES(?,?,?)")

        values = (kobo_id, "", "")
        cursor.execute(query, values)

        logger.info("User inserted")
        conn.commit()
    except sqlite3.IntegrityError:
        logger.info('Record already exists')

def _get_data(conn,kobo_id):
    cursor = conn.cursor()
    query = ("SELECT kobo_id, cb_id, rev_id FROM "
        + base_conf.SQLITE_DATABASE_NAME  
        + " WHERE kobo_id=?")

    values = (kobo_id,)

    cursor.execute(query, values)
    user = cursor.fetchone()
    logger.info(user)

    return user

def _update_data(conn,cb_id, rev_id, kobo_id):
    cursor = conn.cursor()
    query = ("UPDATE "
        + base_conf.SQLITE_DATABASE_NAME
        + " SET cb_id=?, rev_id=? WHERE kobo_id=?")
    values = (cb_id, rev_id, kobo_id)
    cursor.execute(query,values)

    conn.commit()

def _close_db(conn):
    conn.close()