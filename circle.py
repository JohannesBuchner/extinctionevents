import numpy
import matplotlib.pyplot as plt
import sys
from numpy import log, sin, cos, log10, logical_and, pi

data = numpy.loadtxt(sys.argv[1])
t = data[:,0]
err = data[:,1]

def circle(t, P):
	a = sin(2*pi * t / P)
	b = cos(2*pi * t / P)
	S = numpy.mean(a)
	C = numpy.mean(b)
	R = (S**2 + C**2)**0.5
	return R

P = numpy.linspace(5, 50, 1000)
R = [circle(t, Pi) for Pi in P]
plt.plot(P, R)
plt.savefig('circle.pdf', bbox_inches='tight')
plt.close()

plt.figure(figsize=(4,4))
P = 18.4
a = sin(2*pi * t / P)
b = cos(2*pi * t / P)
S = numpy.mean(a)
C = numpy.mean(b)
R = (S**2 + C**2)**0.5
plt.plot(a, b, 's ')
plt.plot(S, C, '* ')
plt.plot([0, S], [0, C], '-')
plt.text(0, 0, '%.3f' % R)
#plt.plot(0.25, '-')
plt.savefig('circle_circle.pdf', bbox_inches='tight')
plt.close()

