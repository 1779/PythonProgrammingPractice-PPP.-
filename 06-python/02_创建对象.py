#创建一个Home对象
class Home:
    def __init__(self,new_area,new_type,new_addr):
        self.area = new_area
        self.type = new_type
        self.addr = new_addr
        self.left_area = new_area
        self.contents =[]

    
    def __str__(self):
        return "房子的面积是：%d\n房子的户型是：%s\n房子的地址是：%s\n房子里面的家具有：%s\n房子的可用面积是：%d"%(self.area,self.type,self.addr,str(self.contents),self.left_area)

    def add_content(self,item):
        #self.contents.append(new_add.name)
        #self.left_area -= new_add.area
        self.contents.append(item.get_name())
        self.left_area -= item.get_area()


class Bed:
    def __init__(self,bed_area,bed_name):
        self.area=bed_area
        self.name=bed_name

    def __str__(self):
        return "%s的占地面积为:%d"%(self.name,self.area)

    def get_name(self):
        return self.name

    def get_area(self):
        return self.area

class Table:
    def __init__(self,table_area,table_name):
        self.area=table_area
        self.name=table_name

    def __str__(self):
        return "%s的占地面积为:%d"%(self.name,self.area)

    def get_name(self):
        return self.name

    def get_area(self):
        return self.area



#++++++++++++++++++++++++++++++++++++++++++++++++++

def get_house_name():
    house_number = input("请输入房子的编号：")
    return "house"+house_number
def buy_a_house():
    house_area = int(input("请输入房子的面积："))
    house_type = input("请输入房子的类型：")
    house_addr = input("请输入房子的地址：")
    house=eval(Home(house_area,house_type,house_addr))
    return house


#+++++++++++++++++++++++++++++++++++++++++++++++++

house=buy_a_house()


#house= Home(150,"三室一厅","北京市")
bed1 = Bed(4,"席梦思")
table1 = Table(2,"长桌子")

print(bed1)
print(table1)

house.add_content(table1)
house.add_content(bed1)
print(house)
