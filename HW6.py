class Solution:
    def reverse(self, x: int) -> int:
        if 0>x:
            negetive=True
        else:
            negetive=False
        x=abs(x)
        x_str=str(x)
        if int(x_str[::-1])>2147483647 or int(x_str[::-1])<-2147483648:
            return 0
        if negetive:
            return int(x_str[::-1])*(-1)
        else:
            return int(x_str[::-1])
