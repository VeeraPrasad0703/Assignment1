in_str=input("Enter a String:")
if len(in_str)>1:
    str_list=list(in_str)
    str_list1=[]
    for i in str_list:
        if i not in str_list1 and i!=' ':
            str_list1.append(i)
    print("Unique letters are:",end=" ")
    for i in range(len(str_list1)):
        if i!=len(str_list1)-1:
            print(str_list1[i],end=',')
        else:
            print(str_list1)
else:
    print(in_str)
