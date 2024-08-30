#Dynamic Matrix Rotation
def tranpose_matrix(matrix):
    n=len(matrix)  #n*n matrix
    for i in range(n):
        for j in range(i+1,n):
            temp=matrix[i][j]
            matrix[i][j]=matrix[j][i]
            matrix[j][i]=temp
def rotate_matrix(matrix,degree):
    if(degree ==90):  #90 degree transpose then reverse elements of each row
        tranpose_matrix(matrix)  
        for row in matrix:
            row.reverse()
    elif(degree ==180): #180 degree reverse order or rows then reverse elements of each row
        matrix.reverse()
        for row in matrix:
            row.reverse()
    elif(degree ==270): #270 degree reverse elements of each row then transpose
        for row in matrix:
            row.reverse()
        tranpose_matrix(matrix)
    print("\nAfter Rotating:")
    for row in matrix:
        print(row)
    return

n=int(input("Enter Size of Matrix: "))
matrix = [[0 for x in range(n)] for y in range(n)]  
#Initializes Matrix with zeroes
#for y in range(n) iterates over no. of rows 
#for x in range(n) iterates over no. of columns
for i in range(n):
    for j in range(n):
        matrix[i][j] = int(input(f"Enter element [{i}][{j}]: "))  

print(f"{n}*{n} Matrix:")
for row in matrix:
    print(row)
degree=int(input("Enter degree of rotation:"))
rotate_matrix(matrix,degree)