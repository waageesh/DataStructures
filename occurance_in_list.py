def occurance(a,key):
    dict = set()
    count=0
    for i in range(0,len(a)):
      if i not in dict and a[i]==key:
          dict.add(i)
          count+=1
    return count
          




a = [1,4,3,4,3,6,4,3,8,1]
obj = occurance(a,4)
print(obj)