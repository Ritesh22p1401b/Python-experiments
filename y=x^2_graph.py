


import matplotlib.pyplot as plt
import numpy as np

x_axis=np.linspace(-50,50,400)
y_axis=[x*x for x in x_axis]
plt.plot(x_axis,y_axis,label='y=x^2')
plt.legend(loc='lower right')
plt.grid()
plt.title('Parabola Curve Graph')
plt.xlabel('x-axis',fontname='serif',fontsize='14')
plt.ylabel('y-axis',fontname='serif',fontsize='14')
plt.show()






'''import matplotlib.pyplot as plt
import numpy as np

y_axis=np.linspace(-50,50,400)
x_axis=[y*y for y in y_axis]
plt.plot(x_axis,y_axis,label='x=y^2')
plt.legend()
plt.title('Parabola Curve Graph')
plt.xlabel('x-axis',fontname='serif',fontsize='14')
plt.ylabel('y-label',fontname='serif',fontsize='14')
plt.show() '''





