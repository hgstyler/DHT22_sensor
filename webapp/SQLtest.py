# pip install psycopg2
import psycopg2

try:
    # connect db
    # conn = psycopg2.connect("host=localhost dbname=test1 user=postgres password=pwtest port=5432")
    conn = psycopg2.connect(dbname='test1', user='postgres', password='sork1emd', host='localhost', port=5432)

    # create cursor before a execution
    cur = conn.cursor()

    # execution: create a table
    cur.execute("CREATE TABLE test_room (date, time, temp INTEGER(2), humid INTEGER(2));") 

    # execution: input data
    cur.execute("INSERT INTO test_room (date, time, temp, humid) VALUES ('07-06-2022' ,'15:40:58', 28, 45);")

    # example 1
    # cur.execute("INSERT INTO numbers VALUES (%d)", (42,)) # WRONG
    #cur.execute("INSERT INTO numbers VALUES (%s)", (42,)) # correct

    # example 2
    # cur.execute("INSERT INTO foo VALUES (%s)", "bar")    # WRONG
    # cur.execute("INSERT INTO foo VALUES (%s)", ("bar"))  # WRONG
    #cur.execute("INSERT INTO foo VALUES (%s)", ("bar",)) # correct
    #cur.execute("INSERT INTO foo VALUES (%s)", ["bar"])  # correct

    # exampel 3
    #SQL = "INSERT INTO authors (name) VALUES (%s);" # Note: no quotes
    #data = ("O'Reilly", )
    #cur.execute(SQL, data) # Note: no % operator

    # test 테이블의 모든 데이터를 가져오고 출력한다
    cur.execute("SELECT * FROM test_room;")
    print(cur.fetchone())

    # 데이터를 변경했다면 반드시 .commit() 해주어야 한다
    conn.commit()

    # 커서를 닫고 연걸을 종료한다.
    cur.close()
    conn.close()

except Exception as e:
    print('postgresql database connection error!')
    print(e)

finally:
    if conn:
        conn.close()

'''
try:
    # connect db
    # # conn = psycopg2.connect("host=localhost dbname=test1 user=postgres password=pwtest port=5432")
    conn = psycopg2.connect(dbname='postgres', user='postgres', password='sork1emd', host='localhost', port=5432)

    # create cursor before a execution
    cur = conn.cursor()

    cur.execute("create database testdb")  # superuser 만 create database  명령어 가능
    cur.execute('SELECT version()')
    ver = cur.fetchone()

except Exception as e:
    print('postgresql database connection error!')
    print(e)

else:
    print(ver)

finally:
    if conn:
        conn.close()


try:
    conn = psycopg2.connect(dbname='testdb', user='postgres', password='sork1emd', host='localhost', port=5432)
    cur = conn.cursor()

    cur.execute("CREATE TABLE Cars(Id INTEGER PRIMARY KEY, Name VARCHAR(20), Price INT)")

    cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
    cur.execute("INSERT INTO Cars VALUES(2,'Mercedes',57127)")

    cur.execute("SELECT * FROM Cars")
    rows = cur.fetchall()
    conn.commit()

except Exception as e:
    print('postgresql database connection error!')
    print(e)

    if conn:
        conn.rollback()

else:
    print(rows)

finally:
    if conn:
        conn.close()
'''