class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """ 
        """
        newHead = ListNode(0)
        newP = newHead
        p1, p2 = l1, l2
        while p1 or p2:
            # 1. 找到操作数 a, b , 进位 jin， 并计算当前计算的进位
            a = p1.val if p1 else 0
            b = p2.val if p2 else 0
            div = (a + b + newP.val) % 10
            jin = (a + b + newP.val) // 10
            # 2. 更新指针后移, 要注意 p1, p2 为 None的判断，不可前移
            if p1: p1 = p1.next 
            if p2: p2 = p2.next
            # 3. 赋值
            newP.val = div
            # 4. 判断是否需要创建新节点
            if p1 or p2 or jin > 0:
                newP.next = ListNode(jin)
                newP = newP.next
        
        return newHead
