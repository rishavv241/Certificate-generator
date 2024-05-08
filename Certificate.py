import cv2
L = []
x=str(input('Enter name for whom you to want to Generate Certificate:--'))
L.append(x)


for index, name in enumerate(L):
    
    tempelate=cv2.imread('c.jpg')
    cv2.putText(tempelate,name,(1350,1447),cv2.FONT_HERSHEY_COMPLEX,4.5,(100,75,79.6),1,cv2.LINE_AA)
    cv2.imwrite(f'/Users/rishav/Desktop/PYTHON PROJECT/Generated certificates/{name}.jpg',tempelate)
    
    print('Processing Certificate... {}/{}'.format(index+1,len(L)))


                         

