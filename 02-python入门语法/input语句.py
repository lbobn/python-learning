user_name = input("请输入用户名")
user_type = input("请输入用户类型")

print(f"您好:{user_name}, 您是尊贵的: {user_type}用户, 欢迎您的光临")


def deleteDuplicates(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """

    node = head
    while node.next is not None and node is not None:
        if node.val == node.next.val:
            node.next = node.next.next
        else:
            node = node.next
    return head
