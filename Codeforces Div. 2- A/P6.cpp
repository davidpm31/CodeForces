#include <bits/stdc++.h>

using namespace std;

bool compareMax (int i, int j)
{
	return (i > j); 
}

int main (void)
{
	ios_base::sync_with_stdio(0);
	std::ios::sync_with_stdio(0);
	cin.tie(0);

	int n = 0, aux = 0;
	int nCoin = 0, Total = 0, evilT = 0;;
	vector<int> a;

	cin >> n;

	for (int i = 0; i < n; i++)
	{
		cin >> aux;
		a.push_back(aux);
		Total += aux;
	}

	sort(a.begin(), a.end(), compareMax);

	while (evilT <= (Total / 2))
    {
        evilT += a[nCoin++];
    }

	cout << nCoin << endl;

	return 0;

}