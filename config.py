# 基础配置类
import os
from urllib import parse


class Config(object):
    ROOT = os.path.dirname(os.path.abspath(__file__))
    LOG_NAME = os.path.join(ROOT, 'logs', 'server.log')
    # 服务信息
    SERVER_HOST = "127.0.0.1"
    SERVER_PORT = 8088

    # MySQL连接信息
    MYSQL_HOST = "127.0.0.1"
    MYSQL_PORT = 3306
    MYSQL_USER = "root"
    MYSQL_PWD = "yourpwd"
    DBNAME = "yourdb"

    # sqlalchemy
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(
                                    MYSQL_USER, parse.quote_plus(MYSQL_PWD), MYSQL_HOST, MYSQL_PORT, DBNAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 权限 0 普通用户 1 组长 2 管理员
    GUEST = 0
    MANAGER = 1
    ADMIN = 2
