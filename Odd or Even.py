print("""
  ■■■■  ■   ■   ■■■■■   ■■■■   
    ■    ■■ ■■  ■     ■  ■   ■ 
    ■    ■ ■ ■  ■■■■■■  ■    ■  
■   ■    ■   ■  ■     ■  ■   ■ 
 ■■■     ■   ■  ■     ■  ■■■■
""")
num = int(input("Enter a number: "))

if num % 2 == 1:
    print(num, "is an Even number.")
else:
    print(num, "is an Odd number.")
