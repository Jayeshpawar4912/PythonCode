import matplotlib.pyplot as plt
plt.plot([1,2,3],[2,5,3])
plt.show()
>>> from matplotlib import pyplot as plt
>>> plt.plot([1,2,3,4,5],[1,4,9,16,25],'ro'
... )
[<matplotlib.lines.Line2D object at 0x000001760422BA10>]
>>> plt.axis([0,6,0,20])
(np.float64(0.0), np.float64(6.0), np.float64(0.0), np.float64(20.0))
>>> plt.show()
>>> names=['Abhishek','Krishna','Jayesh']
>>> marks=[87,54,98]
>>> plt.figure(figsize=(9,3))
<Figure size 900x300 with 0 Axes>
>>> plt.subplot(131)
<Axes: >
>>> plt.bar(names,marks)
<BarContainer object of 3 artists>
>>> plt.subplot(132)
<Axes: >
>>> plt.scatter(names,marks)
<matplotlib.collections.PathCollection object at 0x0000017602EF11D0>
>>> plt.subplot(133)
<Axes: >
>>> plt.plot(names,marks)
[<matplotlib.lines.Line2D object at 0x00000176054184D0>]
>>> plt.suptitle('Categorical Plotting')
Text(0.5, 0.98, 'Categorical Plotting')
>>> plt.show()



 from matplotlib import pyplot as plt
>>> from matplotlib import style
>>> style.use('ggplot')
>>> x=[16,8,10]
>>> y=[8,16,6]
>>> x2=[8,15,11]
>>> y2=[6,15,7]
>>> plt.plot(x,y,'r',label='line one',linewidth=5)
[<matplotlib.lines.Line2D object at 0x000001B5C7277090>]
>>> plt.plot(x2,y2,'m',label='line two',linewidth=5)
[<matplotlib.lines.Line2D object at 0x000001B5C9205010>]
>>> plt.title('Epic info')
Text(0.5, 1.0, 'Epic info')
>>> fig=plt.figure()
>>> plt.xlabel('X axis')
Text(0.5, 0, 'X axis')
>>> plt.ylabel('Y axis')
Text(0, 0.5, 'Y axis')
>>> plt.legend()
<stdin>:1: UserWarning: No artists with labels found to put in legend.  Note that artists whose label start with an underscore are ignored when legend() is called with no argument.
<matplotlib.legend.Legend object at 0x000001B5C7D61150>
>>> plt.grid(True,color='k')
>>> plt.show()