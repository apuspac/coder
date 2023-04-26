#include <bits/stdc++.h>

int main()
{
    std::string a;
    std::cin >> a;

    int count = 0;
    for (int i = 0; i < int(a.size()); ++i)
        if (a[i] == '1')
            count++;

    std::cout << count << std::endl;
    return 0;
}
