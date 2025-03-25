class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        idx_word, idx_abbr = 0, 0
        while idx_abbr < len(abbr) and idx_word < len(word):
            if abbr[idx_abbr].isalpha():
                if abbr[idx_abbr] != word[idx_word]:
                    return False
                else:
                    idx_word += 1
                    idx_abbr += 1
              
            elif abbr[idx_abbr].isdigit():
                if abbr[idx_abbr] == '0':
                    return False
                
                idx_digit = idx_abbr
                while idx_abbr < len(abbr) and abbr[idx_abbr].isdigit():
                    idx_abbr += 1
                
                replace_int = int(abbr[idx_digit : idx_abbr])
                
                if int(abbr[idx_digit : idx_abbr]) > len(word) - idx_word:
                    return False
                
                idx_word += replace_int

        return idx_word == len(word) and idx_abbr == len(abbr)

# Complexity Analysis

# Time complexity : O(n).

# Space complexity : O(1). No additional space is used.