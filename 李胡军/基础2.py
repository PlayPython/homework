## 异常和错误练习
# - 使用try-except处理文件打开异常，打开一个不存在的文件，打印提示信息，但是程序不中断
def try_except_finally(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            print(f.readlines())
    except FileExistsError as e:
        print('文件不存在')
    finally:
        print('不管在不在，程序就是不会中断')


# - 使用raise强制抛出异常，input()只接受正整数的输入,否则中断程序，强制抛出异常
def raise_exception():
    m = input("输入内容:")
    try:
        m = int(m)
        if isinstance(m, int) and m > 0:
            if m > 0:
                print("ojbk")
        else:
            raise Exception
    except:
        raise Exception


# # 函数练习
# - 定义一个函数，传入一个由数字组成列表，返回最大最小值
def fun0(l1):
    return min(l1), max(l1)


# - 定义一个函数，参数可以接受不定参数和字典参数，打印传入的参数
def fun1(a, b, *c, **d):
    dict = {
        "a": a,
        "b": b,
        "c": c,
        "d": d
    }
    return dict


# - 定义匿名函数，返回两数乘积
lmd = lambda x, y: x * y


# - 写一个函数，返回N的阶乘
def func1(n):
    n2 = 1
    for n1 in range(1, n + 1):
        n2 = n1 * n2
    return n2


if __name__ == "__main__":
    # try_except_finally("./file1.txt")  # 文件存在
    # try_except_finally('./file2.txt')  # 文件不存在
    # raise_exception()
    # print(fun1(1,2,"33","44",a1="a1"))
    # print(lmd(2,3))
    # print(func1(4))
    pass

# - 把前面的一些练习题封装成一个个函数实现
#
# # 模块和类
# - 导入自定义模块里面的函数，并使用
# - 安装requests并使用，引入时候给requests包使用别名。使用requests包调用github API获取返回值
#   + github API https://developer.github.com/v3/
# - 定义一个类，同时具有堆栈的数据结构，实现四个方法
#   + shift() 返回并删除列表最后一个元素
#   + unshift() 添加列表第一个元素
#   + push() 添加到列表最后一个元素
#   + pop()  返回并删除列表最后一个元素
# - 定义一个类，实现深度优先搜索和广度优先搜索两个方法
# - 定义一个基类pet，并定义一些通用属性和方法，定义子类猫和狗，从pet基类继承
#
#
# ## 备注：Git持续集成问题梳理
#
# - 在实际项目中主分支是master ，一般是我们在远端创建一个自己的分支，然后本地克隆自己的分支，在自己的分支上修改，
# 然后先将master上面修改的东西push到自己的分支上使自己分支的东西跟master保持一致，然后将本地的代码push到自己的分支上，
# 再通过有权限的管理员，将自己的分支push到master，这就是整个Git的大概工作流程。
