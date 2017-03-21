#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	ll n, m;
	cin >> n >> m;
	ll x = n;
	ll i = 0;
	
	if (m >= n)
	{
		cout << n;
		return 0;
	}
	
	// if m < n
	x -= m;
	ll sum = x;
	ll low = 1, high = 2e9, mid;
	while (low < high)
	{
		mid = (low + high) / 2;
		ll s = mid * (mid + 1) / 2;
		if (s >= sum)
		{
			high = mid;
		}
		else if (s < sum)
		{
			low = mid + 1;
		}
	}
	cout << m + low << "\n";
	return 0;
}
