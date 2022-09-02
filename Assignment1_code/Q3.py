
brothers = ('brother1', 'brother2','brother3')
sisters = ('sister1', 'sister2','sister3')

siblings= brothers+sisters
print("The siblings are:\n",siblings,"\n")

#count of siblings
count_siblings=len(siblings)
print("There are ",count_siblings,"siblings","\n")

#Adding the father and mother to siblings
family_members=siblings+('father','mother')
print("The family memebrs are :\n",family_members)
