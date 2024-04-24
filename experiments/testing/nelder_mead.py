import numpy as np
import copy
import matplotlib
import matplotlib.pyplot as plt

def test_booth():

    x = np.linspace(-10,10,100)
    y = np.linspace(-10,10,200)

    xx,yy = np.meshgrid(x,y)
    
    zz = booth(xx,yy)

    fig,ax = plt.subplots()
    h = plt.contourf(xx, yy, zz, norm=matplotlib.colors.LogNorm(vmin=1e-3, vmax=1e4))
    plt.axis('scaled')
    plt.colorbar()
    plt.show()

# Booth function
def booth(x,y):
    return (x + 2*y - 7)**2 + (2*x+y-5)**2


points = np.array([[-4.,-4.],[-5.,-4.],[-4.,-5.]], dtype=float) # (2,3)

iterations = 50
save_pts = []
for i in range(iterations):
    # Evaluate all points, find worst
    vals = [booth(points[j,:][0],points[j,:][1]) for j in range(points.shape[0])]
    worst_idx = np.argmax(vals)

    # compute centroid of other two, distance to third, and then reflect
    centroid = sum([p for k,p in enumerate(points) if k != worst_idx])/(points.shape[0]-1)

    # Save
    save_pts.append(copy.deepcopy(points))
    # Update
    points[worst_idx] = (centroid - points[worst_idx]) + centroid


x = np.linspace(-10,10,100)
y = np.linspace(-10,10,200)
xx,yy = np.meshgrid(x,y)
zz = booth(xx,yy)


# fig, ax = plt.subplots(10)

# for i, axi in enumerate(ax):
#     # Create the contour plot
#     contour = axi.contourf(xx, yy, zz, norm=matplotlib.colors.LogNorm(vmin=1e-3, vmax=1e4))

#     # Create the colorbar
#     cbar = fig.colorbar(contour, ax=axi)

#     # Plot points:
#     axi.scatter(save_pts[i][0][:], save_pts[i][1][:])
    # axi.scatter(save_pts[i][:,0], save_pts[i][:,1], color="red")

# plt.contourf(xx, yy, zz, norm=matplotlib.colors.LogNorm(vmin=1e-3, vmax=1e4))
# plt.scatter(save_pts[0][:,0], save_pts[0][:,1], color="blue")
# plt.scatter(save_pts[-1][:,0], save_pts[-1][:,1], color="red")

# plt.show()

import matplotlib.animation as animation

fig, ax = plt.subplots()
contour = ax.contourf(xx, yy, zz, norm=matplotlib.colors.LogNorm(vmin=1e-3, vmax=1e4))
cbar = fig.colorbar(contour, ax=ax)

def update(i):
    ax.clear()
    contour = ax.contourf(xx, yy, zz, norm=matplotlib.colors.LogNorm(vmin=1e-3, vmax=1e4))
    plt.scatter(save_pts[i][:,0], save_pts[i][:,1], color="blue")
    return ax

ani = animation.FuncAnimation(fig, update, frames=range(iterations), blit=False)
plt.show()