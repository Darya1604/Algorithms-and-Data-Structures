#include <iostream>
#include <algorithm>

using namespace std;

long long w, h, n;

bool diploma(long long x) {
	return (x / w) * (x / h) >= n;
}

int main() {
	cin >> w >> h >> n;
	
	long long l = 0;
	long long r = n*max(w, h);
	
	while (r - l > 1) {
		long long m = (l + r) / 2;
		
		if (diploma(m)) {
			r = m;
		} else {
			l = m;
		}
	}
	cout << r << endl;
}
