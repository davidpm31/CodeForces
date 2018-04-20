#include <bits/stdc++.h>

using namespace std;


int main (void)
{
	ios_base::sync_with_stdio(0);
	std::ios::sync_with_stdio(0);
	cin.tie(0);

	string s;
	stack <char> H;
	H.push('o');
	H.push('l');
	H.push('l');
	H.push('e');
	H.push('h');

	cin >> s;

	int n = s.size();

	for (int i = 0; i < n; i++)
	{
		if(s[i] == H.top())
			H.pop();
		if(H.empty())
			break;
	}

	if(H.empty())
		cout << "YES" << endl;
	else
		cout << "NO" << endl;

	return 0;

}