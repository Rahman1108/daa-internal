def mergesort(list1):
 if(len(list1)>1):
 mid=len(list1)//2
 leftlist=list1[:mid]
 rightlist=list1[mid:]
 mergesort(leftlist)
 mergesort(rightlist)
 k=0
 i=0
 j=0
 while i<len(leftlist) and j<len(rightlist):
 if(leftlist[i]<rightlist[j]):
 list1[k]=leftlist[i]
 i=i+1
 k=k+1
 else:
 list1[k]=rightlist[j]
 j=j+1
 k=k+1
 while i<len(leftlist):
 list1[k]=leftlist[i]
      i=i+1

 k=k+1

num=int(input("How many elements you want to enter in the list:"))
list1 = input('Enter the list of numbers: ').split()
list1=[int(input())for x in range(num)]
mergesort(list1)
print('Sorted list: ', end='')
print(list1)