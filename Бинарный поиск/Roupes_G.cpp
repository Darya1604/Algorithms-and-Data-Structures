#include <iostream>
#include <vector>

using namespace std;

int N, K;
vector<int> piecies;

bool ropes(int x){
	int count = 0;
	for (int length: piecies){
		count += length / x;
	} 
	return count >= K;
}

int main() {
	cin >> N >> K;
	
	for (int i = 0; i < N; i++) {
		int length;
		cin >> length;
		piecies.push_back(length);
	}
	 int l = 0;
	 int r = 10000001;
	 
	 while (r - l > 1) {
	 	int m = (l + r) / 2;
	 	
	 	if (ropes(m)){
	 		l = m;
		 } else {
		 	r = m;
		 }
	 }
	 cout << l << endl;
}
