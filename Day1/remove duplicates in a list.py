n=int(input()) #size of the list
mylist=list(input().split())#use space to take input don't use enter
mylist = list(dict.fromkeys(mylist))
print(mylist)