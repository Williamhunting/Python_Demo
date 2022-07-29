#Python中装饰器的使用
#引自：https://www.runoob.com/w3cnote/python-func-decorators.html

##############################
def hi(name = "yasoob"):
    return "Hi" + name

print(hi())  #python可以直接打印函数的renturn 

greet = hi #在python中甚至可以将一个函数赋值给一个变量

print(greet()) #在python中，函数名后面加括号是调用该函数，不加括号就将该函数作为参数传递，


del greet
del hi
########################################

#######################################
def hi(name = "yasoob"):
    print("now you are inside the hi() function")
    def greet():
        return "now you are in the greet() function"
    def welcome():
        return "now you are in the welcome() function"
    print (greet())
    print(welcome())
    print("now you are back in the hi() function")

hi()
#greet() #上面可见可以在函数中定义函数，但是在内部定义的函数不能在外部调用
del hi
###############################################

############################################
def hi(name = "yasoob"):
    def greet():
        return "now you are in the greet() function"
    def welcome():
        return "now you are in the welcome() function"
    if name == "yasoob":
        return greet
    else:
        return welcome

a = hi()
print(a)
print(a())
del hi
del a
################################################
def hi():
    return "Hi, yasoob!"

def dosomethingbeforehi(func):
    print("I am doing some boring work before excuting hi()")
    print(func())

dosomethingbeforehi(hi)

##################################################

#####################################################
#装饰器写法一
##def a_new_decorator(a_func):
##    def wrapthefunction():
##        print("I am doing some boring work before executing a_func()")
##
##        a_func()
##        print("I am doing some boring work after executing a_func()")
##
##    return wrapthefunction

#装饰器写法二
def a_new_decorator(a_func):
    print("I am doing some boring work before executing a_func()")
    a_func()
    print("I am doing some boring work after executing a_func()")


def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my  foul smell")

a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)

a_function_requiring_decoration()  #对应装饰器写法一
#a_function_requiring_decoration #对应装饰器写法二，即当装饰器并不返回一个函数，而是直接输出时，调用被装饰的函数时不加括号

del a_function_requiring_decoration

@a_new_decorator
def a_function_requiring_decoration():
    """ Hey you! Decorate me! """
    print("I am the function which needs some decoration to remove my  foul smell")

a_function_requiring_decoration()

#实际上：@a_new_decorator的写法就是a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)的简写



































