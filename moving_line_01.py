import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update_line(num, data, line):
	num = num + 0.01
	new_data = data + num / 1000.0
	line.set_data(new_data)
	plt.draw()
	return line,

fig1 = plt.figure()

mat = [[0.1, 0.2, 0.3], [0.3, 0.4, 0.3]]
line_data = np.random.rand(2, len(mat[0]))
line_data[...,:] = mat

l, = plt.plot([], [], 'go-')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel('x')
plt.title('test')
line_ani = animation.FuncAnimation(fig1, update_line, 100, fargs=(line_data, l), interval=50, blit=True)
	
#line_ani.save('lines.mp4')



#fig2 = plt.figure()

#x = np.arange(-9, 10)
#y = np.arange(-9, 10).reshape(-1, 1)
#base = np.hypot(x, y)
#ims = []
#for add in np.arange(15):
#	ims.append((plt.pcolor(x, y, base + add, norm=plt.Normalize(0, 30)),))

#im_ani = animation.ArtistAnimation(fig2, ims, interval=50, repeat_delay=3000,
#	blit=True)
#im_ani.save('im.mp4', metadata={'artist':'Guido'})

plt.show()