import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig1 = plt.figure()
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel('x')
plt.title('test')

lines = [[0.1, 0.1, 0.9], [0.1, 0.9, 0.1]]
line_data = np.random.rand(2, len(lines[0]))
line_data[...,:] = lines
l, = plt.plot([], [], 'go-')

bez1_data = np.random.rand(2, 2)
bez1_data[...,:] = line_data[...,:2]
b1, = plt.plot([], [], 'b-')

frames = 300
path = [[float(x + 1) / frames for x in range(frames)], [(float(x + 1) / frames) ** 2 for x in range(frames)]]
path_data = np.random.rand(2, len(path[0]))
path_data[...,:] = path
p, = plt.plot([], [], 'r.')

def update_all(i):
	line = l
	bez1 = b1
	path = p
	#print path_data[..., i]
	i = i + 0.01
	t = i / frames
	nx = (1 - t) * line_data[0, 0] + t * line_data[0, 1]
	ny = (1 - t) * line_data[1, 0] + t * line_data[1, 1]
	bez1_data[..., 0] = [nx, ny]
	nx = (1 - t) * line_data[0, 1] + t * line_data[0, 2]
	ny = (1 - t) * line_data[1, 1] + t * line_data[1, 2]
	bez1_data[..., 1] = [nx, ny]
	nx = (1 - t) * bez1_data[0, 0] + t * bez1_data[0, 1]
	ny = (1 - t) * bez1_data[1, 0] + t * bez1_data[1, 1]
	path_data[..., i] = [nx, ny]
	line.set_data(line_data)
	bez1.set_data(bez1_data)
	path.set_data(path_data[...,:i])
	#filename = '_tmp%03d.png'%i
	#fig1.savefig(filename)
	#plt.draw()
	return line, bez1, path

both_ani = animation.FuncAnimation(fig1, update_all, frames, interval=10, blit=True, repeat_delay=1000)
#both_ani.save('bezier_2.mp4', fps=25, bitrate=150)

#im_ani.save('im.mp4', metadata={'artist':'Guido'})

plt.show()