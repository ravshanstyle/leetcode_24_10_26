#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int cost_for_banana, amount_of_money, num_of_bananas;
    cin >> cost_for_banana >> amount_of_money >> num_of_bananas;
    int total = 0;
    int debt = 0;
    for(int i = 1; i < num_of_bananas + 1; i++ ){
        total += i * cost_for_banana;
    }
    if (amount_of_money < total){
        debt = amount_of_money - total;
    }
    cout << debt * (-1) << endl;
    return 0;
}