#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void Counting_Sort(vector <int>& arr) {
	if (arr.empty()) {
		return;
	}
	int k = *max_element(arr.begin(), arr.end());
	vector<int> count(k+1, 0);
	for (int x: arr) {
		count[x]++;
}
	arr.clear();
	for (int i = 0; i <= k; i++ ) {
		for (int j = 0; j < count[i]; j++) {
			arr.push_back(i);
		}
	}
}

int main() {
    vector<int> arr;
    int x;
    while (cin >> x) {
        arr.push_back(x);
    }
    Counting_Sort(arr);
    for (int x : arr) {
        cout << x << " ";
    }
    cout << endl;
}



