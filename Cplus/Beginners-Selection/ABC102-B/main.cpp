#include <bits/stdc++.h>

int main()
{
    int n;
    std::cin >> n;

    std::vector<int> a(n);
    for (int i = 0; i < (n); ++i)
        std::cin >> a[i];

    sort(a.begin(), a.end());

    std::cout << a[n - 1] - a[0] << std::endl;
    return 0;
}

// 最大値 最小値を求めるとしても良い。
// vectorのスニペットは入力も作っていいかもなー