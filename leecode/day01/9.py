class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            num = 0
            if len(str(x)) % 2 == 0:
                st = "0" + str(x)
                for i in range(1, int(len(st)/2) + 1):
                    j = int('-' + str(i))
                    if st[i] == st[j]:
                        pass
                    else:
                        num += 1
                if num != 0:
                    return False
                else:
                    return True
            else:
                st = "0" + str(x)
                for i in range(1, int(len(st)/2)):
                    j = int('-' + str(i))
                    if st[i] == st[j]:
                        pass
                    else:
                        num += 1
                if num != 0:
                    return False
                else:
                    return True


if __name__ == '__main__':
    so = Solution()
    print(so.isPalindrome(1000021))
