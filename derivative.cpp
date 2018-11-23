#include "stdafx.h"
#include <iostream>
#include <math.h>

double derivate_teilor_1(double x);//teilor derive 1
double derivate_teilor_2(double x);
double derivate_teilor_3(double x);
double derivate_teilor_1_(double x);//teilor derive 1
double derivate_teilor_2_(double x);
double derivate_teilor_3_(double x);
/*---------------------------newton m=1 n=2-----------------------------*/
double derivate_newton_der_1_obj_2_f_0();//newton derive 1
double derivate_newton_der_1_obj_2_f_1();
double derivate_newton_der_1_obj_2_f_2();
/*---------------------------newton m=2 n=2-----------------------------*/
double derivate_newton_der_2_obj_2_f_0();//newton derive 2
double derivate_newton_der_2_obj_2_f_1();
double derivate_newton_der_2_obj_2_f_2();

/*---------------------------newton m=1 n=3-----------------------------*/
double derivate_newton_der_1_obj_3_f_0();
double derivate_newton_der_1_obj_3_f_1();
double derivate_newton_der_1_obj_3_f_2();
double derivate_newton_der_1_obj_3_f_3();
/*---------------------------newton m=2 n=3-----------------------------*/
double derivate_newton_der_2_obj_3_f_0();
double derivate_newton_der_2_obj_3_f_1();
double derivate_newton_der_2_obj_3_f_2();
double derivate_newton_der_2_obj_3_f_3();

using namespace std;

double h = 0.1;
double h_1 = 0.01;
double h_newton = 1;
#define x0 2
#define x1 3
#define x2 4
#define x3 5
//#define f(x) (exp(sin(x)))
#define f(x) (5*(sin(7*(x))))+(2*(exp(x)))
#define df(x) (37*(cos(7*(x))))+(2*(exp(x)))
#define ddf(x) ((2*exp(x))-(259*(sin(7*x))))
//#define ff(x) 5*sin(7*(x))+2*exp(x)
int _tmain(int argc, _TCHAR* argv[])
{
	double  x = 2;
	cout << "----------- teilor h=0.1, x0=2 ---------------" << endl;
	cout << "f derivative at 0. 1 method  =  ";  cout << derivate_teilor_1(x) << endl;
	cout << "f derivative at 0. 2 method  =  "; cout << derivate_teilor_2(x) << endl;
	cout << "f derivative at 0. 3 method  =  "; cout << derivate_teilor_3(x) << endl;

	cout << "----------- teilor h=0.01, x0=2 ---------------" << endl;
	cout << "f derivative at 0. 1 method  =  ";  cout << derivate_teilor_1_(x) << endl;
	cout << "f derivative at 0. 2 method  =  "; cout << derivate_teilor_2_(x) << endl;
	cout << "f derivative at 0. 3 method  =  "; cout << derivate_teilor_3_(x) << endl;

	cout << "-----------newton m=1, n=2, x0=2, x1=2, x2=3 --------------" << '\n' << endl;
	/*---------------------------newton m=1 n=2-----------------------------*/
	cout << "f derivative at x0  =  "; cout << derivate_newton_der_1_obj_2_f_0() << endl;
	cout << "f derivative at x1  =  "; cout << derivate_newton_der_1_obj_2_f_1() << endl;
	cout << "f derivative at x2  =  "; cout << derivate_newton_der_1_obj_2_f_2() << endl;

	/*---------------------------newton m=2 n=2-----------------------------*/
	cout << "-----------newton  m=2, n=2, x0=2, x1=2, x2=3, x3=4--------------" << '\n' << endl;
	cout << "f seccond derivative at x0 x1 x2  =  "; cout << derivate_newton_der_2_obj_2_f_2() << endl;
	/*---------------------------newton m=1 n=3-----------------------------*/
	 cout << "-----------newton m=1 n=3 derive 1--------------" << '\n' << endl;
	 cout << "f derivative at x0  =  "; cout << derivate_newton_der_1_obj_3_f_0() << endl;
	 cout << "f derivative at x1  =  "; cout << derivate_newton_der_1_obj_3_f_1() << endl;
	 cout << "f derivative at x2  =  "; cout << derivate_newton_der_1_obj_3_f_2() << endl;
	 cout << "f derivative at x3  =  "; cout << derivate_newton_der_1_obj_3_f_3() << endl;
	/*---------------------------newton m=2 n=3-----------------------------*/
	 cout << "-----------newton m=2 n=3 derive 2--------------" << '\n' << endl;
	 cout << "f seccond derivative at x0  =  "; cout << derivate_newton_der_2_obj_3_f_0() << endl;
	 cout << "f seccond derivative at x1  =  "; cout << derivate_newton_der_2_obj_3_f_1() << endl;
	 cout << "f seccond derivative at x2  =  "; cout << derivate_newton_der_2_obj_3_f_2() << endl;
	 cout << "f seccond derivative at x3  =  "; cout << derivate_newton_der_2_obj_3_f_3() << endl;
	 cout << endl;
	 cout << "df(x0)="; cout << df(x0) << endl;
	 cout << "df(x1)="; cout << df(x1) << endl;
	 cout << "df(x2)="; cout << df(x2) << endl;
	 cout << "df(x3)="; cout << df(x3) << endl;
	 cout << endl;
	 cout << "ddf(x0)="; cout << ddf(x0) << endl;
	 cout << "ddf(x1)="; cout << ddf(x1) << endl;
	 cout << "ddf(x2)="; cout << ddf(x2) << endl;
	 cout << "ddf(x3)="; cout << ddf(x3) << endl;
	 //cout << ddf(x0) << endl;

	return 0;
}
/*---------------------------teilor for h=0.1-----------------------------*/
double derivate_teilor_1(double x)
{
	double derivate = ((f(x+h)) - (f(x))) / h;
	return derivate;
}

double derivate_teilor_2(double x)
{
	double derivate = ((f(x + h)) - (f(x-h))) / (2*h);
	return derivate;
}
double derivate_teilor_3(double x)
{
	double derivate = (8*(f(x+h))-8*(f(x-h))-(f(x+2*h))+(f(x-2*h))) / (12*h);
	return derivate;
}
/*---------------------------teilor for h=0.01-----------------------------*/

double derivate_teilor_1_(double x)
{
	double derivate = ((f(x + h_1)) - (f(x))) / h_1;
	return derivate;
}

double derivate_teilor_2_(double x)
{
	double derivate = ((f(x + h_1)) - (f(x - h_1))) / (2 * h_1);
	return derivate;
}
double derivate_teilor_3_(double x)
{
	double derivate = (8 * (f(x + h_1)) - 8 * (f(x - h_1)) - (f(x + 2 * h_1)) + (f(x - 2 * h_1))) / (12 * h_1);
	return derivate;
}
/*---------------------------newton m=1 n=2-----------------------------*/
double derivate_newton_der_1_obj_2_f_0()//function derivative at x0 point
{
	double derivate = (1 / (2 * h_newton))*(4 * (f(x1)) - 3 * (f(x0)) - (f(x2)));
	return derivate;
}

double derivate_newton_der_1_obj_2_f_1()//function derivative at x1 point
{
	double derivate = (1 / (2 * h_newton))*((f(x2)) - (f(x0)));
	return derivate;
}

double derivate_newton_der_1_obj_2_f_2()//function derivative at x2 point
{
	double derivate = (1 / (2 * h_newton))*((f(x0))-4*(f(x1))+3*(f(x2)));
	return derivate;
}
/*---------------------------newton m=2 n=2-----------------------------*/

double derivate_newton_der_2_obj_2_f_0()//function derivative at x0 point
{
	double derivate = (1 / (2 * h_newton*h_newton))*((f(x0))-2*(f(x1))+(f(x2)));
	return derivate;
}

double derivate_newton_der_2_obj_2_f_1()//function derivative at x1 point
{
	double derivate = (1 / (2 * h_newton*h_newton))*((f(x0)) - 2 * (f(x1)) + (f(x2)));
	return derivate;
}

double derivate_newton_der_2_obj_2_f_2()//function derivative at x2 point
{
	double derivate = (1 / (2 * h_newton*h_newton))*((f(x0)) - 2 * (f(x1)) + (f(x2)));
	return derivate;
}

/*---------------------------newton m=1 n=3-----------------------------*/
double derivate_newton_der_1_obj_3_f_0()
{
	double derivate = (1 / (6 * h_newton)) * (18 * (f(x1)) - 11 * (f(x0)) - 9 * (f(x2)) + 2 * (f(x3)));
	return derivate;
}
double derivate_newton_der_1_obj_3_f_1()
{
	double derivate = (1 / (6 * h_newton)) * (6 * ((f(x2))) - (f(x3)) - 3 * (f(x1)) - 2 * (f(x0)));
	return derivate;
}
double derivate_newton_der_1_obj_3_f_2()
{
	double derivate = (1 / (6 * h_newton)) * ((f(x0)) - 6 * (f(x1)) + 3 * (f(x2)) + 2 * (f(x3)));
	return derivate;
}
double derivate_newton_der_1_obj_3_f_3()
{
	double derivate = (1 / (6 * h_newton)) * (9 * (f(x1)) - 2 * (f(x0)) - 18 * (f(x2)) + 11 * (f(x3)));
	return derivate;
}

/*---------------------------newton m=2 n=3-----------------------------*/
double derivate_newton_der_2_obj_3_f_0()
{
	double derivate = (1 / (6 * h_newton*h_newton)) * (2*(f(x0))-5*(f(x1))+4*(f(x2))-(f(x3)));
	return derivate;
}
double derivate_newton_der_2_obj_3_f_1()
{
	double derivate = (1 / (6 * h_newton*h_newton)) * ((f(x0)) - 2 * (f(x1)) + (f(x2)));
	return derivate;
}
double derivate_newton_der_2_obj_3_f_2()
{
	double derivate = (1 / (6 * h_newton*h_newton)) * ((f(x1))-2*(f(x2))+(f(x3)));
	return derivate;
}
double derivate_newton_der_2_obj_3_f_3()
{
	double derivate = (1 / (6 * h_newton*h_newton)) * (4 * (f(x1)) - 5 * (f(x2)) + 2 * (f(x3)) - (f(x0)));
	return derivate;
}
