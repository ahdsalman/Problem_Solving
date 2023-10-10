                        # <---Palindrome String--->

li = ['m', 'a', 'l', 'a', 'y', 'a', 'l', 'a', 'm']
is_palindrome = True

for x in range(len(li)):
    y =(len(li)-x-1)
    if li[x]!=li[y]:
        is_palindrome = False
        break
        
if is_palindrome:
    print("malayalam")
    
else:
    print("Not Palindrome")
    
    
li = ['m', 'a', 'l', 'a', 'y', 'a', 'l', 'a', 'm']
is_palindrome = True

for x in range(len(li)):
    for y in range(len(li),x + 1):
        if li[x] != li[y]:
            is_palindrome = False
            break

if is_palindrome:
    print("malayalam is a palindrome")
else:
    print("malayalam is not a palindrome")



s1 = "malayalam"

k1 = list(s1)
print(k1)


li = ['m', 'a', 'l', 'a', 'y', 'a', 'l', 'a', 'm']
is_palindrome = True

for x in range(len(li)):
    for y in range(len(li)-1, -1):
        if x != y and li[x]!=li[y]:
            is_palindrome = False
            break

if is_palindrome:
    print("Palindrome")
else:
    print("It is not Palindrome")
    

x = [1, 2, 3, 4, 5]
rev=x[::-1]
print(rev)

                    # <---Palindrome intiger--->

class Solution(object):
    def isPalindrome(self, x):
        x_str = str(x)
        lim = len(x_str)
        is_palindrome = True
        for i in range(lim):
            if x_str[i] != x_str[lim - i - 1]:
                is_palindrome = False
                break

        if is_palindrome:
            return True
        
        else:
            return False