import numpy as np
import matplotlib.pyplot as plt


def Newton( f, df, x0, *args ):

	x = x0
	cutoff = 1e-5
	delta = cutoff + 1.0
	
	while np.fabs(delta) > cutoff:
		delta = f(x, *args)/df(x, *args)
		x = x - delta

	return x

def sq_well( z, a, V ):
	return np.sqrt( a*a*V/2.0 - z*z ) - z*np.tan(z)

def d_sqwell( z, a, V ):
	return -z/np.sqrt(a*a*V/2. - z*z) - z/np.cos(z)/np.cos(z) - np.tan(z)

if __name__=='__main__':

	a = 5.0
	V = 5.5

	roots = []
	x0 = [1.5, 4.0, 7.0]

	for i in x0:
		s = Newton( sq_well, d_sqwell, i, a, V )
		roots.append(s)
		print s

	z = np.linspace( 0,10,500 )
	fix, ax = plt.subplots()

	ax.plot( z,  sq_well( z, a, V ), ls='', marker='o', color='b' )
	ax.plot( z, np.zeros(500), color='grey' )
	ax.plot( roots, [0,0,0], ls='', marker='x', ms=10, mew=3, color='r', label='roots' )

	ax.set_ylim([-10,10])
	ax.set_xlabel(r'$z$', fontsize=16 )
	ax.set_ylabel(r'$\sqrt{\frac{a^2V_0}{2} - z^2} - z\,\tan{z}$', fontsize=16)
	ax.legend(loc='best')

	plt.show()
