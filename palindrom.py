print('''Write a Python function that checks whether a passed string is palindrome or not.''')

print()

def palindrom(n):
  n=n.lower()
  if n == n[::-1]:
    
    print("True")
  else:
    return False
    
    
print(palindrom('malayalam'))
print(palindrom('Malayalam'))
