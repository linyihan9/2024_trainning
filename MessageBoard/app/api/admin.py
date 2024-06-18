from flask import Blueprint
import threading
from datetime import datetime
import time

admin = Blueprint('admin',__name__)

@admin.route('/')
def index():
    return 'Hello admin'


def thread_func():  # 线程函数
    time.sleep(0.01)
    print('我是一个线程函数', datetime.now())

@admin.route('/thread')
def many_thread():
    for num in range(100):  # 循环创建500个线程
        t = threading.Thread(target=thread_func)
        t.start()
        print('还在添加线程'+str(num))
    return 'thread'