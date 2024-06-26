def classifyTriangle(a, b, c):
    if a > 200 or b > 200 or c > 200 or a <= 0 or b <= 0 or c <= 0:
        return "invalidInput"
    elif a+b <= c or a+c <= b or b+c <= a:
        return "not a triangle"
    elif a == b and b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    else:
        return "scalene"

def main():
    a = int(input("Enter side a: "))
    b = int(input("Enter side b: "))
    c = int(input("Enter side c: "))
    print(classifyTriangle(a, b, c))
    
if __name__ == "__main__":
    main()