
class Data():

    def odd_data(self):                         # 0到20内的奇数
        odd_data = []
        for i in range(1, 20, 2):
            odd_data.append(i)
        print(odd_data)

    def even_data(self):                        # 0到20内的奇数
        even_data = []
        for n in range(2, 20, 2):
            even_data.append(n)
        print(even_data)


    def devid(self):                            # 判断整除
        while True:
            n = input("请输入被除数:")
            m = input("请输入除数")

            if int(m) == 0:
                print("请输入一个正整数")
                continue
            elif int(n) % int(m) != 0:
                print("%s不可以被%s整除!" % (n, m))
            else:
                print("%s可以被%s整除" % (n, m))
            break





if __name__ == '__main__':
    yb = Data()
    yb.odd_data()
    yb.even_data()
    yb.devid()
