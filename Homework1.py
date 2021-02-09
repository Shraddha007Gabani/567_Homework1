def Classify_triangle(a,b,c):
    """check the triangle type"""

    if(a>0 and b>0 and c>0):

        if a==b and b==c and a==c:
            return "Equilateral triangle"

        elif (a==b and a!=c) or (a==c and a!=b):
            return "Isoscale triangle"

        elif (a*a + b*b == c*c) or ( a*a + c*c == b*b) or (b*b + c*c == a*a):
            return "right triangle"

        else:
            return "scalene triangle"
    else:
        return "can't form triangle"

def main():
    """take the input"""

    a= float(input("enter value of a"))
    b= float(input("enter the value of b"))
    c= float(input("enetr the value of c"))
    result = Classify_triangle(a,b,c)
    print(result)

if __name__ == "__main__":
    main()
