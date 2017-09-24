// numerical_integral.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <math.h>
double rectangle_method();
double table_method();
double parabolic_method();
double simpson();
double newton_cottess();
double gaus();

#define f(x) (1/((x*x)+3.2))
using namespace std;

#define a 1.2 //for newton kottess
#define b 2.7 

double h = b - a;
#define x0 1.95
//#define f(x) (5*(sin(7*(x))))+(2*(exp(x)))
int _tmain(int argc, _TCHAR* argv[])
{
	cout << "rectangle_method = " << rectangle_method() << endl;
	cout << "table_method     = "; cout << table_method() << endl;
	cout << "parabolic_method = ";   cout << parabolic_method() << endl;
	cout << "simpson          = ";  cout << simpson() << endl;
	cout << "newton_cottess   = ";   cout << newton_cottess() << endl;
	cout << "gaus             = ";  cout << gaus() << endl;
	cout << double(pow(3, double(1 / 2))) << endl;
	return 0;
}


double rectangle_method()
{
	return h*f(1.95);
}

double table_method()
{
	return h*(f(a) + f(a + h))/2;
}

double parabolic_method()
{
	return h* (f(x0 - h/2) + 4 * f(x0) + f(x0 + h/2)) / 6;
}

double simpson()
{
	return (b - a)*(f(a)+4*f((a+b)/2)+f(b)) / 6;
}
double newton_cottess()
{
	return (b-a)*(7*f(a)+32*f((3*a+b)/4)+12*f((a+b)/2)+32*f((a+3*b)/4)+7*f(b))/90;
}
double gaus()
{
	return  ((b - a) / 2)  * (f(((a + b) / 2) - 0.288*(b - a)) + f(((a + b) / 2) + 0.288*(b - a)));
}

