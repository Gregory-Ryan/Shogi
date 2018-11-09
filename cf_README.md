# Complex Arithmetic
## cf.add(z,z1)
Returns the addition of two complex numbers in the form of (Re,Im).
The input is two tuples or strings(x + iy) and it returns a tuple.
## cf.div(z,z1)
Returns the a complex number divided by complex number in the form of (Re,Im). 
The input is two tuples or strings(x + iy) and it returns a tuple.
## cf.multi(z,z1)
Returns the product of two complex numbers in the form of (Re,Im). 
The input is two tuples or strings(x + iy) and it returns a tuple.
## cf.neg(z)
Returns the negative of a complex number in the form of -x + -yi.
The input is a tuple or a string(x + iy) and it returns a tuple.
## cf.power(z,p)
Returns the complex number to the power of complex number in the form of (Re,Im). (z ** p)
The input is two tuples or strings(x + iy) and it returns a tuple.
## cf.sqr(z)
Returns the square of a complex number in the form of (Re,Im). 
The input is a tuple or a string(x + iy) and it returns a tuple.
## cf.sqrt(z)
Returns the square root of a complex number in the form of (Re,Im). 
The input is a tuple or a string(x + iy) and it returns a tuple.
## cf.subt(z,z1)
Returns the subtraction of two complex numbers in the form of (Re,Im). (z - z1)
The input is two tuples or strings(x + iy) and it returns a tuple.

# Complex Analysis
## cf.arg(z)
Returns the argument of a complex number in radians. 
The input is a tuple or a string(x + iy) and it returns a Decimal.
## cf.Arg(z)
Returns the principal argument of a complex number in radians. 
The input is a tuple or a string(x + iy) and it returns a Decimal.
## cf.conj(x,y)
Takes the Real(x) and Imaginary(y) parts of a complex number and puts it in the form of x + -yi. 
The input is two Decimals and it returns a tuple.
## cf.conj_s(x,y)
Takes the Real(x) and Imaginary(y) parts of a complex number and puts it in the form of x + -yi. 
The input is two Decimals and it returns a string(x + iy).
## cf.eul(r,t)
Takes a input in polar form (radius,angle(radians)) and returns a complex number in the form of (Re,Im).
The input is two Decimals and it returns a tuple.
## cf.eul_c(r,z)
Takes a input in the form of (r,z) and returns a complex number in the form of (Re,Im). (r*e**(z*i))
The input is two tuples or strings(x + iy) and it returns a tuple.
## cf.I(x,y)
Takes the Real(x) and Imaginary(y) parts of a complex number and puts it in the form of (Re,Im). 
The input is two Decimals and it returns a tuple.
## cf.Im(z)
Returns the Imaginary part of a complex number.
The input is a tuple or a string(x + iy) and it returns a Decimal.
## cf.Im_s(z)
Returns the Imaginary part of a complex number.
The input is a string(x + iy) and it returns a Decimal.
## cf.I_s(x,y)
Takes the Real(x) and Imaginary(y) parts of a complex number and puts it in the form of x + yi. 
The input is two Decimals and it returns a string(x + iy).
## cf.log(z)
Returns the logarithm of a complex number in the form of (Re,Im). 
The input is a tuple or a string(x + iy) and it returns a tuple.
## cf.Log(z)
Returns the principal logarithm of a complex number in the form of (Re,Im). 
The input is a tuple or a string(x + iy) and it returns a tuple.
## cf.mod(z)
Returns the norm/magnitude/modulus of a complex number. 
The input is a tuple or a string(x + iy) and it returns a Decimal.
## cf.Re(z)
Returns the Real part of a complex number.
The input is a tuple or a string(x + iy) and it returns a Decimal.
## cf.Re_s(z)
Returns the Real part of a complex number.
The input is a string(x + iy) and it returns a Decimal.

# Complex Trigonometry
## cf.cos(z)
Returns the cosine of a complex number in the form of (Re,Im). 
The input is a tuple or a string(x + iy) and it returns a tuple.
## cf.cosh(z)
Returns the hyperbolic cosine of a complex number in the form of (Re,Im). 
The input is a tuple or a string(x + iy) and it returns a tuple.
## cf.cot(z)
Returns the cotangent of a complex number in the form of (Re,Im). 
The input is a tuple or a string(x + iy) and it returns a tuple.
## cf.coth(z)
Returns the hyperbolic cotangent of a complex number in the form of (Re,Im). 
The input is a tuple or a string(x + iy) and it returns a tuple.
## cf.csc(z)
Returns the cosecant of a complex number in the form of (Re,Im). 
The input is a tuple or a string(x + iy) and it returns a tuple.
## cf.csch(z)
Returns the hyperbolic cosecant of a complex number in the form of (Re,Im). 
The input is a tuple or a string(x + iy) and it returns a tuple.
## cf.sec(z)
Returns the secant of a complex number in the form of (Re,Im). 
The input is a tuple or a string(x + iy) and it returns a tuple.
## cf.sech(z)
Returns the hyperbolic secant of a complex number in the form of (Re,Im). 
The input is a tuple or a string(x + iy) and it returns a tuple.
## cf.sin(z)
Returns the sine of a complex number in the form of (Re,Im). 
The input is a tuple or a string(x + iy) and it returns a tuple.
## cf.sinh(z)
Returns the hyperbolic sine of a complex number in the form of (Re,Im). 
The input is a tuple or a string(x + iy) and it returns a tuple.
## cf.tan(z)
Returns the tangent of a complex number in the form of (Re,Im). 
The input is a tuple or a string(x + iy) and it returns a tuple.
## cf.tanh(z)
Returns the hyperbolic tangent of a complex number in the form of (Re,Im). 
The input is a tuple or a string(x + iy) and it returns a tuple.

# Analytic Number Theory
## cf.B(n)
Returns the bernoulli numbers in form of (Re,Im). 
The input is a tuple or a string(x + iy) and it returns a tuple.
## cf.beta(z)
Returns the Dirichlet Beta function in form of (Re,Im).
The input is a tuple or a string(x + iy) and it returns a tuple.
## cf.divisors(n)
Returns the divisors of a number.
The input is a positive integer and it returns list.
## cf.div_sig(k,n)
Returns the Divisor function of a number.
The input are positive integers and it returns integer.
## cf.eta(z)
Returns the Dirichlet Eta function of a complex number in the form of (Re,Im). 
The input is a tuple or a string(x + iy) and it returns a tuple.
## cf.euler_c
The Euler-Mascheroni constant.
## cf.F(z,n)
Returns the polylogarithm of a complex number in the form of (Re,Im). (sum of (z**(k))/(k**(n))
The input is two tuples or strings(x + iy) and it returns a tuple.
## cf.gamma(z)
Returns the euler gamma of a complex number in the form of (Re,Im). 
The input is a tuple or a string(x + iy) and it returns a tuple.
## cf.H_n(n)
Returns the harmonic sum from 1 to n.
The input is a integer and the output is a float.
## cf.is_prime(n)
Returns true if the number is a prime and false if not.
The input is a positive integer and it returns string.
## cf.L(k,s,X1)
Returns the Dirichlet L function in form of (Re,Im). ( mod k, index X1)
The input are positive integers(k,X1) and a tuple or a string(x + iy)(s) and it returns tuple.
## cf.lamba(z)
Returns the Dirichlet Lambda function in form of (Re,Im).
The input is a tuple or a string(x + iy) and it returns a tuple.
## cf.lerch(z,s,a)
Returns the Lerch Transcendent in form of (Re,Im).
The input are tuples or strings(x + iy) and it returns a tuple.
## cf.N(p)
Reurns the group of units in the ring of integers modulo p.
The input is a positive integer and it returns integer.
## cf.pi(n)
Returns the Prime Counting function of a number.
The input is a positive integer and it returns float.
## cf.polygamma(n)
Returns the polygamma function of a real number.
The input is a integer and the output is a float.
## cf.siegel(t)
Returns the Riemann-Siegel theta function of a real number. 
The input is a Decimal and it returns a Decimal.
## cf.tau(n)
Returns the Tau function of a number.
The input is a positive integer and it returns integer.
## cf.totient(n) 
Returns the totient of a number.
The input is a positive integer and it returns integer.
## cf.totient_num(n)
Returns the totatives of a number.
The input is a positive integer and it returns list.
## cf.X(k,j,n)
Returns the Dirichlet Characters of a number. ( mod k, index j)
The input are positive integers and it returns integer.
## cf.Z(t)
Returns the Riemann-Siegel Z function of a real number in the form of (Re,Im). 
The input is a Decimal and it returns a tuple.
## cf.zeta(z)
Returns the Riemann Zeta function of a complex number in the form of (Re,Im). 
The input is a tuple or a string(x + iy) and it returns a tuple.
