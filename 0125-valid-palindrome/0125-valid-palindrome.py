class Solution(object):
    def isPalindrome(self, s):
        cleaned = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        if cleaned == cleaned[::-1]:
            return True
        else:
            return False
        