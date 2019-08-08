class Calc:
    __num1 = None
    __num2 = None


    def __init__(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2


    def set_num1(self, num1):
        self.__num1 = num1


    def set_num2(self, num2):
        self.__num2 = num2


    def get_num1(self):
        return self.__num1


    def get_num2(self):
        return self.__num2


    def sum(self):
        return self.__num1+self.__num2


    def sub(self):
        return self.__num1-self.__num2


    def to_string(self):
        return "num1 is {} and num2 is {}".format(self.__num1, self.__num2)

class number(Calc):
    __num3=None
    def __init__(self, num1, num2,num3): 
        self.__num3=num3       
        super(number, self).__init__(num1, num2)

    def set_num3(self,num3):
        self.__num3=num3
    def get_get(self):
        return self.__num3

    def to_string(self):
        return "num1 is {} and num2 is {}.num3 is {}".format(self.get_num1(), self.get_num2(),self.__num3)


class calcstion:
    def get_type(self,num4):
        num4.get_type()
        

my_number=number(5,6,9)
my_calc=calcstion(34,56)
       
test_calc=calcstion()
test_calc.get_type(my_number)
test_calc.get_type(my_calc)

print(test_calc.to_string())





