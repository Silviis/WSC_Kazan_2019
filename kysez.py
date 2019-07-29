from PIL import Image
from numpy import*
temp=Image.open("C:/Users/Eetu Silvenoinen/Desktop/WorldSkills Kazan 2019/WSC_Kazan/map.bmp")
temp=temp.convert('1')      # Convert to black&white
A = array(temp)             # Creates an array, white pixels==True and black pixels==False
new_A=empty((A.shape[0],A.shape[1]),None)    #New array with same size as A
for i in range(len(A)):
    for j in range(len(A[i])):
        if A[i][j]==True:
            new_A[i][j]=1
        else:
            new_A[i][j]=0

# f= open("C:/Users/Eetu Silvenoinen/Desktop/WorldSkills Kazan 2019/WSC_Kazan/grid.txt","w+")
savetxt("C:/Users/Eetu Silvenoinen/Desktop/WorldSkills Kazan 2019/WSC_Kazan/grid.txt",around(new_A, decimals=1))
print(new_A)
