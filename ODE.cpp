#include "stdafx.h"
#include  <iostream>
#include  <math.h>
bool recursive_euler(double, double,double &);
bool recursive_runge_kutta(double t, double &y, double &accuracy);
bool recursive_runge_kutta(double &t, double &y, double &accuracy, double *,int &n);
bool adams(double &t, double &y, double &accurancy);
bool shtermer(double &t, double &y, double &accurancy);

using namespace std;
/*------- euler -----*/

double h_euler = 0.1;
int i_euler = 0;
#define f(t,y) ((t) + cos((y) / 3))

#define sht(x) ((exp((x))+(x))

/*-------------runge-kutta-----*/
double h = 0.1;
int i_runge = 0;
//#define f(t,y) (pow((t), 2) + pow((y), 2)) //simonyan

double arr[30];
double ar[30];


#define y_derivative(x,y)  (x+cos(y/pow(5,1/2)))
int main()
{
	//cout << y_derivative(1, 2) << endl;
	double euler_accurancy = 10;
	cout << "--------Euler OED----------" << endl;
	//bool ooo=recursive_euler(1.8, 2.6, euler_accurancy);
	bool ooo = recursive_euler(1, 1, euler_accurancy);//simonyan
	cout << "---------------------------" << endl;

	cout << "--------Runge kutta OED----------" << endl;
	double t=1, y=1;
	bool ppp = recursive_runge_kutta(t, y, euler_accurancy);
	cout << "---------------------------------" << endl;


	cout << "--------adams OED----------" << endl;
	t = 1; y = 1;
	i_runge = 0;
	bool lll = adams(t, y, euler_accurancy);
	cout << "---------------------------------" << endl;

	cout << "--------shtermer OED----------" << endl;
	t = 1; y = 1;
	i_runge = 0;
	bool mmm = shtermer(t, y, euler_accurancy);
	cout << "---------------------------------" << endl;
	
	return 0;
}

bool recursive_euler(double t, double y, double &accuracy)
{

	
	cout << "t[" << i_euler << "]=" << t << "   y[" << i_euler << "]=" << y << endl;
	
	//y = y+0.1*(pow(t, 2) + pow(y, 2)); // Simonyan check variables t=1 y=1 accurancy =70
	y = y + 0.1*f(y,t);
	t += h_euler;
	i_euler++;
	if (y > accuracy)
	{
		return true;
	}
	recursive_euler(t, y, accuracy);
	//if (y > 20) cin>>i;
}

bool recursive_runge_kutta(double t, double &y, double &accuracy)
{
	double k1 = h*f(t,y);
	double k2 = h*f(t + 0.5*h, y + 0.5*k1);
	double k3 = h*f(t + 0.5*h, y + 0.5*k2);
	double k4 = h*f(t + h, y + k3);
	cout << "   y[" << i_runge << "]=" << y << endl;
	y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6;
	
	if (y > accuracy)
	{
		return true;
	}
	t += 0.1;
	i_runge++;
	recursive_runge_kutta(t, y, accuracy);
}

bool recursive_runge_kutta(double &t, double &y, double &accuracy, double *p, int &n)//for adams method
{
	p[i_runge] = y;
	double k1 = h*f(t, y);
	double k2 = h*f(t + 0.5*h, y + 0.5*k1);
	double k3 = h*f(t + 0.5*h, y + 0.5*k2);
	double k4 = h*f(t + h, y + k3);
	//cout << "   y[" << i_runge << "]=" << y << endl;
	
	if (i_runge>n-1)
	{
		
		return true;
	}
	y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6;
	t += 0.1;
	i_runge++;
	recursive_runge_kutta(t, y, accuracy,p,n);
}

bool adams_bool = true;
bool shtermer_bool=true;//this stands for runge kutta method's first 4 elements initialization for adams's method
int n_ = 4;
double y_ = 0;
double adams_adjustment = 0;
bool adams(double &t,double &y,double &accurancy)
{

	if (adams_bool)
	{
		recursive_runge_kutta(t, y, accurancy, arr, n_);
		adams_bool = false;
		for (int i = 0; i <n_+1; i++)
		{
			cout << "   y[" << i << "]=" << arr[i] << endl;
		}
	}

	for (int i = n_; i < 10000; i++)
	{
		double y_ = y + (h/24)*(55 * f(t, arr[i]) - 59 * f(t - 0.1, arr[i - 1]) + 37 * f(t - 0.2, arr[i - 2]) - 9 * f(t - 0.3, arr[i - 3]));
		y = y + (h / 24)*(9 * f(t + 0.1, y_) + 19 * f(t, arr[i]) - 5 * f(t - 0.1, arr[i - 1]) + f(t - 0.2, arr[i - 2]));
		arr[i+1] = y;
		t += 0.1;
		cout << "   y[" << i+1 << "]=" << y << endl;
		if (y > accurancy) return true;
	}
}


bool shtermer(double &t, double &y, double &accurancy)
{
	if (shtermer_bool)
	{
		recursive_runge_kutta(t, y, accurancy, ar, n_);
		shtermer_bool = false;
		for (int i = 0; i <n_ + 1; i++)
		{
			cout << "   y[" << i << "]=" << ar[i] << endl;
		}
		cout << "------------shtermer lucum -------" << endl;
		for (double i = 0; i <=0.8; i+=0.2)
		{
			cout << "   y[" << i << "]=";// << sht(i) << endl;
		}
		cout << "------------shtermer lucum -------" << endl;
	}
	return true;

}
