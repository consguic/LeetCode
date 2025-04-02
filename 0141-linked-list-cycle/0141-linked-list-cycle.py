class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head  # Yavaş işaretçi
        fast = head  # Hızlı işaretçi

        while fast and fast.next:  # Fast veya fast.next None olursa döngü yoktur
            slow = slow.next       # Slow her seferinde 1 düğüm ilerler
            fast = fast.next.next   # Fast her seferinde 2 düğüm ilerler
            
            if slow == fast:  # İki işaretçi aynı düğümde buluşursa döngü var
                return True
        
        return False  # Döngü bulunmazsa False
