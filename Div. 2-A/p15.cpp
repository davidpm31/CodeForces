#include <bits/stdc++.h>
 
using namespace std;
 
 
int main (void)
{
	ios_base::sync_with_stdio(0);
	std::ios::sync_with_stdio(0);
	cin.tie(0);
 
	int n = 0;
	int x = 0, y = 0, z = 0;
	int xT = 0, yT = 0, zT = 0;
 
	cin >> n;
 
	vector<int[3]> coordinates(n);
 
	for (int i = 0; i < n; i++)
	{
		cin >> x >> y >> z;
		xT += x;
		yT += y;
		zT += z;
	}
 
	if (xT == 0 && yT == 0 && zT == 0)
		cout << "YES" << endl;
	else
		cout << "NO" << endl;
 
	return 0;
 
}