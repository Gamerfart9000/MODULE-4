list={"Codingal":3 ,"is":3 , "the":3 ,"best":3 , "for":3 ,"coding":3}
print("Original dict:" ,list)

k=3
res=0
for key in list:
    if list[key]== k:
        res = res + 1
print("Frequency of 3 is" ,res)