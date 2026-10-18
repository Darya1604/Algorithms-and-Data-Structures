#include <iostream>
#include <algorithm>

using namespace std;

bool print_copies(int copy, int quick, int slow, int time){
	return time / quick + time / slow >= copy;
}

int main() {
	int copy, quick, slow;
	cin >> copy >> quick >> slow;
	
	if (slow < quick){
		swap(quick, slow);
	}
	int l = 0;
	int r = (copy - 1) * slow;
	while (r - l > 1){
		int m = (l + r) / 2;
		if (!print_copies(copy-1, quick, slow, m)){
			l = m;
		} else {
			r = m;
		}
	}
	cout << r+quick << endl;
}
