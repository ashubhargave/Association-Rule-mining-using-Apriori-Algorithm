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
 
diff_prune = {}
diff_prune[1] = frequent_one_itemset
final_prune[2] = dicti
print final_prune  
  
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

diction = {}
diction1 = {}
lift_parameter = {}
index = 0 
#Here frequent_items is the dictionary containing different k levels of frequent itemsets
for i in range(1,len(frequent_items)):
    #Then iterate over the keys in the 2, 3, 4, etc. frequent itermsets.
    for keys in frequent_items[i]:
    #     print keys
        #Store all the key as list
        t = list(keys)
        #If the key is having multiple iterms iterate over the key
        for i in range(1,len(t)):
            l1 = t[0:i]
            l2 = t[i:len(t)]
            #Create combination of the left part of the Rule
            perm1 = list(combinations(t[:len(t)],i))
            #Create combination of the right part of the Rule
            perm2 = list(combinations(t[:len(t)],len(t)-i))
            z2 = perm2[::-1]

            for indexed in range(0,len(perm1)):
                print perm1[indexed], " uyuyuyyu", z2[indexed]
                try:
                    if len(perm1[indexed])==1:
    #                     print perm1[indexed], "Came in if"
                        if len(z2[indexed])==1:
                            if diction1.has_key(perm1[indexed][0]) and lift_parameter.has_key(perm1[indexed][0]):
    #                             print z2[indexed], "Came in first if dictionary present"
                                diction1[perm1[indexed][0]][z2[indexed]]= diff_prune[len(index_union)][index_union]/diff_prune[1][z2[indexed][0]]
                                supp = diff_prune[1][perm1[indexed][0]] * diff_prune[1][z2[indexed][0]]
                                lift_parameter[perm1[indexed][0]][z2[indexed]]= diff_prune[len(index_union)][index_union]/supp
                            else:
    #                             print z2[indexed], "Came in first else dictionary absent"
                                diction1[perm1[indexed][0]]={}
                                lift_parameter[perm1[indexed][0]]={}
                                diction1[perm1[indexed][0]][z2[indexed]]= diff_prune[len(index_union)][index_union]/diff_prune[1][z2[indexed][0]]
                        else:
                            if diction1.has_key(perm1[indexed][0]) and lift_parameter.has_key(perm1[indexed][0]):
                                index_union = tuple(perm1[indexed][0].split()+list(z2[indexed]))
    #                             print index_union
    #                             print diff_prune[len(index_union)][index_union]
    #                             print z2[indexed], "Came in second if z2 size more dict yes"
                                diction1[perm1[indexed][0]][z2[indexed]]= diff_prune[len(index_union)][index_union]/diff_prune[1][perm1[indexed][0]]
                                lift_parameter[perm1[indexed][0]][z2[indexed]]= diction1[perm1[indexed][0]][z2[indexed]]/diff_prune[len(z2[indexed])][z2[indexed]]
                            else:
    #                             print z2[indexed], "Came in second else z2 size more dict no"
                                diction1[perm1[indexed][0]]={}
                                lift_parameter[perm1[indexed][0]]={}
                                index_union = tuple((perm1[indexed][0].split())+list(z2[indexed]))
    #                             print index_union
    #                             print diff_prune[len(index_union)][index_union]
                                diction1[perm1[indexed][0]][z2[indexed]]= diff_prune[len(index_union)][index_union]/diff_prune[1][perm1[indexed][0]]
                                lift_parameter[perm1[indexed][0]][z2[indexed]]=diction1[perm1[indexed][0]][z2[indexed]]/diff_prune[len(z2[indexed])][z2[indexed]]
                    else:
                        print "came in else"
                        if len(z2[indexed])==1:
                            if (diction1.has_key(perm1[indexed]) and lift_parameter.has_key(perm1[indexed])):
    #                             print z2[indexed], "Came in first if z2 less dict yes"
                                index_union = tuple(list(perm1[indexed])+(z2[indexed][0].split()))
    #                             print diff_prune[len(index_union)][index_union]                            
                                diction1[perm1[indexed]][str(z2[indexed][0])]= diff_prune[len(index_union)][index_union]/diff_prune[len(perm1[indexed])][perm1[indexed]]
                                lift_parameter[perm1[indexed]][str(z2[indexed][0])]= diction1[perm1[indexed]][str(z2[indexed][0])]/diff_prune[1][z2[indexed][0]]
                            else:
    #                             print z2[indexed], "Came in first else z2 less dict no"
                                diction1[perm1[indexed]]={}
                                lift_parameter[perm1[indexed]]={}
    #                             print diction1[perm1[indexed]]
    #                             print z2[indexed][0], "   ",perm1[indexed]
                                temp = list(perm1[indexed])+(z2[indexed][0].split())
                                index_union = tuple(temp)
    #                             print diff_prune[len(index_union)][index_union]                            
                                diction1[perm1[indexed]][str(z2[indexed][0])]= diff_prune[len(index_union)][index_union]/diff_prune[len(perm1[indexed])][perm1[indexed]]
                                lift_parameter[perm1[indexed]][str(z2[indexed][0])]=diction1[perm1[indexed]][str(z2[indexed][0])]/diff_prune[1][z2[indexed][0]]
                        else:
                            if (diction1.has_key(perm1[indexed]) and lift_parameter.has_key(perm1[indexed])):
    #                             print z2[indexed], "Came in second if z2 size more dict yes"
                                index_union = tuple(list(perm1[indexed])+list(z2[indexed]))
    #                             print diff_prune[len(index_union)][index_union]
                                diction1[perm1[indexed]][z2[indexed]]= diff_prune[len(index_union)][index_union]/diff_prune[len(perm1[indexed])][perm1[indexed]]
                                diction1[perm1[indexed]][z2[indexed]]=diction1[perm1[indexed]][z2[indexed]]/diff_prune[len(z2[indexed])][z2[indexed]]
                            else:
                                diction1[perm1[indexed]]={}
                                lift_parameter[perm1[indexed]]={}
    #                             print z2[indexed], "Came in second else z2 size more dict no"
                                index_union = tuple(str(perm1[indexed])+list(z2[indexed]))
    #                             print index_union
    #                             print diff_prune[len(index_union)][index_union]
                                diction1[perm1[indexed]][z2[indexed]]= diff_prune[len(index_union)][index_union]/diff_prune[len(perm1[indexed])][perm1[indexed]]
                                lift_parameter[perm1[indexed]][z2[indexed]]=diction1[perm1[indexed]][z2[indexed]]/diff_prune[len(z2[indexed])][z2[indexed]]
                except:
                    pass

min_conf = 0.7
ry = {}
for keys,calues in diction1.items():
    for item,values in calues.items():
        if values>min_conf:
            ry[keys, item] = values
#             print keys, item, values
#     print "*******************"
#     print calues
# print ry
# print sorted(ry.values)
d_view = [ (v,k) for k,v in ry.iteritems() ]
d_view.sort(reverse=True) # natively sort tuples by first element
print_index = 0
for v,k in d_view:
    print "%s: %f" % (k,v)
    print_index = print_index+1
    if print_index ==10:
        break
        
# print lift_parameter
min_lift = 0.00
ry = {}
for keys,calues in lift_parameter.items():
    for item,values in calues.items():
        if values>min_lift:
            ry[keys, item] = values
#             print keys, item, values
#     print "*******************"
#     print calues
# print ry
# print sorted(ry.values)
d_view = [ (v,k) for k,v in ry.iteritems() ]
d_view.sort(reverse=True) # natively sort tuples by first element
print_index = 0
for v,k in d_view:
    print "%s: %f" % (k,v)
    print_index = print_index+1
    if print_index ==90:
        break
print len()