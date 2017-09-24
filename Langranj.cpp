// Langranj.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
using namespace std;
double lang_value();
double lang__value_();
void gorcakic_funciton();
void tpel();
double function_arr[5] = {1, 3.75, 20, 76, 213};
double x_arr[5] = {0, 0.5, 1, 1.5, 2};

int n = 5;
double x =2;
double gorcakicner_of_each_summary[5] = { 0 };

int _tmain(int argc, _TCHAR* argv[])
{
	
	cout << "n="; cin >> n;
	double op = 0;
	
	for (int i = 0; i < n; i++)
	{
		cout << "x[" << i << "]=";
		cin >> x_arr[i];
	}
	for (int i = 0; i < n; i++)
	{

		cout << "f(" << op << ")=";
		cin >> function_arr[i];
		op = op + 0.5;
	}
	cout << "x="; cin >> x;
	tpel();
	cin >> x;
	return 0;
}

double lang__value_()
{
	
	double s, t,k=0;
	//cout << "a=";
	//cin >> a;
		for (int i = 0; i<n; i++)
		{
			s = 1;
			t = 1;
			for (int j = 0; j<n; j++)
			{
				if (j != i)
				{
					s = s*(x - x_arr[j]);
					t = t*(x_arr[i] - x_arr[j]);
				}
			}
			k = k + ((s / t)*function_arr[i]);
		}
		return k;
}


void gorcakic_funciton()
{
	for (int i = 0; i<n; i++)
	{
		double s = 1;
		for (int j = 0; j<n; j++)
		{
			if (j != i)
			{
				s *= x_arr[i] - x_arr[j];
			}
		}
		gorcakicner_of_each_summary[i] = function_arr[i] / s;
	}
}
void tpel()
{
	gorcakic_funciton();
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (j != n-i)
			{
				cout << "(x-" << x_arr[j] << ")*";
			}
		}
		cout <<"("<< gorcakicner_of_each_summary[i]<<")";
		if (i!=n-1)
			cout<< "+";
	}
	cout << "=" << lang__value_() << endl;
}