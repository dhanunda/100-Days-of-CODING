#Transpose a matrix
r=int(input("Enter number of rows"))
c=int(input("Enter number of coloums"))
m = [[int(input()) for x in range (c)] for y in range(r)]
print("beforeTranspose")
print(m)
transpose = [[row[i] for row in m] for i in range(c)]
print("after Transpose")
print(transpose)
