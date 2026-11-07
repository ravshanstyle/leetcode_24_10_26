#include <bits/stdc++.h>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    vector<int> lst;
    int n;
    cin >> n;
    int x;
    while(cin >> x) lst.push_back(x);
    double sum = accumulate(lst.begin(), lst.end(), 0LL);
    double res = sum/n;
    cout << fixed << setprecision(12) << res << endl;
    return (0);
}