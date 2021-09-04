import polygon_calculator


def test_get_width():
    test = polygon_calculator.Rectangle(5,10)
    assert test.get_width() == 5
    test = polygon_calculator.Rectangle(8,10)
    assert test.get_width() == 8

def test_get_height():
    test = polygon_calculator.Rectangle(5,10)
    assert test.get_height() == 10
    test = polygon_calculator.Rectangle(5,12)
    assert test.get_height() == 12

def test_get_area():
    test = polygon_calculator.Rectangle(5,10)
    assert test.get_area() == 50 
    test = polygon_calculator.Rectangle(5,12)
    assert test.get_area() == 60

def test_get_perimeter():
    test = polygon_calculator.Rectangle(5,10)
    assert test.get_perimeter() == 30
    test = polygon_calculator.Rectangle(8,12)
    assert test.get_perimeter() == 40

def test_get_diagonal():
    test = polygon_calculator.Rectangle(5,10)
    assert test.get_diagonal() == 11.180339887498949
    test = polygon_calculator.Rectangle(12,10)
    assert test.get_diagonal() == 15.620499351813308

def test_rectangle_picture():
    test = polygon_calculator.Rectangle(7,3)
    assert test.get_picture() == "*******\n*******\n*******\n"
def test_square_picture():
    test = polygon_calculator.Square(2 == "**\n**\n")


def test_big_picture():
    test = polygon_calculator.Rectangle(51,3)
    assert test.get_picture() == "Too big for picture."

def test_is_subclass():
    assert issubclass(polygon_calculator.Square, polygon_calculator.Rectangle) == True

def test_square_is_square_and_rectangle():
    test = polygon_calculator.Square(5)
    assert  isinstance(test, polygon_calculator.Square) and isinstance(test, polygon_calculator.Square) == True

def test_square_string():
    test = polygon_calculator.Square(5)
    assert str(test) == "Square(side=5)"

def rectangle_string():

    test = polygon_calculator.Rectangle(3, 6)
    assert str(test) == "Rectangle(width=5, height=10)"    

def test_get_amount_inside():
    testrect = polygon_calculator.Rectangle(30, 16)
    testsq = polygon_calculator.Square(5)
    assert testrect.get_amount_inside(testsq) == 18

def test_get_amount_inside_two_rectangles():
    test = polygon_calculator.Rectangle(3,6)
    rect2 = polygon_calculator.Rectangle(4, 8)
    assert rect2.get_amount_inside(test) == 1
 