class Pair_Element:
    def twoSum(self,nums,targets):
        lookup={}

        for i,j in enumerate(nums):
            if targets-j in lookup:
                return(lookup[targets-j],i)
            lookup[j]=i

value=int(input("enter the number : "))
print("index1= %d,index2= %d"%Pair_Element().twoSum((10,20,30,40,50,60,70,80,90),value))
            

