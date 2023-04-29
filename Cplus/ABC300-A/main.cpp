#include <bits/stdc++.h>

int main()
{
    int n, a, b;
    std::cin >> n >> a >> b;

    std::vector<int> c(n);
    for (int i = 0; i < (n); ++i)
        std::cin >> c[i];

    int plus = a + b;
    for (int i = 0; i < (n); ++i)
    {
        if (c[i] == plus)
        {
            std::cout << i + 1 << std::endl;
            break;
        }
    }
    return 0;
}
