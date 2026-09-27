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

    elif cal == "Circle":
        cir = st.radio("Select the circle", ("Circle", "Semicircle" ,"Quater Circle", "Circular Sector", "Circular Segment" ,"Annulus", "Ellipse"))
        if cir == "Circle":
            per =  st.radio("Select the calculation", ("Area", "Circumference"))
            if per == "Area":
                r = st.number_input("Enter the radius of the circle")
                area = circle_area(r)
                st.write(f"The area of the circle is: {area}")
            elif per == "Circumference":
                r = st.number_input("Enter the radius of the circle")
                circumference = circle_circumference(r)
                st.write(f"The cirumference of the circle is: {circumference}")
        elif cir == "Semicircle":
            per =  st.radio("Select the calculation", ("Area", "Perimeter"))
            if per == "Area":
                r = st.number_input("Enter the radius of the semicircle")
                area = semicircle_area(r)
                st.write(f"The area of the semicircle is: {area}")
            elif per == "Perimeter":
                r = st.number_input("Enter the radius of the semicircle")
                perimeter = semicircle_primeter(r)
                st.write(f"The perimeter of the semicircle is: {perimeter}")
        elif cir == "Quate Circle":
            per =  st.radio("Select the calculation", ("Area", "Perimeter"))
            if per == "Area":
                r = st.number_input("Enter the radius of the quater circle")
                area = quartercircle_area(r)
                st.write(f"The area of the quater circle is: {area}")
            elif per == "Perimeter":
                r = st.number_input("Enter the radius of the quater circle")
                perimeter = quatercircle_perimeter(r)
                st.write(f"The perimeter of the quater circle is: {perimeter}")
        elif cir == "Circular Sector":
            per =  st.radio("Select the calculation", ("Arc Length", "Area"))
            if per == "Area":
                r = st.number_input("Enter the radius of the circular sector")
                theta=st.number_input("Enter the value of theta of the circular sector")
                area = circular_sector_area(theta,r)
                st.write(f"The area of the circular sector is: {area}")
            elif per == "Arc Length":
                r = st.number_input("Enter the radius of the circular sector")
                theta=st.number_input("Enter the value of theta of the circular sector")
                arc_length = circular_sector_arc(theta, r)
                st.write(f"The arc length of the circular sector is: {arc_length}")   
        elif cir == "Circular Segment":
            per =  st.radio("Select the calculation", ("Area"))
            if per == "Area":
                sector = st.number_input("Enter the value of sector of  circular segment")
                triangle =st.number_input("Enter the value of triangle of  circular sector")
                area = circular_segment_area(sector, triangle)
                st.write(f"The area of the circular segment is: {area}")    
        elif cir == "Annulus":
            per =  st.radio("Select the calculation", ("Outer Circumference", "Inner Circumference", "Area"))
            if per == "Area":
                R = st.number_input("Enter the radius of the outer circle of annulus")
                r = st.number_input("Enter the radius of the inner circle of the annulus")
                area = annulus_area(R,r)
                st.write(f"The area of the annulus is: {area}")
            if per == "Outer Circumference":
                R = st.number_input("Enter the radius of the outer circle of annulus")
                o_circumference = outer_circumference(R)
                st.write(f"The outer circumference of the annulus is: {o_circumference}")
            if per == "Inner Circumference":
                r = st.number_input("Enter the radius of the inner circle of the annulus")
                i_circumference = inner_circumference(r)
                st.write(f"The inner circumference of the annulus is: {i_circumference}")
        elif cir == "Ellipse":
            per =  st.radio("Select the calculation", ("Area"))
            if per == "Area":
                a = st.number_input("Enter the value of semi major axis of ellipse")
                b =st.number_input("Enter the value of semi minor axis of ellipse")
                area = ellipse_area(a,b)
                st.write(f"The area of the ellipse is: {area}")
    elif cal == "Polygon":
        per =  st.radio("Select the calculation", ("Area", "Perimeter"))
        if per == "Area":
            apothem = st.number_input("Enter the value of apothem of polygon")
            perimeter = st.number_input("Enter the valus of perimeter of polygon")
            area = polygon_area(apothem, perimeter)
            st.write(f"The area of the polygon is: {area}")
        if per == "Perimeter":
            n = st.number_input("Enter the number of sides  of the polygon")
            a = st.number_input("Enter the length of one side of the polygon")
            perimeter = polygon_perimeter(n,a)
            st.write(f"The perimeter of the polygon is: {perimeter}")
    elif cal == "Hexagon":
        per =  st.radio("Select the calculation", ("Area", "Perimeter"))
        if per == "Area":
            a = st.number_input("Enter the length of one side of the hexagon")
            area = hexagon_area(a)
            st.write(f"The area of the hexagon is: {area}")
        if per == "Perimeter":
            a = st.number_input("Enter the length of one side of the hexagon")
            perimeter = heaxagon_perimeter(a)
            st.write(f"The perimeter of the hexagon is: {perimeter}")
    elif cal == "Pentagon":
        per =  st.radio("Select the calculation", ("Area", "Perimeter"))
        if per == "Area":
            a = st.number_input("Enter the length of one side of the pentagon")
            area = pentagon_area(a)
            st.write(f"The area of the pentagon is: {area}")
        if per == "Perimeter":
            a = st.number_input("Enter the length of one side of the pentagon")
            perimeter = pentagon_perimeter(a)
            st.write(f"The perimeter of the pentagon is: {perimeter}")
    elif cal == "Octagon":
        per =  st.radio("Select the calculation", ("Area", "Perimeter"))
        if per == "Area":
            a = st.number_input("Enter the length of one side of the octagon")
            area = octagon_area(a)
            st.write(f"The area of the octagon is: {area}")
        if per == "Perimeter":
            a = st.number_input("Enter the length of one side of the octagon")
            perimeter = octagon_perimeter(a)
            st.write(f"The perimeter of the octagon is: {perimeter}")    
    else: 
        pass