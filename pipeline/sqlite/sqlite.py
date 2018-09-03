import sqlite3

import logs.logging_conf, logging
logger = logging.getLogger("sqlite.sqlite")

db = sqlite3.connect('data/kobodb')
cursor = db.cursor()

def _create_table():
    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS
                        kobo(id INTEGER PRIMARY KEY, kobo_id TEXT, cb_id TEXT, rev_id TEXT)''')
        db.commit()
    except Exception as e:
        # Roll back any change if something goes wrong
        db.rollback()
        raise e
    finally:
        # Close the db connection
        db.close()

def _insert_data(kobo_id, cb_id, rev_id):
    try:
        cursor.execute('''INSERT INTO kobo(kobo_id, cb_id, rev_id)
                        VALUES(?,?,?)''', (kobo_id, cb_id, rev_id))

        logger.info("First user inserted")
        db.commit()
    except sqlite3.IntegrityError:
        logger.info('Record already exists')
    finally:
        db.close()

def _get_data(kobo_id):
    cursor.execute('''SELECT kobo_id, cb_id, rev_id FROM kobo WHERE id=?''', (kobo_id))
    user = cursor.fetchone()
    logger.info(user)
    db.close()

    return user

def _update_data(cb_id, rev_id, kobo_id):
    cursor.execute('''UPDATE kobo SET cb_id = ?, rev_id = ? WHERE id = ? ''',
    (cb_id, cb_id, kobo_id))

    db.commit()