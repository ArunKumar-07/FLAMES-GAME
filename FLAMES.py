name1 = input("Enter your name :").lower()
name2 = input("Enter your crush name:").lower()
name1 = name1.replace(" ","")
name2 = name2.replace(" ","")
print("")
print("-->",name1)
print("-->",name2)

for i in name1:
	for j in name2:
		if i == j :
			name1 = name1.replace(i,"",1)
			name2 = name2.replace(j,"",1)
			break;

count = len(name1+name2)
print("")
print(count)
print("")
print("FLAMES...")
print("F = Friend \nL = Love \nA = Affection \nM = Marriage \nE = Enemy \nS = Siblings \n\n")
if count>0:
	list1 = ["FRIENDS","LOVERS","AFFECTIONATE","MARRIAGE","ENEMIES","SIBLINGS"]
	while len(list1)>1:
		c = count%len(list1)
		s_index= c-1
		if s_index>0:
			left = list1[:s_index]
			right = list1[s_index+1:]
			list1 = right+left
		else:
		    list1 = list1[:len(list1)-1]
	print("-------------------------")
	print("")	    
	print("Relationship is ",list1[0])
	print("")
	print("-------------------------")
else:
	print("try different names")	    