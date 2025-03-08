print("""
  ■■■■  ■   ■   ■■■■■   ■■■■   
    ■    ■■ ■■  ■     ■  ■   ■ 
    ■    ■ ■ ■  ■■■■■■  ■    ■  
■   ■    ■   ■  ■     ■  ■   ■ 
 ■■■     ■   ■  ■     ■  ■■■■
""")
def Define_age(age):
    if age < 0:
        print("Invalid age.")
    else:
        if age > 64:
            print("You are a Senior.")
        else:
            if age > 19:
                print("You are an Adult.")
            else:
                if age > 12:
                    print("You are a Teen.")
                else:
                    print("You are a Child.")


age = int(input("Enter your age: "))
Define_age(age)

