def transpose(matrix):
    new_m=[]
    temp=[]
    for i in range(len(matrix)):
        temp=[]
        for j in range(len(matrix[i])):
            temp.append(matrix[j][i])
        new_m.append(temp)
    return new_m 
a=[[1,2,3],
  [4,5,6],
  [7,8,9]]
b=transpose(a)
for i in range(len(b)):
    print()
    for j in range(len(b[i])):
        print(b[i][j],end=" ")