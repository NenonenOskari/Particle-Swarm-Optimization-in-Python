import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx 
from pyswarms.utils.plotters.formatters import Mesher, Designer
from pyswarms.utils.plotters import plot_cost_history, plot_contour, plot_surface
import matplotlib.pyplot as plt
#from IPython.display import Image

# This code uses pyswarms -library for the PSO, the library can be 
# installed as pyswarms or found here:
# https://github.com/ljvmiranda921/pyswarms

#Hyperparameters (cognitive, social and inertia weight) 
opt = {"c1":0.5, "c2":0.3, "w":0.9}

#The optimizer for sphere function:
optimizer = ps.single.GlobalBestPSO(n_particles=50,dimensions=2,options=opt)
optimizer.optimize(fx.sphere, iters=100)

#history of particle positions for animation
hist = optimizer.pos_history

#This can plot the cost history, not needed for the assignment:
#plot_cost_history(optimizer.cost_history)

#Mesh for the plot:
m = Mesher(func=fx.sphere, limits=[(-1,1),(-1,1)])

#This can be used for designing the animation 
#but the defaults are enough for this task
#d = Designer(limits=[(-1,1),(-1,1),(-0.1,1)],
 #           label=["x-axis","y-axis","z-azis"])

animation = plot_contour(pos_history=hist, mesher=m,mark=(0,0))

#3D version for fun:
#pos_his_3D = m.compute_history_3d(hist)
#            anim3D = plot_surface(pos_history=pos_his_3D,
#            mesher=m, mark=(0,0,0))

#Shows the sphere animation, the code continues after the animation is closed:
plt.show()

#Same for a more interesting function Schaffer N.2 Objective function
optimizer2 = ps.single.GlobalBestPSO(n_particles=50,dimensions=2,options=opt)
optimizer2.optimize(fx.schaffer2, iters=100)

hist2 = optimizer2.pos_history

m2 = Mesher(func=fx.schaffer2, limits=[(-1,1),(-1,1)])

animation2 = plot_contour(pos_history=hist2, mesher=m2,mark=(0,0))

plt.show()
