#include <bits/stdc++.h>

int main()
{
    int h, w;
    std::cin >> h >> w;

    std::vector<std::vector<char>> rpg_1(h, std::vector<char>(w));
    std::vector<std::vector<char>> rpg_2(h, std::vector<char>(w));
    for (int i = 0; i < (h); ++i)
        for (int j = 0; j < (w); ++j)
            std::cin >> rpg_1.at(i).at(j);
    for (int i = 0; i < (h); ++i)
        for (int j = 0; j < (w); ++j)
            std::cin >> rpg_2.at(i).at(j);

    auto print = [](std::vector<std::vector<char>> &s)
    {
        for (auto i : s)
        {
            for (auto v : i)
            {
                std::cout << v;
            }

            std::cout << std::endl;
        }
    };
    bool no_flag = true;
    for (int i = 0; i < (h - 1); ++i)
    {
        for (int j = 0; j < (w - 1); ++j)
        {

            // tate
            for (int k = 0; k < (j); ++k)
            {
                for (int l = 0; l < (w); ++l)
                {
                    std::rotate(rpg_1.at(l).begin(), rpg_1.at(l).begin() + 1, rpg_1.at(l).end());
                }
            }
            // yoko
            for (int k = 0; k < (i); ++k)
            {

                std::rotate(rpg_1.begin(), rpg_1.begin() + 1, rpg_1.end());
            }

            bool ok_flag = true;
            for (int k = 0; k < (h); ++k)
            {
                if (rpg_1.at(k) != rpg_2.at(k))
                {
                    ok_flag = false;
                }
            }

            if (ok_flag)
            {
                std::cout << "Yes" << std::endl;
                no_flag = false;
                break;
            }
        }
    }
    if (no_flag)
        std::cout << "No" << std::endl;

    return 0;
}
