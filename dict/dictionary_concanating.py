dict1 = {1:'Vivek'}
dict2 = {2:'John'}
dict3 = {3:'Methew'}
dic4 = {}
for i in (dict1, dict2, dict3): 
    dic4.update(i)
    print(dic4)