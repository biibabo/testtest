import pymysql

# 查询操作数据库分为以下步骤
# 1, 创建数据库连接
connect = pymysql.connect(
    host='121.5.178.227',  # 数据库地址
    port=3306,  # 数据库端口号  mysql端口一般是3306
    user='tanling',  # 用户名
    password='123456',  # 登陆密码
    database='shop',  # 要连接的数据库名
    charset='utf8',  # 数据库编码  一般默认utf8
    cursorclass=pymysql.cursors.DictCursor  # 编码格式  写上这串代码就会返回字典; 默认返回元组
)
# 2,创建游标, 用于pymysql与mysql数据库进行sql的提交与数据接收
cursor = connect.cursor()  # 使用创建好的连接  创建游标
# 3, 编写sql,通过execute(sql)进行sql的执行
sql = "SELECT * from ls_user u where u.nickname ='石狗子'"
cursor.execute(sql)
# 4,通过fetchall()来获取执行结果 , 以元组形式返回
db_datas = cursor.fetchall()
print(db_datas)  # 如果返回两条就使用 db_datas[1]
# 5, 关闭游标
cursor.close()
# 6, 关闭数据库连接   #及时关闭数据库以免浪费多余的资源
connect.close()

# 修改操作数据库分为以下步骤
# 1,创建数据库连接
connt = pymysql.connect(
    host='121.5.178.227',  # 数据库地址
    port=3306,  # 数据库的端口号
    user='tanling',
    password='123456',
    database='shop',  # 要连接的库
    charset='utf8',  # 编码格式
    cursorclass=pymysql.cursors.DictCursor  # 默认返回元组, 加上这个返回字典类型; 默认返回元组
)
# 2,创建游标
cur = connt.cursor()  # 使用创建好的连接  创建游标
# 3, 编写sql, 通过execute(sql) 进行sql的执行
sql = "update ls_user  set nickname ='二石狗子' where nickname ='石狗子'"
cur.execute(sql)  # 使用游标执行
# 4, 提交sql执行到数据库
connt.commit()
# 5, 关闭游标
cur.close()
# 6, 数据库关闭
connt.close()


# 复习
# 封装一个函数 , 要求传入参数是一个查询sql  函数中代码实现对这个sal查询, 并返回结果
def sql_inquire(arg1):
    connect = pymysql.connect(
        host='121.5.178.227',  # 数据库地址
        port=3306,  # 数据库端口号  mysql端口一般是3306
        user='tanling',  # 用户名
        password='123456',  # 登陆密码
        database='shop',  # 要连接的数据库名
        charset='utf8',  # 数据库编码  一般默认utf8
        cursorclass=pymysql.cursors.DictCursor  # 编码格式  写上这串代码就会返回字典; 默认返回元组
    )
    # 2,创建游标, 用于pymysql与mysql数据库进行sql的提交与数据接收
    cursor = connect.cursor()  # 使用创建好的连接  创建游标
    # 3, 编写sql,通过execute(sql)进行sql的执行
    cursor.execute(arg1)
    # 4,通过fetchall()来获取执行结果 , 以元组形式返回
    db_datas = cursor.fetchall()
    # 5, 关闭游标
    cursor.close()
    # 6, 关闭数据库连接   #及时关闭数据库以免浪费多余的资源
    connect.close()
    return db_datas  # 如果返回两条就使用 db_datas[1]


sql = "SELECT * from ls_user u where u.nickname ='石狗子'"
print(sql_inquire(sql))

# 封装一个类 来实现数据库查询
import pymysql


class MySQLSelect():
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def select(self, sql):
        try:
            # 创建数据库连接
            connect = pymysql.connect(
                host=self.host,  # 数据库地址
                port=self.port,  # 数据库端口号  mysql端口一般是3306
                user=self.user,  # 用户名
                password=self.password,  # 登陆密码
                database=self.database,  # 要连接的数据库名
                charset='utf8',  # 数据库编码  一般默认utf8
                cursorclass=pymysql.cursors.DictCursor  # 编码格式  写上这串代码就会返回字典(其实是列表子集的字典); 默认返回元组
            )
            # 创建游标, 用于pymysql与mysql数据库进行sql的提交与数据接收
            cur = connect.cursor()  # 使用创建好的连接  创建游标
            # 编写sql, 通过execute(sql)进行sql的执行
            cur.execute(sql)
        # except SyntaxError as e:
        #     print(f'出错了,可能是数据库连接时某一项输入错误;{e}')
        except pymysql.err.OperationalError as e:
            print(f'连接服务器超时,可能是服务器没有启动;{e}')
        except pymysql.err.ProgrammingError as e:
            print(f'您的语法可能有问题;{e}')
            if cur:
                # 关闭游标
                cur.close()
                # print('验证是否成功关闭游标')
            if connect:
                # 关闭数据库连接   #及时关闭数据库以免浪费多余的资源
                connect.close()
                # print('验证是否成功关闭数据库连接')
        else:
            # 通过fetchall()  #来获取执行结果, 以元组形式返回
            db_datas = cur.fetchall()
            # 关闭游标
            cur.close()
            # 关闭数据库连接   #及时关闭数据库以免浪费多余的资源
            connect.close()
            return db_datas  # 如果返回两条就使用 db_datas[1]
        finally:
            print('谢谢你的使用')

    def update(self):
        pass

    def delete(self):
        pass

    def insert(self):
        pass


sql = "SELECT * from ls_user u where u.nickname ='石狗子'"
if __name__ == '__main__':
    tanlingMysql = MySQLSelect(host='121.5.178.227', port=3306, user='tanling', password='123456', database='shop')
    print(tanlingMysql.select(sql))

# import pymysql
#
#
# class Database:
#
#     def __init__(self, sql):
#         self.__connect = pymysql.Connect(
#             host='121.5.178.227',
#             port=3306,
#             user='tanling',
#             password='123456',
#             charset='utf8',
#             database='studentsDB'
#         )
#         self.sql = sql
#
#     def select_db(self):
#         """
#         数据库查询数据
#         :return: 查询出的数据结果res
#         """
#         with self.__connect.cursor() as cur:
#             cur.execute(self.sql)
#             res = cur.fetchall()
#         self.__connect.close()
#         return res
#
#     def change_db(self):
#         """
#         数据库增、删、改
#         :return:
#         """
#         with self.__connect.cursor() as cur:
#             cur.execute(self.sql)
#             self.__connect.commit()
#         self.__connect.close()
