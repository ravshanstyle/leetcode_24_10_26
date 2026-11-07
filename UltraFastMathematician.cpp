#include <bits/stdc++.h>
using namespace std;

int main (){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string c1, c2, res;
    cin >> c1 >> c2 ;
    for( int i = 0; i < c1.size(); ++i){
        if(c1[i] != c2[i]){
            res += '1';
    }else{
        res +='0';
    }
}
    cout << res << endl;
    return (0);
}