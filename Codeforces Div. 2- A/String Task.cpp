#include <bits/stdc++.h>

using namespace std;

const int N  =  100;
int main (void)
{
	ios_base::sync_with_stdio(0);
	std::ios::sync_with_stdio(0);
	cin.tie(0);

	string str, aux;
	cin >> str;

	int n = str.size();
	for (int i = 0; i < n; i++)
	{
		if (((str[i] != 65) && (str[i] != 69) && (str[i] != 73) && (str[i] != 79) && (str[i] != 89) && (str[i] != 85)) && (str[i] != 97) && (str[i] != 101) && (str[i] != 105) && (str[i] != 121) && (str[i] != 111) && (str[i] != 117))
		{
			aux.append(sizeof(char), '.');
			if (str[i] >= 97 && str[i] <= 122)
				aux.append(sizeof(char), str[i]);
			if (str[i] >= 65 && str[i] <= 90)
				aux.append(sizeof(char), str[i] + 32);
		}
	}

	cout << aux << endl;

}
