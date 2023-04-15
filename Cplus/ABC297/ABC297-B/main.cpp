#include <iostream>
#include <vector>

int main()
{
    std::string chess;
    std::cin >> chess;

    int b1 = 0;
    int b2 = 0;
    int r1 = 0;
    int r2 = 0;
    int k = 0;

    bool b_flag = 0;
    bool r_flag = 0;

    for (int i = 0; i < 8; i++)
    {
        if (chess.at(i) == 'B')
        {
            if (b_flag == 0)
            {
                b1 = i;
                b_flag = 1;
            }
            else
            {
                b2 = i;
            }
        }
        if (chess.at(i) == 'R')
        {
            if (r_flag == 0)
            {
                r1 = i;
                r_flag = 1;
            }
            else
            {
                r2 = i;
            }
        }
        if (chess.at(i) == 'K')
        {
            k = i;
        }
    }

    if ((b1 % 2) == (b2 % 2))
    {
        std::cout << "No" << std::endl;
    }
    else if (!(r1 < k && r2 > k))
    {
        std::cout << "No" << std::endl;
    }
    else
    {
        std::cout << "Yes" << std::endl;
    }
    return 0;
}