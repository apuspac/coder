#include <bits/stdc++.h>

int main()
{
    int n;
    std::cin >> n;

    std::cout << ((n % 2 == 0) ? (n / 2) : ((n / 2) + 1)) << std::endl;
    return 0;
}
