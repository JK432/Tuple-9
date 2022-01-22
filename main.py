# Write a python program to find duplicate elements in an input tuple

tuplex = 2, 4, 5, 6, 2, 3, 4, 4, 7 
lst=[]
print(tuplex)

for i in tuplex:
  count = tuplex.count(i)
  if(count>1):
     if i not in lst:
       lst.append(i)
       print(i," have dupe items")
