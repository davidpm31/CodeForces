#include <bits/stdc++.h>

using namespace std;


int main (void)
{
	ios_base::sync_with_stdio(0);
	std::ios::sync_with_stdio(0);
	cin.tie(0);

	int n = 0, m = 0;

	cin >> n >> m;

	if ((min(n, m) % 2) == 0)
		cout << "Malvika" << endl;
	else
		cout << "Akshat" << endl;

	return 0;

}
