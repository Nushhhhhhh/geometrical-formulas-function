import streamlit as st  
from Mathematical_formulas import * 

st.title("Solve Geometrical Problems")

shapes = st.radio("Select the shape of your choice", ("2D Shape", "3D Shape"))

if shapes == "2D Shape":
    cal = st.radio("Select the figure", ("Rectangle", "Square", "Triangle","Parallelogram","Rhombus", "Kite", "Trapezium", "Circle","Polygon", "Hexagon", "Pentagon", "Octagon"))

    if cal == "Rectangle":
        per =  st.radio("Select the calculation", ("Area", "Perimeter"))
        if per == "Area":
            l = st.number_input("Enter the length of the rectangle")
            w = st.number_input("Enter the width of the rectangle")
            area = rectangle_area(l, w)
            st.write(f"The area of the rectangle is: {area}")
        elif per == "Perimeter":
            l = st.number_input("Enter the length of the rectangle")
            w = st.number_input("Enter the width of the rectangle") 
            perimeter = rectangle_perimeter(l, w)
            st.write(f"The perimeter of the rectangle is: {perimeter}")

    elif cal == "Square":
        per =  st.radio("Select the calculation", ("Area", "Perimeter"))
        if per == "Area":
            a = st.number_input("Enter the length of the square")
            area = square_area(a)
            st.write(f"The area of the square is: {area}")
        elif per == "Perimeter":
            a = st.number_input("Enter the length of the cube")
            perimeter = square_perimeter(a)
            st.write(f"The perimeter of the square is: {perimeter}")
        
    elif cal == "Triangle":
        tri = st.radio("Select the triangle", ("Equilateral Triangle", "Isoceles/Scalene Triangle"))
        if tri == "Equilateral Triangle":
            per =  st.radio("Select the calculation", ("Area", "Perimeter"))
            if per == "Area":
                a = st.number_input("Enter the length of the side of the triangle")
                area = equilateral_triangle_area(a)
                st.write(f"The area of the equilateral triangle is: {area}")
            elif per == "Perimeter":
                a = st.number_input("Enter the length of the side of the triangle")
                perimeter = equilateral_triangle_perimeter(a)
                st.write(f"The perimeter of the equilateral triangle is: {perimeter}")
        elif tri == "Isoceles/Scalene Triangle":
            per =  st.radio("Select the calculation", ("Area", "Heron's Area", "Perimeter"))
            if per == "Area":
                b = st.number_input("Enter the base of the triangle")
                h = st.number_input("Enter the height of the triangle")
                area = triangle_area(b, h)
                st.write(f"The area of the triangle is: {area}")
            if per == "Perimeter":
                a = st.number_input("Enter side of the triangle", key="side1")
                b = st.number_input("Enter another side of the triangle", key="side2")
                c = st.number_input("Enter the third side of the triangle", key="side3")
                perimeter = triangle_perimeter(a, b, c)
                st.write(f"The perimeter of the triangle is: {perimeter}")
            if per == "Heron's Area":
                a = st.number_input("Enter side of the triangle", key="side1")
                b = st.number_input("Enter another side of the triangle", key="side2")
                c = st.number_input("Enter the third side of the triangle", key="side3")
                h_area = heron_triangle(a, b, c)
                st.write(f"The herons's area of the triangle is: {h_area}")

    elif cal == "Parallelogram":
        per =  st.radio("Select the calculation", ("Area", "Perimeter"))
        if per == "Area":
            b = st.number_input("Enter the base of the parallelogram")
            h = st.number_input("Enter the height of the parallelogram")
            area = parallelogram_area(b, h)
            st.write(f"The area of the parallelogram is: {area}")
        if per == "Perimeter":
            a = st.number_input("Enter side of the parallelogram", key="side1")
            b = st.number_input("Enter another side of the parallelogram", key="side2")
            perimeter = parallelogram_perimeter(a,b)
            st.write(f"The perimeter of the parallelogram is: {perimeter}")

    elif cal == "Rhombus":
        per =  st.radio("Select the calculation", ("Area", "Perimeter"))
        if per == "Area":
            d1 = st.number_input("Enter the first diagnol of the rhombus")
            d2 = st.number_input("Enter the second diagnol of the rhombus")
            area = rhombus_area(d1, d2)
            st.write(f"The area of the rhombus is: {area}")
        if per == "Perimeter":
            a = st.number_input("Enter side of the rhombus")
            perimeter = rhombus_perimeter(a)
            st.write(f"The perimeter of the rhombus is: {perimeter}")

    elif cal == "Kite":
        per =  st.radio("Select the calculation", ("Area", "Perimeter"))
        if per == "Area":
            d1 = st.number_input("Enter the first diagnol of the kite")
            d2 = st.number_input("Enter the second diagnol of the kite")
            area = kite_area(d1, d2)
            st.write(f"The area of the kite is: {area}")
        if per == "Perimeter":
            a = st.number_input("Enter side of the kite")
            b = st.number_input("Enter side of the kite")
            perimeter = kite_perimeter(a,b)
            st.write(f"The perimeter of the kite is: {perimeter}")

    elif cal == "Trapezium":
        per =  st.radio("Select the calculation", ("Area", "Perimeter"))
        if per == "Area":
            d1 = st.number_input("Enter the first diagnol of the kite")
            d2 = st.number_input("Enter the second diagnol of the kite")
            area = kite_area(d1, d2)
            st.write(f"The area of the kite is: {area}")
        if per == "Perimeter":
            a = st.number_input("Enter side of the kite")
            b = st.number_input("Enter side of the kite")
            perimeter = kite_perimeter(a,b)
            st.write(f"The perimeter of the kite is: {perimeter}")

    else: 
        pass