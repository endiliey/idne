#include <bits/stdc++.h>

using namespace std;

int main()
{
    int k, n;
    vector<int> scores;
    cin >> n >> k;
    for (int val, i = 0; i != n ; ++i)
    {
        cin >> val;
        scores.push_back(val);
    }

    int passingScore = scores[k - 1];
    int passer = 0;

    for (int score : scores)
    {
        if (score >= passingScore && score != 0)
        {
            ++passer;
        }
    }

    cout << passer << endl;

    return 0;
}
