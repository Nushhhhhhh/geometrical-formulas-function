# 2D Shapes

def rectangle_area(l, w):
    return l * w

def rectangle_perimeter(l, w):
    return 2 * (l + w)

def square_area(a):
    return a ** 2

def square_perimeter(a):
    return 4 * a

def equilateral_triangle_area(a):
    return (3 ** 0.5 / 4) * a ** 2

def equilateral_triangle_perimeter(a):
    return 3 * a

def triangle_area(b, h):
    return 0.5 * b * h

def triangle_perimeter(a, b, c):
    return a + b + c 

def heron_triangle(a, b, c):
    s = (a + b + c) / 2
    return (s * (s-a) * (s-b) * (s-c)) ** 0.5

def parallelogram_area(b, h):
    return b * h

def parallelogram_perimeter(a, b):
    return 2 * (a + b)

def rhombus_area(d1, d2):
    return 0.5 * d1 * d2

def rhombus_perimeter(a):
    return 4 * a

def kite_area(d1, d2):
    return 0.5 * d1 * d2

def kite_perimeter(a , b):
    return 2 * (a + b)

def trapezium_area(a, b, h):
    return 0.5 * (a + b) * h

def trapezium_perimeter(a, b, c, d):
    return a + b + c + d 

def circle_area(r):
    return 3.14 * r ** 2

def circle_circumference(r):
    return 2 * 3.14 * r

def semicircle_area(r):
    return 0.5 * 3.14 * r ** 2

def semicircle_primeter(r):
    return 3.14 * r + 2 * r

def quartercircle_area(r):
    return 0.25 * 3.14 * r ** 2

def quatercircle_perimeter(r):
    return 0.5 * 3.14 * r + 2 * r

def circular_sector_area(theta, r):
    return (theta / 360) * 3.14 * r ** 2

def circular_sector_arc(theta, r):
    return (theta / 360) * 2 * 3.14 * r 

def circular_segment_area(sector, triangle):
    return sector - triangle

def annulus_area(R, r):
    return 3.14 * (R ** 2 - r ** 2)

def outer_circumference(R):
    return 2 * 3.14 * R

def inner_circumference(r):
    return 2 * 3.14 * r

def ellipse_area(a, b):
    return 3.14 * a * b

def polygon_area(apothem, perimeter):
    return 0.5 * apothem * perimeter

def polygon_perimeter(n,a):
    return n * a 

def hexagon_area(a):
    return (3 * (3 ** 0.5) / 2) * a ** 2

def heaxagon_perimeter(a):
    return 6 * a

def pentagon_area(a):
    return (1/4) * (5 * (5 + 2 * (5 ** 0.5))) ** 0.5 * a ** 2

def pentagon_perimeter(a):
    return 5 * a

def octagon_area(a):
    return 2 * (1 + (2 ** 0.5)) * a ** 2

def octagon_perimeter(a):
    return 8 * a
    
# 3D Shapes

def cube_volume(a):
    return a ** 3

def cube_tsa(a):
    return 6 * a ** 2

def cuboid_volume(l, w, h):
    return l * w * h

def cuboid_tsa(l, w, h):
    return 2 * (l*w + l*h + w*h)

def cylinder_volume(r, h):
    return 3.14 * r ** 2 * h

def cylinder_tsa(r, h):
    return 2 * 3.14 * r * (r + h)

def hollow_cylinder_volume(R, r, h):
    return 3.14 * h * (R ** 2 - r ** 2)

def hollow_cylinder_tsa(R, r, h):
    return 2 * 3.14 * (R + r) * h + 2 * 3.14 * (R ** 2 - r ** 2)

def sphere_volume(r):
    return (4/3) * 3.14 * r ** 3

def sphere_tsa(r):
    return 4 * 3.14 * r ** 2

def hemisphere_volume(r):
    return (2/3) * 3.14 * r ** 3

def hemisphere_tsa(r):
    return 3 * 3.14 * r ** 2

def cone_volume(r, h):
    return (1/3) * 3.14 * r ** 2 * h

def cone_tsa(r, s):
    return 3.14 * r * (r + s)

def frustum_of_cone_volume(R, r, h):
    return (1/3) * 3.14 * h * (R ** 2 + R*r + r ** 2)

def frustum_of_cone_tsa(R, r, s):
    return 3.14 * (R + r) * s + 3.14 * (R ** 2 + r ** 2)

def prism_volume(base_area, h):
    return base_area * h

def prism_tsa(B, P, h):
    return 2 * B + P * h

def triangular_prism_volume(b, h, l):
    return 0.5 * b * h * l

def triangular_prism_tsa(triangle_area, l, a, b, c):
    return 2 * (triangle_area + l * (a + b + c))

def pyramid_volume(base_area, h):
    return (1/3) * base_area * h

def pyramid_tsa(B, P, s):
    return B + 0.5 * P * s

def square_pyramid_volume(a, h):
    return (1/3) * a ** 2 * h

def square_pyramid_tsa(a, s):
    return a ** 2 + 2 * a * s

def rectangular_pyramid_volume(l, w, h):
    return (1/3) * l * w * h

def rectangular_pyramid_tsa(l, w, s1, s2):
    return l*w + l*s1 + w*s2

def frustum_of_pyramid_volume(A1, A2, h):
    return (h/3) * (A1 + A2 + (A1*A2) ** 0.5)

def tetrahedron_tsa(a):
    return (3 ** 0.5) * a ** 2

def ellipsoid_volume(a, b, c):
    return (4/3) * 3.14 * a * b * c

def octahedron_tsa(a):
    return 2 * (3 ** 0.5) * a ** 2