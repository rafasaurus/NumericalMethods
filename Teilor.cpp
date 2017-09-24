// ConsoleApplication11.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <math.h>
using namespace std;
int factor(int);
int teilor(int n, int x0,int x);//veradardznum e x ketum motarkox functioni arjeq@
int teilor_(int n, int x0, int x);
int zugordutyun(int, int);
int derivate[5] = { 20, 61, 154, 270, 240 };//acancyalner@
int x = 1;//es keti hamar teilor
int x0 = 1;//ketum vorum trvac en acancyalner
int _tmain(int argc, _TCHAR* argv[])
{
	int n;
	cout << "n="; cin >> n;
	cout << "x0="; cin >> x0;
	cout << x0 << " ketum trvac acacnyal@" << endl;
	for (int i = 0; i < n; i++)
	{
		cout << "acancyal[" << i << "]=";
		cin >> derivate[i];
	}
	cout << "x="; cin >> x;	
	cout<<" = "  << teilor(n, x0,x) << endl;	
	cin >> x;
	return 0;
}

int teilor(int n, int x0, int x)
{
	cout << endl;
	cout << endl;
	int newton_alfa = 0;
	int teil = 0;
	int newton_teil_ = 0;
	int newton_teil_sum_ = 0;
	int array_of_factors_[10][10]= { 0 };
	int factors[10]= { 0 };
	for (int i = 0; i <=n; i++)
	{
		int newton_ = 0;

		teil += (derivate[i] * pow((x - x0), i)) / factor(i);
		for (int j = 0; j <=i; j++)
		{
			newton_ = zugordutyun(i, j)*pow(x0, j)*pow(-1, j);
			array_of_factors_[i][j] = newton_* derivate[i] / factor(i);
		}
		
		
		//cout << endl;
		//newton_teil_ = derivate[i] * newton_ / factor(i);
		//newton_teil_sum_ += newton_teil_;
		//cout << newton_teil_sum_ << endl;
		
	}
	//for (int i = 0; i <= n; i++)
	//{
	//	for (int j = 0; j <= n; j++)
	//	{
	//		cout << array_of_factors_[i][j] << " ";
	//	}
	//	cout << endl;
	//}
	
	for (int j = 0; j <= n; j++)
	{
		for (int i = 0; i <= n - j; i++)
		{
			factors[j] += array_of_factors_[i+j][i];
		}	
	}

	for (int j = 0; j <= n; j++)//bazmadnami artacum
	{	
		cout << factors[j] << "x^" << n - j;
		if (j != n)
		{
			cout<< "+";
		}
	}	
	return teil;
}

int factor(int k)
{
	int fact=1;
	for (int i = 1; i <=k; i++)
	{
		fact *= i;
	}
	return fact;
}

int zugordutyun(int n,int k)//n ic k akan
{
	return factor(n) / (factor(k)*factor(n - k));
}