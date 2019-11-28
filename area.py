from math import sqrt, pi


# Contains Area Calculating Functions

# Triangles

#Equilateral Triangle
def equtri_area(a: int) -> 'area':
    '''
    This Function Is For Equilateral Triangle's Area Calculation.
    Takes 'a' As Side Of The Triangle.
    :param a: int
    :return: area
    '''
    area = (sqrt(3) / 4) * pow(a, 2)
    return area

#Right Angle Triangle
def righttri_area(b: int, h: int) -> 'area':
    '''
    This Function Is For Right Angled Triangle's Area Calculation.
    Takes 'h' As Height & 'b' As The Base Of The Right Angled Triangle.
    And Returns The (approx)Area.
    :param h: int
    :param b: int
    :return: area
    '''
    area = 1 / 2 * b * h
    return area

#Acute Triangle
def acute_triangle_area(a: int, b: int, c: int) -> 'area':
    '''
    This Function Is For Acute Angled Triangle's Area Calculation.
    Takes 'a','b','c' As Length Of Side.
    And Divides The Sum Of The Three Integers By 2.
    And Returns The(approx) Area.
    :param a: int
    :param b: int
    :param c: int
    :return: area
    '''
    s = (a + b + c) / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    return area

#Obtuse Triangle
def obtuse_triangle_area(a: int, b: int, c: int) -> 'area':
    '''
        This Function Is For Obtuse Angled Triangle's Area Calculation.
        Takes 'a','b','c' As Length Of Side.
        And Divides The Sum Of The Three Integers By 2.
        And Returns The(approx) Area.
        :param a: int
        :param b: int
        :param c: int
        :return: area
        '''
    s = (a + b + c) / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    return area


# Quadrilaterals

#Square
def square_area(a: int) -> 'area':
    '''
    This Function Is For Square's Area Calculation.
    Takes 'a' As Length Of The Side.
    And Returns The Area.
    :param a: int
    :return: area
    '''
    area = pow(a, 2)
    return area

#Rectangle
def rectangle_area(l: int, b: int) -> 'area':
    '''
       This Function Is For Rectangle's Area Calculation.
       Takes 'a' As Length Of The Side.
       And Returns The Area.
       :param l: int
       :param b: int
       :return: area
       '''
    area = l * b
    return area

#Parallelogram
def parallelogram_area(b: int, h: int) -> 'area':
    '''
    This Function Is For Parallelogram's Area Calculation.
Takes 'b' As The Base And 'h' As The Height.
    And Returns The Area.
    :param b: int
    :param h: int
    :return: area
    '''
    area = b * h
    return area

#Rhombus
def rhombus_area(do: int, ds: int) -> 'area':
    '''
    This Function Is For Rhombus's Area Calculation.
    Takes 'do' As The First Diagonal And 'ds' As The Second Diagonal.
    And Returns The Area.
    :param do: int
    :param ds: int
    :return:
    '''
    area = 1 / 2 * do * ds
    return area


def trapezium_area(a: int, b: int, h: int) -> 'area':
    '''
    This Function Is For Trapezium's Area Calculation.
    Takes 'a'&'b' As The Length Of The Parallel Sides And 'h' As The Height.
    And Returns The Area.
    :param a: int
    :param b: int
    :param h: int
    :return: area
    '''
    area = 1 / 2 * (a + b) * h
    return area


# Circles

#Full Circle
def circle_area(r: int) -> 'area':
    '''
    This Function Is For Circle's Area Calculation.
    Takes 'r' As The Radius Of The Circle.
    And Returns The Area.
    :param r:
    :return: Area
    '''
    area = pi * (pow(r, 2))
    return area

#Semicircle
def semicircle_area(r: int) -> 'area':
    """
    This Function Is For Semicircle's Area Calculation.
    Takes 'r' As The Radius Of The semicircle.
    And Returns The Area.
    :param r: int
    :return: area
    """
    area = 1 / 2 * (circle_area(r))
    return area


def cirsector_area(r: int, a: int) -> 'area':
    """
    This Function Is For Circular Sector's Area Calculation.
    Takes 'r' As The Radius Of The Circular Sector.
    And Returns The Area.
    :param r: int
    :param a: int
    :return: area
    """
    length = (a / 360) * 2 * pi * r
    area = 1 / 2 * length * r
    return area

#Ring
def cirring_area(ro: int, rs: int != 1) -> 'area':
    """
    This Function Is For Circular Ring's Area Calculation.
    Takes 'ro'(Radius Of The Outer Circle),
    'rs'(Radius Of The Inner Circle) As The Radii Of The Circular Ring.
    And Returns The Area.
    :param ro: int
    :param rs: int
    :return: area
    """
    area = pi * (pow(ro, 2) - pow(rs, 2))
    return area

#Ellipse
def ellipse_area(a: int, b: int != 1) -> 'area':
    """
    This Function Is For Ellipse's Area Calculation.
    Takes 'a' & 'b' As The Length Of Major And Minor Axis Respectively.
    And Returns The Area.
    :param a: float
    :param b: float
    :return: area
    """
    area = pi * a * b
    return area
