import numpy
import matplotlib.pyplot as plt
import scipy.misc as misc
import matplotlib.cbook as cbook

class NBAgame(object):

	def __init__(self, filename):

		self.gamearr = numpy.loadtxt(filename, dtype='string', delimiter=',', skiprows=1)
		self.ateam = filename.split('.')[1][0:3]
		self.hteam = filename.split('.')[1][3:6]
		self.date = filename.split('.')[0]
		self.date = self.date[4:6] + '/' + self.date[6:8] + '/' + self.date[0:4]

		self.a1, self.a2, self.a3, self.a4, self.a5, self.h1, self.h2, self.h3, \
		self.h4, self.h5, self.period, self.ime, self.team, self.etype, self.assist, \
		self.away, self.block, self.entered, self.home, self.left, self.num, \
		self.opponent, self.outof, self.player, self.points, self.possession, \
		self.reason, self.result, self.steal, self.kind, self.x, self.y = range(32)

	def printShots(self):

		for play in self.gamearr:
			if (play[self.etype] == 'shot'):
				print play[self.player] + ' ' + play[self.result] + ' a ' + play[self.kind]

	def printRebounds(self):

		for play in self.gamearr:
			if (play[self.etype] == 'rebound' and play[self.player] != ''):
				print play[self.player] + ' got a ' + play[self.kind] + ' ' + play[self.etype]

	def printFouls(self):

		for play in self.gamearr:
			if (play[self.etype] == 'foul'):
				print play[self.opponent] + ' committed the ' + play[self.kind] + ' foul on ' + play[self.player]

	def plotShots(self):

		self.xshots = []
		self.yshots = []
		self.shotres = []

		for play in self.gamearr:
			if (play[self.etype] == 'shot'):
				self.xshots.append(float(play[self.x]))
				self.yshots.append(float(play[self.y]))
				self.shotres.append(play[self.result])

		mades = []
		misseds = []

		for i in range(len(self.shotres)):
			if(self.shotres[i] == 'made'):
				mades.append(i)
			else:
				misseds.append(i)

		xmades = [self.xshots[i] for i in mades]
		ymades = [self.yshots[i] for i in mades]
		xmisseds = [self.xshots[j] for j in misseds]
		ymisseds = [self.yshots[j] for j in misseds]

		datafile = cbook.get_sample_data('/Users/Martin/anaconda/NBA/bucksnewcourt.jpg')
		img = misc.imread(datafile)
		plt.scatter(xmisseds, ymisseds, marker='x', c='r', zorder=2)
		plt.scatter(xmades, ymades, marker='o', c='g', zorder=1)
		plt.imshow(img, zorder=0, extent=[0.0, 50.0, 0.0, 94.0])
		plt.show()
		plt.title(self.ateam + '@' + self.hteam + ' on ' + self.date)

