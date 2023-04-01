import  matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import os
import cv2


n=10

fig = []
roll = 150101

for i in range(0,n):
    fig.append(plt.figure(figsize=(7.8,10.6)))
    fig[i].subplots_adjust(bottom=0.025, left=0.025, top = 0.975, right=0.975)

    r,c = 2,4
    X=[]
    for j in range(1,9):
        X.append((r,c,j))

    for ncols, nrows, plot_number in X:
        #sub = fig.add_subplot(nrows, ncols, plot_number)
        sub = plt.subplot(nrows, ncols, plot_number)
        # plt.imshow(the_array[i])

        sub.set_xticks([])
        sub.set_yticks([])

        # sub.text(0.5, 0.5, "Roll:{}\n PUST,CSE".format(roll), ha='center', va='center',
        #           size=20, alpha=.5, color="r")
        
        # Images
        # path=os.path.join("C:\Users\nazmu\OneDrive\Desktop\Balagha\seatPlan\MdNazmulHossain.jpg")
        # path=os.path("C:\Users\nazmu\OneDrive\Desktop\Balagha\seatPlan\MdNazmulHossain.jpg")

        # image=cv2.open(path)

        font = cv2.FONT_HERSHEY_SIMPLEX
  
        # org
        org = (40, 116)

        
        # fontScale
        fontScale = 0.5
        
        # Blue color in BGR
        # color = (255, 0, 0)
        color = (0, 0, 225)
        # color = (20, 30, 40)
        
        # Line thickness of 2 px
        thickness = 1
        img = cv2.imread("MdNazmulHossain.jpg", cv2.IMREAD_COLOR)
       

        img = cv2.putText(img, "Roll:{}".format(roll), org, font, 
                   fontScale, color, thickness, cv2.LINE_AA)
        org = (50, 132)
        img = cv2.putText(img, "PUST,CSE", org, font, 
                   fontScale, color, thickness, cv2.LINE_AA)
        
        # img = cv2.putText(img, "\n PUST,CSE", org, font, 
        #            fontScale, color, thickness, cv2.LINE_AA)
        
        
        sub.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))

        roll +=1
    #fig[i].tight_layout()
    #plt.show()

with PdfPages('mui.pdf') as pdf:
    for f in fig:
        #plt.figure(f.number)
        pdf.savefig(f)