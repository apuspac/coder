#include <bits/stdc++.h>

int main()
{
    std::string s;
    std::cin >> s;

    int count = int(s.size()) - 2;
    std::string count_str = std::to_string(count);

    std::string ans;

    ans += s[0];
    ans += count_str;
    ans += s.back();

    std::cout << ans << std::endl;

    return 0;
}

/**
 * ans
 * stringの最後にはnull文字があるので、 lengthはそのままで良いし、最後は-1する必要がある。
 *
 * std::string s;
 * std::cin >> s;
 *
 * int n = s.length();
 *
 * std::cout << s[0] << n -2 << s[n-1] << std::endl;
 *
 */