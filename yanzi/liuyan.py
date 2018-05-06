# 异常和错误练习
#- 改进input函数，使用try - except处理异常，只接受正整数输入，非正整数输入判断类型，打印提示
def fun(a):
    #a=input("请输入一个数：")
    try:
        if isinstance(a,int) and a>0:
            print("{0}是一个正整数".format(a))
        else:
            raise AssertionError("输入的不是一个正整数")
    except Exception as e:
        print(e)
fun(-1)
fun(0)
fun(22)
# 函数练习

#定义一个函数，传入一个由数字组成列表，返回最大最小值
def fun1(a):
    for i in range(len(a)+1):
        for j in range(len(a)-i-1):
            if a[j+1]>a[j]:
                a[j],a[j+1]=a[j+1],a[j]

    print(a)
    print("{0}中最大的数是{1}，最小的数是{2}".format(a,a[0],a[-1]))


fun1([1,3,5,7,9,2])

#定义一个函数，参数可以接受不定参数和字典参数，打印传入的参数


'''
-
- 定义匿名函数，返回两数乘积
- 写一个函数，返回N的阶乘
- 把前面的一些练习题封装成一个个函数实现
'''
# 模块和类

'''
- 导入自定义模块里面的函数，并使用
- 安装requests并使用，引入时候给requests包使用别名。使用requests包调用github API获取返回值
  + github API https://developer.github.com/v3/
- 定义一个类，同时具有堆栈的数据结构，实现四个方法
  + shift() 返回并删除列表最后一个元素
  + unshift() 添加列表第一个元素
  + push() 添加到列表最后一个元素
  + pop()  返回并删除列表最后一个元素
- 定义一个类，实现深度优先搜索和广度优先搜索两个方法
- 定义一个基类pet，并定义一些通用属性和方法，定义子类猫和狗，从pet基类继承
'''

## 备注：Git持续集成问题梳理
'''
- 在实际项目中主分支是master ，一般是我们在远端创建一个自己的分支，然后本地克隆自己的分支，在自己的分支上修改，
然后先将master上面修改的东西push到自己的分支上使自己分支的东西跟master保持一致，然后将本地的代码push到自己的分支上，
再通过有权限的管理员，将自己的分支push到master，这就是整个Git的大概工作流程。

'''
