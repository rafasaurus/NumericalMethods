// Newton.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
using namespace std;
void Newton_function_matrix();
double Newton_function(int,double);
void tpel();
double x_arr[] { 0.115, 0.120, 0.125, 0.130, 0.135, 0.140, 0.145, 0.150, 0.155, 0.160, 0.165, 0.170, 0.175, 0.180	};
double function_arr[] {8.65, 8.29 , 7.95 ,7.64 ,7.36 ,7.09 ,6.84 ,6.61 ,6.39 ,6.19 ,6.00 ,5.82 ,5.65 ,5.49 };
double newton_arr[5][5]={0};
double x0_arr[] {0.1217, 0.1736, 0.1141, 0.185};
int n = 14;
double x = 0.115;

int _tmain(int argc, _TCHAR* argv[])
{
	cout << "n=" << n << endl; n++;
	cout << endl;
	for (int i = 0; i < n; i++)
	{
		cout << "x[" << i << "]=" << x_arr[i] << endl;
	}
	cout << endl;
	for (int i = 0; i < n; i++)
	{
		cout << "f[" << i << "]=" << function_arr[i] << endl;
	}

	cout << endl;
	for (int i = 0; i < 4; i++)
	{
		x = x0_arr[i];
		cout << "x=" << x0_arr[i] << " i hamar" << endl;
		tpel();
		cout << endl;
	}
	cin >> n;
	return 0;
}
void Newton_function_matrix()
{
	for (int i = 0; i < n; i++)
	{
		newton_arr[i][0] = function_arr[i];
	}
	int k = 1;
	int p = 0;
	for (int i = 1; i < n-1; i++)
	{
		k = 0;
		p = 0;
		k += i;
		for (int j = 0; j <= n-i+1; j++)
		{	
			newton_arr[j][i] = (newton_arr[j + 1][i - 1] - newton_arr[j][i - 1]) / (x_arr[k] - x_arr[p]);		
			k++;
			p++;
		}
	}
		//cout << endl;
		//for (int i = 0; i < n; i++)
		//{
		//
		//	for (int j = 0; j < n - i; j++)
		//	{
		//		cout << newton_arr[i][j]<<" ";
		//	}
		//	cout << endl;
		//	
		//}
		//cout << endl;
}

double  Newton_function()
{
	Newton_function_matrix();
	double s = function_arr[0];
	for (int i = 0; i <n; i++)
	{
		double  x_gorcak=1;
		for (int j = 0; j <=i; j++)
		{
			x_gorcak*= x - x_arr[j];
		}
		
		s += newton_arr[0][i+1] * x_gorcak;
	}

	return s;
}

void tpel()
{
	cout << function_arr[0] << "+";
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j <=i; j++)
		{
			cout << "(x-" << x_arr[j] << ")";
		}
		cout << "*" <<"("<< function_arr[i]<<")";
		if (i!=n-1)
		cout << "+";
	}
	cout << " = " << Newton_function() << endl;
}


