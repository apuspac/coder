#include <bits/stdc++.h>

int main()
{
    int n;
    std::cin >> n;

    // 0が答えに含まれそうな場合 -1からはじめたほうがいいかも。
    int max_n = -1;
    int ans = -1;
    for (int i = 1; i <= (n); ++i)
    {
        int count = 0;
        int ii = i;
        while (ii % 2 == 0)
        {
            ii /= 2;
            count++;
        }
        if (count > max_n)
        {
            max_n = count;
            ans = i;
        }
    }

    std::cout << ans << std::endl;
    return 0;
}
