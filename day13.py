"""
fibanocci
------------------
num=0
num1=1
def fib(num, num1):
    limit=int(input("enter val:"))
    print(num, num1, end=" ")
    for i in range(1, limit):
        num2=num+num1
        num=num1
        num1=num2
        print(num2, end=" ")
fib(num, num1)

def removee(numbers):
    a = []
    for i in numbers:
        if i not in a:
            a.append(i)
    return a
nums = [1, 2, 3, 2, 4, 1, 5]
print(remove_duplicates(nums))


def word(so, count):
    for j in so:
        count+=1
    print(count)
word(so, count)
"""


def words(sentence):
    words = sentence.split()
    return len(words)

text = input("Enter sentence: ")

print("Number of words:", words(text))
