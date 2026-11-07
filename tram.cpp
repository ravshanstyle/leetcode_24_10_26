#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int a, b, n, m = 0, p = 0;
    cin >> n;
    for(int i = 0; i < n; ++i){
        cin >> a >> b;
        p += (b-a);
        if(p > m){
            m = p;
        }
    }
    cout << m << endl;
    return 0;
}