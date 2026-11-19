from abc import ABC,abstractmethod

class ABSClass(ABC):
      def print(self,x):
            print("passed value : ",x)

      @abstractmethod
      def task(self):
            print("we are inside abstract method")

class test_class(ABSClass):
      def task(self):
            print("gave implementation to abstract method")


test_obj=test_class
test_obj.task()
test_obj.print(200)