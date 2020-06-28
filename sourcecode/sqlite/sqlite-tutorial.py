# -*- coding: utf-8 -*-


import sqlite3


def connect(db_name: str):
    return sqlite3.connect(db_name)


def create_school_sql():
    return '''create table if not exists scores \
    ("id" integer primary key not null, "name" text not null, "math" integer not null)
    '''


if __name__ == '__main__':
    cnn = connect('school.db')

    cnn.execute(create_school_sql())
    cnn.commit()

    cnn.execute("insert into scores values ({}, '{}', {})".format(2, '林大胖', 98))
    cnn.commit()

    cursor = cnn.execute('select * from scores')
    scores_list = cursor.fetchall()
    if scores_list:
        for item in scores_list:
            print('{id} {name} {math}'.format(id=item[0], name=item[1], math=item[2]))

    cnn.close()
