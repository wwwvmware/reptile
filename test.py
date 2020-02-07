import pymysql
conn =pymysql.connect(
    host ='127.0.0.1',
    port = 3306,
    user = 'root',
    password ='123456',
    database ='lr_project',
    charset ='utf8'
)
cursor =conn.cursor()  
sql ='insert into userinfo (user,pwd) values (%s,%s);'
 
name = 'wuli'
pwd = '123456789'
cursor.execute(sql, [name, pwd])
conn.commit()
cursor.close()
conn.close()
