import sqlite3

def create_dept():
    connect = sqlite3.connect('sqlite.db')
    cursor = connect.cursor()

    cursor.execute('''
        create table if not exists dept (
            deptno integer primary key,
            dname text not null,
            loc text
        )
    ''')

    connect.commit()
    connect.close()

def insert_dept():
    connect = sqlite3.connect('sqlite.db')
    cursor = connect.cursor()

    cursor.execute('''
        insert into dept (deptno, dname, loc)
        values (?, ?, ?)
    ''', (10, '1강의실', '천안'))

    cursor.execute('''
        insert into dept (deptno, dname, loc)
        values (?, ?, ?)
    ''', (20, '2강의실', '수원'))

    cursor.execute('''
        insert into dept (deptno, dname, loc)
        values (?, ?, ?)
    ''', (30, '3강의실', '서울'))

    print('수정 개수:', cursor.rowcount)

    connect.commit()
    connect.close()

def select_dept():
    connect = sqlite3.connect('sqlite.db')
    cursor = connect.cursor()

    cursor.execute('''
        select deptno, dname, loc
        from dept
    ''')

    rows = cursor.fetchall()
    print('fetchall 결과')
    print(rows)

    connect.close()

def select_dept_20():
    connect = sqlite3.connect('sqlite.db')
    cursor = connect.cursor()

    cursor.execute('''
        select deptno, dname, loc
        from dept
        where deptno = ?
    ''', (20,))

    rows = cursor.fetchone()
    print('fetchone 결과')
    print(rows)

    connect.close()

def select_dict():
    connect = sqlite3.connect('sqlite.db')
    connect.row_factory = sqlite3.Row
    cursor = connect.cursor()

    cursor.execute('''
        select deptno, dname, loc
        from dept
        where deptno = ?
    ''', (20,))

    rows = cursor.fetchone()
    print('fetchone 결과')
    print(rows)
    connect.close()

def select_all_dict():
    connect = sqlite3.connect('sqlite.db')
    connect.row_factory = sqlite3.Row
    cursor = connect.cursor()

    cursor.execute('''
        select deptno, dname, loc
        from dept
    ''')

    rows = cursor.fetchall()
    print('fetchall 결과')
    print(rows)

    result = []
    for row in rows:
        result.append(dict(row))
    print(result)

    result2 = [dict(row) for row in rows]
    print(result2)

    connect.close()

from pydantic import BaseModel
# class DeptDTO(BaseModel):
# class DeptSchema(BaseModel):
class DeptModel(BaseModel):
    deptno: int
    dname: str
    loc: str

# create_dept()
# insert_dept()
# select_dept()
# select_dept_20()
# select_dict()
# select_all_dict()
# select_all_class()