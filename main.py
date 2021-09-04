import polygon_calculator

print("\n\n====Polygon Calculator====\n\n ===By Abhijith Ashokan===")
print("\nPress 1 for Rectangle and 2 for Square:")
ch=int(input())
if ch == 1:
    w = int(input("Enter Width:"))
    h = int(input("Enter height:"))
    rect = polygon_calculator.Rectangle(w,h)
    print("Press:\n1. for area\n2. for perimeter\n 3. set width\n4. set height\n5. get width\n6. get height\n7. diagonal  ")
    c = int(input())
    if c == 1:
        print("Area=")
        print(rect.get_area())
    elif c == 2:
        print("Perimeter=")
        print(rect.get_perimeter())
    elif  c== 3:
        wid = input("Enter width:")
        rect.set_width(wid)
    elif c == 4:
        hei = input("Enter Height:")
        rect.set_height(hei)
    elif c == 5:
        print("Width=")
        print(rect.get_width)
    elif c == 6:
        print("Height = ")
        print(rect.get_height)
    
    elif c == 7:
        print(rect.diagonal)
   
    
    print(rect)

elif ch == 2:
    s = int(input("Enter Side:"))
    sq = polygon_calculator.Square(s)
    print("Press:\n1. for area\n2. for perimeter\n 3. set width\n4. set height\n5. get width\n6. get height\n7. diagonal")
    c = int(input())
    if c == 1:
        print("Area=")
        print(sq.get_area())
    elif c == 2:
        print("Perimeter=")
        print(sq.get_perimeter())
    elif  c== 3:
        wid = input("Enter width:")
        sq.set_width(wid)
    elif c == 4:
        hei = input("Enter Height:")
        sq.set_height(hei)
    elif c == 5:
        print("Width=")
        print(sq.get_width)
    elif c == 6:
        print("Height = ")
        print(sq.get_height)
    
    elif c == 7:
        print(sq.diagonal)
    # print(sq.get_area())
    # sq.set_side(4)
    # print(sq.get_diagonal())
    # print(sq)
else :
    print("Invalid Choice")
