from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
def Hemisphere(x,y):
	return np.sqrt(1-x**2-y**2)

x=np.arange(-1.0,1.0,0.001)
y=np.arange(-1.0,1.0,0.001)
X,Y=np.meshgrid(x,y)
Z=Hemisphere(X,Y)
fig=plt.figure()
ax=Axes3D(fig)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.plot_wireframe(X,Y,Z)
plt.show()
