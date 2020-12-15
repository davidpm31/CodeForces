#include <bits/stdc++.h> //need to send test cases with a file (a.exe < test.txt)

using namespace std;


int main (void)
{
	ios_base::sync_with_stdio(0);
	std::ios::sync_with_stdio(0);
	cin.tie(0);
	int x = 0, y = 0;
	int aux = 0, res = 0;

	for (int i = 1; i <= 5; i++)
	{
		for (int j = 1; j <= 5; j++)
		{
			cin >> aux;
			if(aux == 1)
			{
				x = i;
				y = j;
			}
		}
		scanf("\n");
	}

	res = abs((3 - x)) + abs((3 - y));

	cout << res << endl;

}
