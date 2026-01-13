class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # Find maximum window in middle such that remaining chars have at least k of each
        # Time: O(n), Space: O(1)
        
        n = len(s)
        count = {'a': 0, 'b': 0, 'c': 0}
        
        # Count total characters
        for c in s:
            count[c] += 1
        
        # Check if solution exists
        if count['a'] < k or count['b'] < k or count['c'] < k:
            return -1
        
        if k == 0:
            return 0
        
        # Find maximum window we can remove from middle
        # Window must leave at least k of each char outside
        # i.e., window can have at most (count[c] - k) of each char
        max_removable = {c: count[c] - k for c in 'abc'}
        
        max_window = 0
        window = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        
        for right in range(n):
            window[s[right]] += 1
            
            # Shrink window if any character exceeds limit
            while window['a'] > max_removable['a'] or window['b'] > max_removable['b'] or window['c'] > max_removable['c']:
                window[s[left]] -= 1
                left += 1
            
            max_window = max(max_window, right - left + 1)
        
        return n - max_window