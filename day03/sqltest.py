import sys
import pymysql
import csv
import codecs


def get_conn():
    conn = pymysql.connect("localhost","root","123456","movies")
    # conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456.', db='movies', charset='utf8')
    print('get conn')
    return conn

def query_all(cur, sql, args):
    cur.execute(sql, args)
    return cur.fetchall()

def read_mysql_to_csv(filename):
    with codecs.open(filename=filename, mode='w', encoding='utf-8') as f:
        write = csv.writer(f, dialect='excel')
        conn = get_conn()
        cur = conn.cursor()
        cur.execute('select * from users_resulttable')
        #sql = ('select * from users_resulttable WHERE userId = 1001')
        rr = cur.fetchall()
        #results = query_all(cur=cur, sql=sql, args=None)
        for result in rr:
            print(result)
            write.writerow(result[:-1])


def read_mysql_to_csv2(filename,user):
    with codecs.open(filename=filename, mode='a', encoding='utf-8') as f:
        write = csv.writer(f, dialect='excel')
        conn = get_conn()
        cur = conn.cursor()
        cur.execute('select * from users_resulttable')
        sql = ('select * from users_resulttable WHERE userId = 1001')
        rr = cur.fetchall()
        results = query_all(cur=cur, sql=sql, args=None)
        for result in results:
            #print(result)
            write.writerow(result[:-1])





if __name__ == '__main__':
    # main()
    read_mysql_to_csv('../resulttable.csv')
