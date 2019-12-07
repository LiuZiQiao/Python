# import pymysql


# conn = pymysql.connect(host='localhost',user='root',passwd='123456',port='3306',db='movies')

# print(conn)
# def connectdb():
#     print('连接到mysql服务器...')
#     db = pymysql.connect(
#         host="localhost",
#         user="root",
#         passwd="123456",
#         port=3306,
#         db="movies",
#         charset='utf8',
#         cursorclass=pymysql.cursors.DictCursor)
#     print('连接上了!')



#     if __name__ == "__main__":
#         connectdb()



#!/usr/bin/python3
 
# import pymysql
 
# # 打开数据库连接
# db = pymysql.connect("localhost","root","123456","movies" )
 
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
 
# # 使用 execute()  方法执行 SQL 查询 
# cursor.execute("SELECT VERSION()")
 
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
 
# print ("Database version : %s " % data)
 
# # 关闭数据库连接
# db.close()


USERID = 1000+int('1')
print(USERID)