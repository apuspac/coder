#include <iostream>
#include <vector>

int main()
{
    int n, d, j;
    std::vector<int> time_log;

    std::cin >> n >> d;

    while (std::cin >> j)
    {
        time_log.push_back(j);
    }

    int click_time = -1;
    for (int i = 0, k = 1; i < (n - 1); i++, k++)
    {

        // std::cout << time_log.at(k) - time_log.at(i) << std::endl;
        if ((time_log.at(k) - time_log.at(i)) <= d)
        {
            click_time = time_log.at(k);
            break;
        }
    }

    std::cout << click_time << std::endl;

    return 0;
}