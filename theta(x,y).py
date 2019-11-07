from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
def theta(x,y):
	return np.arctan(y/x)

x=np.arange(-3.0,3.0,0.1)
y=np.arange(-3.0,3.0,0.1)
X,Y=np.meshgrid(x,y)
Z=theta(X,Y)
fig=plt.figure()
ax=Axes3D(fig)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("θ")
ax.plot_wireframe(X,Y,Z)
plt.show()