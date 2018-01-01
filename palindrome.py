def is_palindrome(s):
    t = str(s)
    if t[::-1] == t:
        return s


r = (filter(is_palindrome,range(1, 200)))
print(list(r))
