class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        tokens.sort()  # Sorting tokens to facilitate two-pointer approach
        left, right = 0, len(tokens) - 1
        score = 0
        max_score = 0

        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                left += 1
                score += 1
                max_score = max(max_score, score)
            elif score > 0:
                power += tokens[right]
                right -= 1
                score -= 1
            else:
                break

        return max_score