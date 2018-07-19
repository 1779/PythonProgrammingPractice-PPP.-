class Test(object):
    def __init__(self,switch):
        self.switch = switch

    def calc(self,a,b):
        try :

            return a/b
        except Exception as result:

            if self.switch:
                print("捕获到了异常，异常信息如下：")
                print(result)

            else:
                raise


test=Test(True)
test.calc(11,0)
print("---------------华丽分割线----------------")
 
a.switch=False
test.calc(11,0)

