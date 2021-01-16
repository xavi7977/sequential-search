Sequential_test.py
import timeit

# class for sequential search
class SequentialStringList:

    # constructor, which creates a list
    def __init__(self):

        self.list=[]

    # method to add the element to a list
    def add(self,element):

        self.list.append(element)

    # method to find the element in a list
    def find(self,element):

        for i in self.list:
            if i == element:
                return i

        return None

# class for binary search
class BinaryStringList:

    # constructor, which creates a list
    def __init__(self):

        self.list2=[]
      
    # method to add the element to a list
    def add(self,element):
        self.list2.append(element)

    # method to find the element in a list
    def find(self,element):

        self.list2.sort()

        first_pos=0
        last_pos=len(self.list2)-1
        flag=False

        while first_pos <= last_pos and not flag:
            mid_point=(first_pos+last_pos )//2

            if self.list2[mid_point] == element:              
                return self.list2[mid_point]
            else:
                if element < self.list2[mid_point]:
                    last_pos=mid_point - 1
                else:
                    first_pos=mid_point + 1

        return None
    if __name__=='__main__':

        code='''
from __main__ import SequentialStringList
ob=SequentialStringList()
ob.add('java')
ob.add('python')
ob.add('perl')
ob.add('c')
ob.add('c++')
ob.add('ada')
ob.add('go')
ob.add('rust')
ob.add('swift')
ob.add('html')
ob.add('php')
ob.add('bash')
ob.add('c#')
ob.add('cython')
ob.add('jython')
ob.add('cobol')
ob.add('fortran')
ob.add('basic')
ob.add('smalltalk')
ob.add('pascal')
'''

    # finding the execution for searching the list
    t=timeit.timeit("ob.find('fortran')",code,number=1)
    print('Sequential Search, String found: ',t)
    t2=timeit.timeit("ob.find('simula')",code,number=1)
    print('Sequential Search, String not found: ',t2)
