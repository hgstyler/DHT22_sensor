# pip install psycopg2
import psycopg2

# connect db
# conn = psycopg2.connect("host=localhost dbname=test user=postgres password=pwtest port=5432")
conn = psycopg2.connect(host='localhost', dbname='test1', user='postgres', password='sork1emd', port='5432')

# create cursor before a execution
#cur = conn.cursur()

# execution: create a table
#cur.execute("CREATE TABLE test_table (title varchar, content text);") 

# execution: input data
#cur.execute("INSERT INTO test_table (title, content) VALUES (%s, %s)", ('hello' ,'qwerttyfdas'))

# example 1
#cur.execute("INSERT INTO numbers VALUES (%d)", (42,)) # WRONG
#cur.execute("INSERT INTO numbers VALUES (%s)", (42,)) # correct

# example 2
#cur.execute("INSERT INTO foo VALUES (%s)", "bar")    # WRONG
#cur.execute("INSERT INTO foo VALUES (%s)", ("bar"))  # WRONG
#cur.execute("INSERT INTO foo VALUES (%s)", ("bar",)) # correct
#cur.execute("INSERT INTO foo VALUES (%s)", ["bar"])  # correct

# exampel 3
#SQL = "INSERT INTO authors (name) VALUES (%s);" # Note: no quotes
#data = ("O'Reilly", )
#cur.execute(SQL, data) # Note: no % operator

# test ���̺��� ��� �����͸� �������� ����Ѵ�
#cur.execute("SELECT * FROM test;")
#print(cur.fetchone())

# �����͸� �����ߴٸ� �ݵ�� .commit() ���־�� �Ѵ�
#conn.commit()

# Ŀ���� �ݰ� ������ �����Ѵ�.
#cur.close()
#conn.close()
