class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 0
        
        # Check every possible starting position
        for i in range(n):
            counts = [0] * 26
            distinct_chars = 0
            
            # Extend the substring from i to j
            for j in range(i, n):
                char_idx = ord(s[j]) - ord('a')
                
                # If this is a new character, increment our distinct count
                if counts[char_idx] == 0:
                    distinct_chars += 1
                counts[char_idx] += 1
                
                # The length of the current substring s[i:j+1]
                current_len = j - i + 1
                
                if current_len % distinct_chars == 0:
                    target_freq = current_len // distinct_chars
                    
                    is_balanced = True
                    # Only check the characters we've actually seen
                    for k in range(26):
                        if counts[k] > 0 and counts[k] != target_freq:
                            is_balanced = False
                            break
                    
                    if is_balanced:
                        max_len = max(max_len, current_len)
                        
        return max_len