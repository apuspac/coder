#include <bits/stdc++.h>

int main()
{
    int n;
    std::cin >> n;
    std::vector<int> A(n);
    for (int i = 0; i < (n); ++i)
        std::cin >> A[i];

    bool flag = false;
    int count = 0;
    while (true)
    {
        for (int i = 0; i < (n); ++i)
            if (A[i] % 2 != 0)
                flag = true;

        // flagはboolにすると ==0とかの処理がいらない
        if (flag)
            break;
        else
            for (int i = 0; i < (n); ++i)
                A[i] /= 2;

        ++count;
    }
    std::cout << count << std::endl;
    return 0;
}
