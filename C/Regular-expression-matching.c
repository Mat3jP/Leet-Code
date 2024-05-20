#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool isMatch(char *s, char *p)
{
    int s_len = strlen(s);
    int p_len = strlen(p);

    bool **dp = (bool **)malloc((s_len + 1) * sizeof(bool *));
    for (int i = 0; i < s_len + 1; i++)
    {
        dp[i] = (bool *)malloc((p_len + 1) * sizeof(bool));
    }

    for (int i = 0; i <= s_len; i++)
    {
        for (int j = 0; j <= p_len; j++)
        {
            dp[i][j] = false;
        }
    }

    dp[0][0] = true;

    for (int j = 1; j <= p_len; j++)
    {
        if (p[j - 1] == '*')
        {
            dp[0][j] = dp[0][j - 2];
        }
    }

    for (int i = 1; i <= s_len; i++)
    {
        for (int j = 1; j <= p_len; j++)
        {
            if (s[i - 1] == p[j - 1] || p[j - 1] == '.')
            {
                dp[i][j] = dp[i - 1][j - 1];
            }
            else if (p[j - 1] == '*')
            {
                dp[i][j] = dp[i][j - 2];
                if (p[j - 2] == '.' || p[j - 2] == s[i - 1])
                {
                    dp[i][j] = dp[i][j] || dp[i - 1][j];
                }
            }
        }
    }

    bool result = dp[s_len][p_len];

    for (int i = 0; i < s_len + 1; i++)
    {
        free(dp[i]);
    }
    free(dp);

    return result;
}
