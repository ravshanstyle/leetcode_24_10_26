#include <bits/stdc++.h>
using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string n;
    cin >> n ;
    string res = "YES";
    int count = 0;
    for(int i = 0; i < n.size(); ++i){
        if(n[i] == '4' || n[i] == '7'){
            count =+ 1;
        }
    }
    if(count != 4 && count != 7){
        res = "NO";
    }
    cout << res << endl;
    return 0;
}