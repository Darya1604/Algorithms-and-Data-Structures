#include <iostream>
#include <vector>

using namespace std; 

void Selection_Sort(vector<int>& vec){
    int n;
    n = vec.size();
    for (int i = 0; i < n-1; i++) {
    	int MaxIndex = i;
    	for (int j = i; j < n; j++){
    		if (vec[j] > vec[MaxIndex]){
    			MaxIndex = j;
			}
		}
		swap(vec[i], vec[MaxIndex]);
	}
}

int main() {
	int x;
    vector <int> arr;
    while (cin >> x){
    arr.push_back(x);
    }
    Selection_Sort(arr);
    for (int i=0; i < arr.size(); i++){
    cout << arr[i] << " ";
    }
    cout << endl;
}

