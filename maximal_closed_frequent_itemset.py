import pandas as pd
from __future__ import division
automobile_data = pd.read_csv("Data mining\Homework4\Problem 3\\data\new_data.txt",delimiter=",")
new_data = automobile_data
total_size =  len(new_data)
#This is the minimum Support value which is set initially as user specified values
#This value is in terms of percentage.
minimum_support = 10
#This dictionary contains the 1 frequent itemsets.
frequent_one_itemset = {}
#Iterate over all the columns 
for column in new_data:
    #If support of the column is more than the minimum threshold then only the iterm is considered and stored.
    support = len(new_data[new_data[column]==1])/total_size*100
    if support > minimum_support: 
        frequent_one_itemset[column] = support

#set value of k as 2
k = 2 
#Initially pruned and frequent items are the same.
frequent_one_item  = sorted(frequent_one_itemset)
pruned_item = sorted(frequent_one_itemset)
#This dictionary stores the 2 frequent itermsets.
dicti = {}
#This dictionary store the final_pruned data
final_prune = {} 
k_itemset = {}
from itertools import combinations

level_wise_dictionary1 = {}
level_wise_dictionary1[1] = frequent_one_itemset
particular_level_dictionary1 = {}
#Here k is to iterate over total number of columns and not the frequent itemsets.
k = 2
while k != len(sorted(frequent_one_itemset)) :
    print "AT stage " , k
    combination_of_keys = combinations(frequent_one_item,k)
#     print combination_of_keys.next()
    particular_level_dictionary1 = {}
    for values in combination_of_keys: 
        
        updated = new_data
        for index in values:
            updated = updated[updated[index]==1]
        #Store the support of the current index in the dictionary
        if (len(updated)/total_size*100)>=minimum_support:
            particular_level_dictionary1[values]= (len(updated)/total_size*100)
    #Store the whole dictionary just created into another dictionary with its key as "K"
    level_wise_dictionary1[k] = particular_level_dictionary1
    k = k + 1
#print length of candidate itemset generated.
print length_candidate
#print length of frequent itemset generated.
print length_frequent


maximal_frequent_itemset = {}
maximal_sum = 0
for indi in range(1,len(sorted(frequent_one_itemset))-1):
    print "Working for level ",indi
    for key in level_wise_dictionary1[indi]:
        z = [value1 for key1,value1 in level_wise_dictionary1[indi+1].items() if ''.join(map(str,key)) in ''.join(map(str,key1))]
        for key1,value1 in level_wise_dictionary1[indi+1].items():
            if ''.join(map(str,key)) in ''.join(map(str,key1)):
                print key, key1, value1
#         print key, z
        if len(z) == 0 :
            maximal_sum = maximal_sum +1
            print key
print maximal_sum


maximal_frequent_itemset = {}
closed_sum = 0
#After finding the frequent itmemset we find the maximal itemsets and stoe sum of closed itemsets. 
for indi in range(1,len(sorted(frequent_one_itemset))-1):
    print "Working for level ",indi
    for key in level_wise_dictionary1[indi]:
        #&& level_wise_dictionary1[indi+1][key]==level_wise_dictionary1[indi+1][key]]
        z1 = [value1 for key1,value1 in level_wise_dictionary1[indi+1].items() if ''.join(map(str,key)) in ''.join(map(str,key1))  ]
        if len(z) == 0 :
            closed_sum = maximal_sum +1
            print key
print closed_sum
