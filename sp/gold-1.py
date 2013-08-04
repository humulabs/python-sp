import numpy
import pylab
from sp import mls
from sp import filter
nbits = 9
m = mls.mls(nbits)
pylab.figure()
pylab.title('%d bit M-Sequence Periodic Autocorrelation' % nbits)
m = numpy.where(m, 1.0, -1.0)
pylab.plot((numpy.roll(filter.ccorr(m, m).real, 2**nbits/2 - 1)))
pylab.xlim(0, len(m))
pylab.show()