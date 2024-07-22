#!/usr/bin/env python3

import sqlite3

def check_table_exists(db_name, table_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';")
    result = cursor.fetchone()
    conn.close()
    return result is not None

if __name__ == '__main__':
    db_name = 'students.db'
    table_name = 'students'
    if check_table_exists(db_name, table_name):
        print(f"Table '{table_name}' exists in database '{db_name}'.")
    else:
        print(f"Table '{table_name}' does not exist in database '{db_name}'.")