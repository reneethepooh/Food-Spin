import MySQLdb as dbapi
import sys
import csv

db="foodspin"
user="food"
password="food"
host="localhost"

QUERY='SELECT * FROM mydb.people;'

QUERY='SELECT * FROM '+
db=dbapi.connect(host='localhost',user='root',passwd='password')

cur=db.cursor()
cur.execute(QUERY)
result=cur.fetchall()

c = csv.writer(open('dbdump01.csv', 'wb'))
for x in result:
    c.writerow(x)