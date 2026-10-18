#include <iostream>
#include <vector>

using namespace std;

bool cow_in_stall(vector<int>& boxes,int N, int cow, int dist) {
	int cows_count = 1;
	int last_box = boxes[0];
	for (int i = 1; i < N; i++){
		int box = boxes[i];
		if (box - last_box >= dist){
		   cows_count++;
		   last_box = box;}
	}
	return cows_count >= cow;
}

int main() {
	int N, cow;
	cin >> N >> cow;
	
	vector<int> boxes(N);
	for (int i = 0; i < N; i++){
		cin >> boxes[i];
    }
	
	int l = 0;
	int r = boxes[N-1] - boxes[0] + 1;
	
	while (r - l > 1){
		int m = (l + r) / 2;
		if (cow_in_stall(boxes, N, cow, m)){
			l = m;
		} else {
			r = m;
		}
	}
	cout << l << endl;
}
