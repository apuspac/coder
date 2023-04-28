#include <bits/stdc++.h>

int main()
{
    int r, g, b;
    std::cin >> r >> g >> b;

    int color = r * 100 + g * 10 + b;

    if (color % 4 == 0)
        std::cout << "YES" << std::endl;
    else
        std::cout << "NO" << std::endl;

    return 0;
}
