import numpy
import matplotlib.pyplot as plt
import sys
import scipy.stats
from numpy import log, sin, cos, log10, logical_and, pi

def circle(t, P):
	a = sin(2*pi * t / P)
	b = cos(2*pi * t / P)
	S = numpy.mean(a, axis=0)
	C = numpy.mean(b, axis=0)
	R = (S**2 + C**2)**0.5
	return R

Rmax = []
N = 100000
for i in range(N):
	sys.stderr.write('generating ... %d/%d\r' % (i, N))
	t = numpy.random.uniform(5, 300, 37)

	P = numpy.linspace(5, 50, 1001)
	R = circle(t.reshape((-1,1)), P.reshape((1,-1)) )
	assert R.shape == P.shape
	Rmax.append(max(R))

plt.hist(Rmax, bins=100, label='Random, uniform distributed data')
plt.ylabel('Number')
plt.xlabel('R peak value')
p = [0.95, 0.99, 0.999]
pR = scipy.stats.mstats.mquantiles(Rmax, p)
ylo, yhi = plt.ylim()
colors = ['r', 'g', 'b']
for pi, pRi, color in zip(p, pR, colors):
	plt.vlines(pRi, ylo, yhi, linestyles=['dashed']*3, color=color, 
		label='%s%% confidence limit' % (pi*100.))
plt.legend(loc='upper right', prop=dict(size=12))
plt.savefig('gendata.pdf', bbox_inches='tight')
plt.savefig('gendata.png', bbox_inches='tight')
plt.close()

