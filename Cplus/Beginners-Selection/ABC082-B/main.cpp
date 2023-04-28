#include <bits/stdc++.h>

int main()
{
    std::string s, t;
    std::cin >> s;
    std::cin >> t;

    // s < t　ができるかどうかだけ 聞いているので、sを一番小さく、tを一番大きくすればいい。
    sort(s.begin(), s.end(), [&](char c1, char c2)
         { return c1 < c2; });
    sort(t.begin(), t.end(), [&](char c1, char c2)
         { return c1 > c2; });

    // 辞書順でとかいってるが、単なるs < t で勝手に比較してくれる。
    if (s < t)
        std::cout << "Yes" << std::endl;
    else
        std::cout << "No" << std::endl;

    return 0;
}

/**
 * sortの別回答
 * sort(s.begin(), s.end());
 * sort(t.begin(), t.end());
 * reverse(t.begin(), t.end());
 *
 */