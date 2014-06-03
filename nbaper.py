import numpy
import matplotlib.pyplot as plt

class NBAper(object):

	def __init__(self, filename):
		self.perdata = numpy.loadtxt(filename, dtype='string', delimiter=',', skiprows=1)

		self.rk, self.player, self.position, self.age, self.team, self.g_played, \
			self.min_played, self.PER, self.TSpercent, self.effFG, self.FTar, self.threeptar, \
			self.ORBpercent, self.DRBpercent, self.TRBpercent, self.Apercent, self.STLpercent, \
			self.BLKpercent, self.TOpercent, self.USGpercent, self.OFFrating, self.DEFrating, \
			self.OWS, self.DWS, self.WS, self.WSper48 = range(26)

	def makePERdict(self):

		self.PERdict = {}

		for line in self.perdata:
			if(line[self.PER] != '' and line[self.player] != ''):
				if(float(line[self.g_played]) >= 20 or float(line[self.min_played]) >= 500.):
					if(line[self.player] not in self.PERdict.keys()):
						self.PERdict[str(line[self.player])] = [float(line[self.PER])]
					else:
						self.PERdict[str(line[self.player])].append(float(line[self.PER]))

	def PERPlayerAvg(self):

		avgs = []

		for key in self.PERdict:
			if(len(self.PERdict[key]) >= 4):
				avgs.append(numpy.average(self.PERdict[key]))

		self.PERavgs = numpy.array(avgs)

	def makePERhist(self):

		plt.hist(self.PERavgs, bins=50, alpha=0.6, color='black')
		plt.xlabel('PER')
		plt.ylabel('Number of Players')
		plt.title('PER Histogram')
		plt.show()

