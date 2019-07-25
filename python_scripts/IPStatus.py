import psycopg2
from  subprocess import Popen , PIPE
iplists = []
try:
    connection=psycopg2.connect(user="postgres",password="node",host="localhost",port="5432",database="test")
    cursor = connection.cursor()
    fetch_all = "select * from iplists";
    cursor.execute(fetch_all)
    all_records = cursor.fetchall()

    for row in all_records:
        iplists.append(row[2])

    for ip in iplists:
        #print (ip)
        ip = str(ip)
        hostup = Popen(["ping","-c3",ip],stdout=PIPE)
        result = hostup.communicate()[0]
        ret_code= hostup.returncode

        if ret_code == 0:
            print (ip,"UP")
        else:
            print(ip,"DOWN")
except (Exception,psycopg2.Error) as Error:
    print(Error)