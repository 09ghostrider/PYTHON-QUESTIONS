print("\n----------------------------------------------------------------------------------------------------\n")

print("1. Write a Python class to convert an integer to a roman numeral\n\nSOLUTION:")

class Int_Roman:
    def IR(self, num):
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syb = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman_num = ''
        i = 0

        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

number = 100
print(f"NUMBER: {number}\nROMAN NUMBER: {Int_Roman().IR(number)}")

print("\n----------------------------------------------------------------------------------------------------\n")

print("2. Write a Python class to convert a roman numeral to an integer\n\nSOLUTION:")

class Roman_Int:
    def RI(self, num):
        val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        Number = 0
        for i in range(len(num)):
            if i > 0 and val[num[i]] > val[num[i - 1]]:
                Number += val[num[i]] - 2 * val[num[i - 1]]
            else:
                Number += val[num[i]]
        return Number

roman = "C"
print(f"ROMAN NUMBER: {roman}\nNUMBER: {Roman_Int().RI(roman)}")

print("\n----------------------------------------------------------------------------------------------------\n")

print("3. Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These brackets must be close in the correct order, for example () and ()[]{} are valid but [), ({[)] and {{{ are invalid.\n\nSOLUTION:")

class Check_Valid:
  def check(S):
    open = ["[","{","("] 
    close = ["]","}",")"] 
    list1 = [] 
    for i in S: 
      if i in open: 
        list1.append(i) 
      elif i in close: 
        pos = close.index(i) 
        if ((len(list1) > 0) and
          (open[pos] == list1[len(list1) - 1])): 
          list1.pop()
        else: 
          return "INVALID"
    if len(list1) == 0: 
      return "VALID"
    else: 
      return "INVALID"

string = "{[]{()}}"
print(f"PARENTHESES: {string}\nVALIDITY: {Check_Valid.check(string)}")

print("\n----------------------------------------------------------------------------------------------------\n")

print("""4. Write a Python class to get all possible unique subsets from a set of distinct integers.
Input : [4, 5, 6]
Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]\n\nSOLUTION:""")

class Subsets:
    def unique_sets(self, Set):
        return self.subset([], sorted(Set))
    
    def subset(self, current, Set):
        if Set:
            return self.subset(current, Set[1:]) + self.subset(current + [Set[0]], Set[1:])
        return [current]

list1 = [4, 5, 6]
print(f"INPUT: {list1}\nOUTPUT: {Subsets().unique_sets(list1)}")

print("\n----------------------------------------------------------------------------------------------------\n")

print("5. Write a Python class to implement pow(x, n).\n\nSOLUTION:")

class Implement:
  def Pow(x, n):
    return pow(x, n)

num1 = 2
num2 = 2
print(f"\n'{num1}' TO THE POWER '{num2}' IS '{Implement.Pow(num1, num2)}'")

print("\n----------------------------------------------------------------------------------------------------\n")

print("6. Write a Python class to reverse a string word by word.\n\nSOLUTION:")

class Reverse:
    def words(Str):
        return ' '.join(reversed(Str.split()))

words = "I AM GHOST"
print(f"STRING: {words}\nREVERSE STRING: {Reverse.words(words)}")

print("\n----------------------------------------------------------------------------------------------------\n")
