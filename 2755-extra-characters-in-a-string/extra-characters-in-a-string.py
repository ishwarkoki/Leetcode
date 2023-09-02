class Solution:
  def minExtraChar(self, s: str, dictionary: List[str]) -> int:
    final_n = len(s)
    dictionary_set = set(dictionary)

    # dp[i] := min extra characters if breaking up s[0:i] optimally
    dp = [final_n] * (final_n + 1)
    dp[0] = 0

    for i in range(1, final_n + 1):
      for j in range(0, i):
        # s[j..i) is in dictionarySet.
        if s[j:i] in dictionary_set:
          dp[i] = min(dp[i], dp[j])
        # s[j..i) are extra characters.
        else:
          dp[i] = min(dp[i], dp[j] + i - j)

    return dp[final_n]
