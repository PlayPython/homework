
#- 导入自定义模块里面的函数，并使用
import test
def importfun():
    test.jiecheng(5)

#- 安装requests并使用，引入时候给requests包使用别名。使用requests包调用github API获取返回值
import requests as req
def requestgit():
    response=req.get("https://developer.github.com/v3/")
    print(response.content)

if __name__ == '__main__':
    print("\n①、导入模块练习，并使用该模块的函数")
    importfun()
    print("\n②、requests库访问某个网站，并返回结果")
    requestgit()