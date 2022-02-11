#include "bits/stdc++.h"

using namespace std;

int main(){
    string curr;
    ifstream file("input.txt");
    int inr=0;
    int prev=INT_MAX;
    while(getline(file, curr)){
        int temp = stoi(curr);
        if (temp > prev){
            inr++;
        }
        prev=temp;
    }
    cout << inr << endl;
    file.close();
}