import cmd
import numpy as np
import matplotlib.pyplot as plt

from scipy.interpolate import spline
from time import time


class HelloWorld(cmd.Cmd):
	def __init__(self):
		cmd.Cmd.__init__(self)
		self.data = []
		self.start = time()
	
	
	def emptyline(self):
		self.data.append(time()-self.start)

	
	def do_report(self, line):
		# Initialize Minute hand and data index
		i, j = 1, 0

		# Spikes per minute
		t = []
		
		spikes = 0
		while (j < len(self.data)):

			# If time stamp under current minute window
			if self.data[j] < i*60:x
				spikes += 1
				j += 1

			# slide window to next frame
			else:
				t.append(spikes)
				spikes = 0
				i += 1

		x, y = self.getSmoothData(t)
		self.getPlot(x, y)
		plt.show()
		return True


	def getPlot(self, x, y):
		# Insert data
		plt.plot(x, y)
		
		# Set Labels
		plt.xlabel('Time (min)')
		plt.ylabel('Distraction Spikes (n/min)')
		
		# Get axes and set background color
		ax = plt.gca()
		ax.set_fc('k')


	def getSmoothData(self, y):
		# Transfer data to numpy array
		x_smooth = np.linspace(0, len(y), 100)
		y_smooth = spline(np.arange(len(y)), y, x_smooth)

		return (x_smooth, y_smooth)

	
	def do_EOF(self, line):
		return True


if __name__ == '__main__':
	HelloWorld().cmdloop()
