import  matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

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
        sub.set_xticks([])
        sub.set_yticks([])

        sub.text(0.5, 0.5, "Roll:{}\n PUST,CSE".format(roll), ha='center', va='center',
                  size=20, alpha=.5, color="r")

        roll +=1
    #fig[i].tight_layout()
    #plt.show()

with PdfPages('mui.pdf') as pdf:
    for f in fig:
        #plt.figure(f.number)
        pdf.savefig(f)