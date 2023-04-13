"""

"""

import time
import threading


def sing(msg):
    while True:
        print(f"{msg}")
        time.sleep(1)


def dance(msg):
    while True:
        print(f"{msg}")
        time.sleep(1)


sing_thread = threading.Thread(target=sing, args=("我在唱歌,啦啦啦",))
dance_thread = threading.Thread(target=dance, kwargs={"msg": "我在跳舞,噜噜噜噜"})

sing_thread.start()
dance_thread.start()
