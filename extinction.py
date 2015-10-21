import numpy
import scipy.stats
import json
import matplotlib.pyplot as plt
import sys
from  pymultinest.solve import solve

data = numpy.array(zip(
	numpy.arange(15, 255, 20).tolist() + numpy.random.uniform(15, 255, size=5).tolist(), 
	numpy.zeros(shape=1000) + 0.1
	))
numpy.savetxt('extinction_testdata.txt', data)

data = numpy.loadtxt(sys.argv[1])
prefix = sys.argv[1]
samples = numpy.array([numpy.random.normal(t, tdelta, size=1000) for t, tdelta in data])

def transform(cube):
	params = numpy.copy(cube)
	params[0] = 10**(cube[0] * 2 - 2) # strength of signal (log-uniform)
	params[1] = 10**(cube[1] * 3 - 1) # width of signal (log-uniform, 0.1-10Myr)
	params[2] = 10**(cube[2] * (0.523) + 1.2) # period (log-uniform, 15-50Myrs)
	params[3] = cube[3] # phase/position of signal (uniform, 0-1)
	return params
parameter_names = ['strength', 'width', 'period', 'phase']


def model(x, s, w, p, phase):
	xwrapped = numpy.fmod(x / p - phase + 2, 1)
	return (1 - s) + s * scipy.stats.norm.pdf(xwrapped, 0.5, w / p)

def loglikelihood(params):
	s, w, p, phase = params
	prob = model(samples, s, w, p, phase)
	loglike = numpy.log(prob.mean(axis=1) + 1e-300).sum()
	print 'Like: %.1f' % loglike, params
	return loglike

sol = solve(loglikelihood, transform, n_dims=len(parameter_names),
	outputfiles_basename=prefix + '_gauss')
json.dump(parameter_names, open(prefix + '_gaussparams.json', 'w'))
print 'Evidence log Z = %.1f +- %.1f' % (sol['logZ'], sol['logZerr'])


x = numpy.linspace(5, 300, 4000)
plt.subplot(2, 1, 1)
plt.errorbar(x=data[:,0], xerr=data[:,1], y=numpy.random.normal(size=len(data)) + 0.5, linestyle=' ')
plt.xlim(x[0], x[-1])
plt.subplot(2, 1, 2)
plt.xlim(x[0], x[-1])
from posterierr.quantileshades import Shade
shade = Shade(x)
for s, w, p, phase in sol['samples'][:40]:
	s = 1
	y = model(x, s, w, p, phase)
	plt.plot(x, y, color='k', alpha=0.3)
	shade.add(y)
shade.line()
#shade.shade()
plt.savefig(prefix + '_gauss_predict.pdf', bbox_inches='tight')
plt.close()


