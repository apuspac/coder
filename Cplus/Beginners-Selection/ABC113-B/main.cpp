
#include <bits/stdc++.h>

int main()
{
    int n, a, t;

    std::cin >> n;
    std::cin >> t >> a;

    std::vector<int> h(n);
    for (int i = 0; i < (n); ++i)
        std::cin >> h[i];

    int ans = -1;

    // 実行結果がdoubleになりそうなときは doubleにしてしまう
    double close_a = 1000;

    for (int i = 0; i < (n); ++i)
    {
        double av = t - h[i] * 0.006;

        // -を扱うときは absを頭にちらつかせる
        if (close_a > std::abs(a - av))
        {
            close_a = std::abs(a - av);
            ans = i;
        }
    }

    std::cout << ans + 1 << std::endl;
    return 0;
}
