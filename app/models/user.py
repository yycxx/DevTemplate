from datetime import datetime
from sqlalchemy import Column, String, INT, DATETIME

from app.models import Base


class User(Base):
    __tablename__ = "user"

    id = Column(INT, primary_key=True, comment="用户唯一id")
    username = Column(String(16), unique=True, index=True, comment="用户名")
    name = Column(String(16), index=True, comment="姓名")
    password = Column(String(32), unique=False, comment="用户密码")
    email = Column(String(64), unique=True, nullable=False, comment="用户邮箱")
    role = Column(INT, default=0, comment="0: 普通用户 1: 组长 2: 超级管理员")
    created_at = Column(DATETIME, nullable=False, comment="创建时间")
    updated_at = Column(DATETIME, nullable=False, comment="更改时间")
    deleted_at = Column(DATETIME, comment="删除时间")
    last_login_at = Column(DATETIME, comment="上次登录时间")

    def __init__(self, username, name, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.role = 0
