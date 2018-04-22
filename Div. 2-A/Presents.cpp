#include <bits/stdc++.h>

using namespace std;

vector<int> invert(vector<int> perm)
{
    int n = perm.size();
    vector<int> inverse(n);

    for (int i = 0; i < n; i++)
        inverse[perm[i] - 1] = i + 1;

    return inverse;     
}


int main (void)
{
    ios_base::sync_with_stdio(0);
    std::ios::sync_with_stdio(0);
    cin.tie(0);

    int n = 0, aux = 0;
    vector<int> friends;

    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> aux;
        friends.push_back(aux);
    }

    vector<int> res = invert(friends);

    for (int i = 0; i < n; i++)
    {
        if (i == 0)
            cout << res[0];
        else
            cout << " " << res[i];
    }
    cout << endl;

    return 0;
}
