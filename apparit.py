str=input("Ecrire un mot !!")

n_str=list(str)

new_list=[]

for j in n_str:

    if j not in new_list:

        new_list.append(j)

        count=0

        for i in range(len(newstr)):

            if j==n_str[i]:

                count+=1

        print("{},{}".format(j,count))