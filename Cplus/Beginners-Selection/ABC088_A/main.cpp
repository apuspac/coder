#include <bits/stdc++.h>

int main()
{
    int n, a;
    std::cin >> n >> a;

    if (n % 500 <= a)
        std::cout << "Yes" << std::endl;
    else
        std::cout << "No" << std::endl;
    return 0;
}
