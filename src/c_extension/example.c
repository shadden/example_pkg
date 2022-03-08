#include <math.h>

void standard_map(double* theta, double* p, double K){
	*p = *p + K * sin( *theta);
	*theta = *theta + *p;
}
  
