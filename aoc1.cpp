#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen("data.txt", "r", stdin);
	cin.tie(0)->sync_with_stdio(0);
	vector<int> list1(1000);
	vector<int> list2(1000);

	for (int i = 0; i < 1000; i++) cin >> list1[i] >> list2[i];

	sort(list1.begin(), list1.end());
	sort(list2.begin(), list2.end());
	long long X = 0;
	for (int i = 0; i < 1000; i++) {
		X += abs(list2[i] - list1[i]);
	}
	cout << X << endl;

	X = 0;
	for (int i = 0; i < 1000; i++) {
		int count = 0;
		for (int j = 0; j < 1000; j++) {
			if (list1[i] == list2[j]) count++;
		}
		X += list1[i] * count;
	}

	cout << X << endl;
}
