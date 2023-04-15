#include <iostream>
#include <vector>

int main()
{
    int h, w;

    std::cin >> h >> w;

    std::vector<std::vector<std::string>> heya(h, std::vector<std::string>(w));

    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j < w; j++)
        {
            std::cin >> heya.at(i).at(j);
        }
    }

    for (auto ele & : heya)
    {
        std::cout << ele << std::endl;
    }

    return 0;
}