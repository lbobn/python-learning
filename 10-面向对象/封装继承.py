"""
封装
"""


class Phone:
    __on = True

    def __call(self):
        print("打电话")

    def use(self):
        if self.__on:
            print("已开机")
            self.__call()
        else:
            self.__on = True
            print("开机中")
            self.__call()


class Infrared:
    __remote_control = True

    def __open_TV(self):
        print("打开电视")


class IPhone(Phone, Infrared):
    __play = True

    def play_game(self):
        if (self.__play):
            print("打游戏")


class Xiaomi(Phone, Infrared):
    __on = True

    def use(self):
        if self.__on:
            print("发短信")

    pass


iphone = IPhone()
iphone.play_game()
iphone.use()

xiaomi = Xiaomi()
xiaomi.use()
