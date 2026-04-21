import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,3,4,5])
y=np.array([6,4,1,3,8])

plt.plot(x,y,marker="+",linestyle="--",color="b")
plt.title("Sample Plot")

plt.savefig("plot.pdf",format="pdf")
plt.show()
