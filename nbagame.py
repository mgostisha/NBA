import numpy
import math
import matplotlib.pyplot as plt
import scipy.misc as misc
import matplotlib.cbook as cbook
import matplotlib.colors as colors

class NBAgame(object):

	def __init__(self, filename):

		self.gamearr = numpy.loadtxt(filename, dtype='string', delimiter=',', skiprows=1)
		self.ateam = filename.split('.')[1][0:3]
		self.hteam = filename.split('.')[1][3:6]
		self.date = filename.split('.')[0]
		self.date = self.date[4:6] + '/' + self.date[6:8] + '/' + self.date[0:4]

		self.a1, self.a2, self.a3, self.a4, self.a5, self.h1, self.h2, self.h3, \
		self.h4, self.h5, self.period, self.time, self.team, self.etype, self.assist, \
		self.away, self.block, self.entered, self.home, self.left, self.num, \
		self.opponent, self.outof, self.player, self.points, self.possession, \
		self.reason, self.result, self.steal, self.kind, self.x, self.y = range(32)

	def printShots(self):
		count = 0

		for play in self.gamearr:
			if (play[self.etype] == 'shot'):
				print play[self.player] + ' ' + play[self.result] + ' a ' + play[self.kind]
				count += 1

		print count

	def printRebounds(self):

		for play in self.gamearr:
			if (play[self.etype] == 'rebound' and play[self.player] != ''):
				print play[self.player] + ' got a ' + play[self.kind] + ' ' + play[self.etype]

	def printFouls(self):

		for play in self.gamearr:
			if (play[self.etype] == 'foul'):
				print play[self.opponent] + ' committed the ' + play[self.kind] + ' foul on ' + play[self.player]

	def plotAllShots(self):

		self.xshots = []
		self.yshots = []
		self.shotres = []

		halfs = 0

		for play in self.gamearr:
			if (play[self.etype] == 'shot' and float(play[self.y]) <= 47.0):
				self.xshots.append(float(play[self.x]))
				self.yshots.append(float(play[self.y]))
				self.shotres.append(play[self.result])
			elif (play[self.etype] == 'shot' and float(play[self.y]) >= 47.0):
				halfs += 1

		print 'Shots from beyond halfcourt: ' + str(halfs)

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

		courtfn = '/Users/Martin/anaconda/NBA/halfcourts/' + (self.hteam).lower() + '_halfcourt.jpg'

		datafile = cbook.get_sample_data(courtfn)
		img = misc.imread(datafile)
		miss = plt.scatter(xmisseds, ymisseds, marker='x', c='r', s=40, zorder=2)
		make = plt.scatter(xmades, ymades, marker='o', c='g', s=100, zorder=1)
		plt.imshow(img, zorder=0, extent=[0.0, 50.0, 0.0, 47.0])
		plt.legend((make, miss), ('Make', 'Miss'), scatterpoints=1, loc='upper right', ncol=1, fontsize=10)
		plt.xticks([])
		plt.yticks([])
		plt.show()
		plt.title(self.ateam + '@' + self.hteam + ' on ' + self.date)

		print len(xmades)+len(xmisseds)

	def plotTeamShots(self, teamcode):

		self.xshotsteam = []
		self.yshotsteam = []
		self.shotresteam = []

		halfs = 0

		for play in self.gamearr:
			if (play[self.etype] == 'shot' and float(play[self.y]) <= 47.0 and play[self.team] == teamcode):
				self.xshotsteam.append(float(play[self.x]))
				self.yshotsteam.append(float(play[self.y]))
				self.shotresteam.append(play[self.result])
			elif (play[self.etype] == 'shot' and float(play[self.y]) >= 47.0 and play[self.team] == teamcode):
				halfs += 1

		print 'Shots from ' + teamcode + ' beyond halfcourt: ' + str(halfs)

		mades = []
		misseds = []

		for i in range(len(self.shotresteam)):
			if(self.shotresteam[i] == 'made'):
				mades.append(i)
			else:
				misseds.append(i)

		xmades = [self.xshotsteam[i] for i in mades]
		ymades = [self.yshotsteam[i] for i in mades]
		xmisseds = [self.xshotsteam[j] for j in misseds]
		ymisseds = [self.yshotsteam[j] for j in misseds]

		courtfn = '/Users/Martin/anaconda/NBA/halfcourts/' + (self.hteam).lower() + '_halfcourt.jpg'

		datafile = cbook.get_sample_data(courtfn)
		img = misc.imread(datafile)
		miss = plt.scatter(xmisseds, ymisseds, marker='x', c='r', s=40, zorder=2)
		make = plt.scatter(xmades, ymades, marker='o', c='g', s=100, zorder=1)
		plt.imshow(img, zorder=0, extent=[0.0, 50.0, 0.0, 47.0])
		plt.legend((make, miss), ('Make', 'Miss'), scatterpoints=1, loc='upper right', ncol=1, fontsize=10)
		plt.xticks([])
		plt.yticks([])
		plt.show()
		plt.title(teamcode + ' - ' + self.ateam + '@' + self.hteam + ' on ' + self.date)

		print len(xmades)+len(xmisseds)

	def plotPlayerShots(self, shooter):

		self.xshotsplayer = []
		self.yshotsplayer = []
		self.shotresplayer = []

		halfs = 0

		for play in self.gamearr:
			if (play[self.etype] == 'shot' and float(play[self.y]) <= 47.0 and play[self.player] == shooter):
				self.xshotsplayer.append(float(play[self.x]))
				self.yshotsplayer.append(float(play[self.y]))
				self.shotresplayer.append(play[self.result])
			elif (play[self.etype] == 'shot' and float(play[self.y]) >= 47.0 and play[self.player] == shooter):
				halfs += 1

		print 'Shots from ' + shooter + ' beyond halfcourt: ' + str(halfs)

		mades = []
		misseds = []

		for i in range(len(self.shotresplayer)):
			if(self.shotresplayer[i] == 'made'):
				mades.append(i)
			else:
				misseds.append(i)

		xmades = [self.xshotsplayer[i] for i in mades]
		ymades = [self.yshotsplayer[i] for i in mades]
		xmisseds = [self.xshotsplayer[j] for j in misseds]
		ymisseds = [self.yshotsplayer[j] for j in misseds]

		courtfn = '/Users/Martin/anaconda/NBA/halfcourts/' + (self.hteam).lower() + '_halfcourt.jpg'

		datafile = cbook.get_sample_data(courtfn)
		img = misc.imread(datafile)
		miss = plt.scatter(xmisseds, ymisseds, marker='x', c='r', s=40, zorder=2)
		make = plt.scatter(xmades, ymades, marker='o', c='g', s=100, zorder=1)
		plt.imshow(img, zorder=0, extent=[0.0, 50.0, 0.0, 47.0])
		plt.legend((make, miss), ('Make', 'Miss'), scatterpoints=1, loc='upper right', ncol=1, fontsize=10)
		plt.xticks([])
		plt.yticks([])
		plt.show()
		plt.title(shooter + ' - ' + self.ateam + '@' + self.hteam + ' on ' + self.date)

		print len(xmades)+len(xmisseds)

	def shotHistogram(self):

		shots = []
		madeshots = []
		missshots = []
		binwidths = range(0, 51, 2)

		for play in self.gamearr:
			r = 0
			if (play[self.etype] == 'shot'):
				x = math.fabs(25.0 - float(play[self.x]))
				y = math.fabs(5.25 - float(play[self.y]))
				r = numpy.sqrt(x**2 + y**2)
				shots.append(r)

				if (play[self.result] == 'made'):
					madeshots.append(r)
				else:
					missshots.append(r)

		#plt.hist(shots, bins=binwidths, histtype='step', color='b', label='Total Shots')
		#plt.hist(madeshots, bins=binwidths, histtype='stepfilled', color='g', alpha=0.5, label='Shots Made')
		plt.hist([madeshots, missshots], bins=binwidths, histtype='stepfilled', stacked=True,
			label=('Shots Made', 'Shots Missed'), color=('#75C34B', '#C45B4F'))
		plt.title('Shot Distances')
		plt.xlabel('Shot Distance from Basket')
		plt.ylabel('Total Shots')
		plt.legend()

	def shotHistogram2D(self):

		xshots = []
		yshots = []
		xbinwidths = range(0,51,2)
		ybinwidths = range(0,47,2)

		for play in self.gamearr:
			if(play[self.etype] == 'shot'):
				xshots.append(float(play[self.x]))
				yshots.append(float(play[self.y]))

		plt.hist2d(xshots, yshots, bins=[xbinwidths,ybinwidths], cmax=20)
		plt.colorbar()

