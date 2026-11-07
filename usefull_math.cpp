#include <bits/stdc++.h>
using namespace std;

int main () {
    string str;
    cin >> str;
    std::vector<char> lst;
    for(int i = 0; i < str.size(); i++){
        if(isdigit(str[i])){
            lst.push_back(str[i]);
        }
    }
    sort(lst.begin(), lst.end());
    for(int j = 0; j < lst.size(); j++){
        cout << lst[j];
        if (j != lst.size() - 1){
            cout << "+";
        }
    }
    return (0);
}
