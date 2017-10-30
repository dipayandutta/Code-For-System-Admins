import pyodbc
import pymssql
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=127.0.0.1;"
                      "Database=College_2014_15_DB;"
                      "Trusted_Connection=yes;")
cursor = cnxn.cursor()
'''
if cnxn:
    print "Connected"
else:
    print "Not Connected"


print cursor
'''
tablesquery='SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES'
query=cursor.execute(tablesquery)
columns = [column[0] for column in cursor.description]
results = []
for row in query.fetchall():
    #results.append(dict(zip(columns,row)))
    results.append(row)

for table_name in results:
    print "============="
    print "table name"
    print "============="
    print table_name[0]
    print "============="
    print "Columns"
    print "--------------"
    for row in cursor.columns(table=table_name[0]):
        print row.column_name
