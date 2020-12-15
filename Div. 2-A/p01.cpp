#include <bits/stdc++.h>

using namespace std;


int main (void)
{
	ios_base::sync_with_stdio(0);
	std::ios::sync_with_stdio(0);
	cin.tie(0);
	int w = 0;

	cin >> w;

	if(w % 2 == 0 && w > 2)
		cout << "YES" << endl;
	else
		cout << "NO" << endl;

	return 0;

}
