#include <iostream>
#include <vector>

using namespace std; 

void Insertion_Sort(vector<int>& vec){
    int n = vec.size();
    for (int i = 1; i < n; i++) {
    	int key = vec[i];
    	int j = i - 1;
		while (j >= 0 && vec[j] > key) {
			vec[j+1] = vec[j];
			j--;}
			
			vec[j+1] = key;
			}
	}
	
int main3() {
	int x;
    vector <int> arr;
    while (cin >> x){
    arr.push_back(x);
    }
    Insertion_Sort(arr);
    for (int i=0; i < arr.size(); i++){
    cout << arr[i] << " ";
    }
    cout << endl;
}
