#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;
    vector<int> lst(n);
    for(int i = 0; i < n; i++){
        cin >> lst[i];
        }
    
    int police = 0, c_gone = 0;
    for (int i = 0; i < n; ++i){
        if(lst[i] > 0){
            police += lst[i];
        }else if(lst[i] == -1){
            if(police <= 0 ){
                c_gone += 1;
            }else{
                police -= 1;
            }
        }
    }
    cout << c_gone << endl;
    return (0);

}