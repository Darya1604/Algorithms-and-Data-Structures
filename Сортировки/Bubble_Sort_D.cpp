#include <iostream>
#include <vector>

using namespace std;

void Bubble_Sort(vector<int>& vec, int& Count_Change){
    int n;
    n = vec.size();
    Count_Change = 0;
    for (int i = 0; i < n - 1; i++){
        for (int j = 0; j < n - i - 1; j++){
            if (vec[j] > vec[j + 1]){
                swap(vec[j], vec[j+1]);
                Count_Change++;
            }
        }
    }
}

int main(){
    int n;
    int Count_Change;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++){
        cin >> arr[i];
    }
    Bubble_Sort(arr, Count_Change);
    cout << Count_Change << endl;
}
