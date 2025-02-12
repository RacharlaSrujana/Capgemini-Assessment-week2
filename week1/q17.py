'''17. Word counter'''

sentence=input("Enter any sentence : ").split()
dic={}
for i in range(len(sentence)):
    if sentence[i] in dic:
        dic[sentence[i]]+=1
    else:
        dic[sentence[i]]=1
for key,value in dic.items():
    print(f"{key} : {value}")