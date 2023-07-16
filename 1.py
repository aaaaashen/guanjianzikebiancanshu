#可变参数
def struct(*args):
    print(args)

struct(1,2,3,4,5)
struct(1,1,4,5,1,4)

#关键字可变参数
def teatmup(**kwargs):#**被成为可选参数，其参数关键字是一个字典类型，key为一个字符串
    print(kwargs)

teatmup(age='114514',name='汤可')

#组合使用
def test(*asd,**qwer):#可选参数必须放到关键字参数之前
    print(asd)
    print(qwer)
    pass

test(11,2,54,14,pro='物理')

"""
总结:
    可选参数：接受的数据是一个元组类型
    关键字可选参数：接受的数据是一个字段类型
    可选参数必须放到关键字参数之前
"""


