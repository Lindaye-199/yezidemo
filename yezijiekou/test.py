import pymysql
db=pymysql.connect(host='47.100.228.152',
                    port=3306,
                    user='yexiaojing',
                    password='ins_test123',
                    db='yibaodb-test')
cur=db.cursor()
cur.execute("select Name from yibaodb-test")
data=cur.fetchall()
print(data)
db.close()