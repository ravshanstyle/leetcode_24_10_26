#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    vector<int> lst;
    int x;
    while(cin >> x) lst.push_back(x);
    sort(lst.begin(), lst.end()); // o'sish tartibida
    int count = 0;
    for(int i = 1; i < 4; ++i){
        if(lst[i] == lst[i-1]){
            count++;
        }
    }
    cout << count << endl;

    return (0);
}