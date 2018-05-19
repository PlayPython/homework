
#- 定义一个类，同时具有堆栈的数据结构，实现四个方法
#  + unshift() 添加列表第一个元素
#  + push() 添加到列表最后一个元素
#  + pop()  返回并删除列表最后一个元素
class class_test(object):
    def unshift(self):
        varlist.insert(0,"夏目玲子")
        print(varlist)

    def push(self):
        varlist.append("小燕子")
        print(varlist)

    def pop(self):
        x=len(varlist)
        print("最后一个元素:",end=' ')
        print(varlist[x-1])
        varlist2=varlist[:-1]
        print(varlist2)

#- 定义一个类，实现深度优先搜索和广度优先搜索两个方法
class sousuo(object):
    def guangdu(self):
        pass

    def shendu(self):
        pass

#- 定义一个基类pet，并定义一些通用属性和方法，定义子类猫和狗，从pet基类继承
class pet(object):
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour
        print("{0}的{1}".format(colour,name))

    def test(self):
        return "--------分割线--------"

class cat(pet):
    def jiao(self):
        return "喵喵喵"

class dog(pet):
    def jiao(self):
        return "汪汪汪"

if __name__=="__main__":
    print("关于类的练习\n")
    my_class=class_test()
    varlist = ["夏目贵志","藤原兹","藤原塔子","娘阔老师","中级妖怪","丙","小狐狸"]
    print("有这样一个list:\n{0}".format(varlist))
    print("\n①、往列表最前面加入一个元素")
    my_class.unshift()
    print("\n②、往列表最后面加入一个元素")
    my_class.push()
    print("\n③、返回并删除最后一个元素")
    my_class.pop()

    print("\n########################\n")

    my_class = pet("小燕子", "美丽")
    print(my_class.test())
    my_cat = cat("sendy", "灰色")
    print(my_cat.jiao())
    print(my_cat.test())
    my_cat = cat("旺财", "黑色")
    print(my_cat.jiao())
    print(my_cat.test())
