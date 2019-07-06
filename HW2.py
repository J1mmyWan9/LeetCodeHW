# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result=ListNode(0)
        l3_now=result
        carry=False
        l3_value=0
        while None!=l1 or None!=l2 or carry:
            if None!=l1:#如果還有l1，取出值，換下一個l1
                l1_value=l1.val
                l1=l1.next
            else:
                l1_value=0
            if None!=l2:#如果還有l2，取出值，換下一個l2     
                l2_value=l2.val
                l2=l2.next
            else:
                l2_value=0                
            l3_value=l1_value+l2_value#兩項相加
            if carry:#若前項有進位，補1
                l3_value+=1
                carry=False               
            if 10<=l3_value:#若本項結果需要進位，-10
                carry=True
                l3_value=l3_value-10            
            l3_now.next=ListNode(l3_value)#將本項結果放入輸出LinkedlList
            l3_now=l3_now.next      
        return result.next
