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
#Create a combination of different keys from first frequent itemset.
def get_keys(pruned_item, frequent_one_item):
    u = []
    #Returns a dictionary of keys.
    for num in sorted(pruned_item):
            print type(num)
            #Check if column is a single number of a tuple or string.
            if type(num) is tuple:
                z = num
            elif type(num) is numpy.int64 or type(num) is str:
                z = []
                z.append(num)
            #Iterate over the frequent on2 itemset and returns the keys.
            for keys in sorted(frequent_one_item):
                if numpy.logical_and(keys not in (z),z[-1]<keys):
                        o = list(z) + [keys]
                        u.append(o)
    return u

final_prune = {} 
k_itemset = {}
#To store the lenght of candidate itemsets
length_candidate = 0
#TO store the length of frequent itermsets
length_frequent = 0
frequent_one_item  = sorted(frequent_one_itemset)
pruned_item = sorted(frequent_one_itemset)
frequent_one_item  = sorted(frequent_one_itemset)
combination_of_keys = get_keys(pruned_item,frequent_one_item)
dicti = {}
for values in combination_of_keys: 
            updated = new_data
        #Check if the current combination is present in the k frequent itemset. THen only find its support. 
#         if values in pruned_k_frequent_itemset:
            sum1 = 0 
            for indexes in values:
                updated = updated[updated[indexes]==1]
#                 sum1 = sum1 + len(updated)
#             print values, " " ,(len(updated)/total_size*100)
            if (len(updated)/total_size*100)>minimum_support:
#                 print tuple(values)
#                 print len(updated)
                dicti[tuple(values)] = len(updated)/total_size*100
print "This is the " , k , " level frequent itemset"
#level 2 frequent itemset
print dicti
#To find the values from the dataset which are present for this keys.
#i.e. If a column is "Bread" and "Beer" I try to find all the 1's present for these two columns.
def combine_list(keys):
    updated = new_data
    for key in keys:
        updated = updated[updated[key]==1]
    return len(updated)/total_size*100
#This method creates the combination of keys for the Frequent itemset generation.
def candidate_generation(dicti):
    adict = {}
    for num in sorted(dicti):
        for keys in sorted(dicti):
            if (list(keys[0])==list(num[0])) and (num[-1]<keys[1]):
                    o = list(num)
                    o.append(keys[1])
#                     print o
                    adict[tuple(o)] = combine_list(o)      
    return adict

# This method finds the pruned set
def prune_itemset(candidate_generated):
    pruned = {}
    # Check if minimum_support is more or less than our support.
    for index in candidate_generated:
        if candidate_generated[index]>minimum_support:
            pruned[index]=candidate_generated[index]
    return pruned
    
  
k = 2 
final_prune = {} 
k_itemset = {}
#To store the lenght of candidate itemsets
length_candidate = 0
#TO store the length of frequent itermsets
length_frequent = 0
#Sort the keys or items lexicographically
frequent_one_item  = sorted(frequent_one_itemset)
pruned_item = sorted(frequent_one_itemset)
frequent_one_item  = sorted(frequent_one_itemset)
combination_of_keys = get_keys(pruned_item,frequent_one_item)
#This stores level two frequent itemset.
dicti = {}
#Iterate over the lexicographically sorted items
for values in combination_of_keys: 
            updated = new_data
        #Check if the current combination is present in the k frequent itemset. THen only find its support. 
            sum1 = 0 
            for indexes in values:
                updated = updated[updated[indexes]==1]
#                 sum1 = sum1 + len(updated)
#             print values, " " ,(len(updated)/total_size*100)
            if (len(updated)/total_size*100)>minimum_support:
                dicti[tuple(values)] = len(updated)/total_size*100
print "This is the " , k , " level frequent itemset"

k = 3
while k != 0 :
    print "AT stage " , k
    candidate_generated = candidate_generation(dicti)
    print "This is the candidate generated ", len(candidate_generated)
    length_candidate = length_candidate + len(candidate_generated) 
    pruned_k_frequent_itemset = prune_itemset(candidate_generated)
    final_prune[k] = pruned_k_frequent_itemset
    pruned_item = sorted(pruned_k_frequent_itemset)
    dicti = pruned_k_frequent_itemset
    print "This is the next level pruned items ",len(pruned_item)
#     print pruned_item
    length_frequent = length_frequent + len(pruned_item)
#         print k_itemset
    if len(pruned_k_frequent_itemset)==0:
            print "STOP when k is ", k
            print final_prune[k-1]
            k=0
            break
    elif k==len(sorted(frequent_one_itemset)):
        k = 0
    else:
            print "Update k to ", k+1
            k = k+1
#print length of candidate itemset generated.
print length_candidate
#print length of frequent itemset generated.
print length_frequent