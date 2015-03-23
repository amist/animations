import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig1 = plt.figure()
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel('x')
plt.title('test')

def update_line(num, data, line):
	num = num + 0.01
	new_data = data + num / 1000.0
	line.set_data(new_data)
	#plt.draw()
	return line,

mat = [[0.1, 0.2, 0.3], [0.3, 0.4, 0.3]]
line_data = np.random.rand(2, len(mat[0]))
line_data[...,:] = mat

l, = plt.plot([], [], 'go-')
#line_ani = animation.FuncAnimation(fig1, update_line, 100, fargs=(line_data, l), interval=50, blit=True)

def update_path(i, data, path):
	path.set_data(data[...,:i])
	#plt.draw()
	return path,

frames = 100
path = [[float(x + 1) / frames for x in range(frames)], [(float(x + 1) / frames) ** 2 for x in range(frames)]]
path_data = np.random.rand(2, len(path[0]))
path_data[...,:] = path
p, = plt.plot([], [], 'r.')
#path_ani = animation.FuncAnimation(fig1, update_path, 100, fargs=(path_data, p), interval=10, blit=True)

def update_both(i, line_data, line, path_data, path):
	i = i + 0.01
	new_data = line_data + i / 1000.0
	line.set_data(new_data)
	path.set_data(path_data[...,:i])
	filename = '_tmp%03d.png'%i
	fig1.savefig(filename)
	return line, path

both_ani = animation.FuncAnimation(fig1, update_both, frames, fargs=(line_data, l, path_data, p), interval=10, blit=True)
both_ani.save('lines.mp4', fps=25, bitrate=150)


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

#plt.show()