#include <bits/stdc++.h>

int main()
{
    std::string s;
    std::cin >> s;

    int ans = 700;
    for (int i = 0; i < (3); ++i)
        if (s[i] == 'o')
            ans += 100;

    std::cout << ans << std::endl;
    return 0;
}
