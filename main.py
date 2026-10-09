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
            a = st.number_input("Enter side of the kite", key="kite_side_a")
            b = st.number_input("Enter another side of the kite", key="kite_side_b")
            perimeter = kite_perimeter(a,b)
            st.write(f"The perimeter of the kite is: {perimeter}")

    elif cal == "Trapezium":
        per =  st.radio("Select the calculation", ("Area", "Perimeter"))
        if per == "Area":
            a = st.number_input("Enter the first parallel side", key="trap_a")
            b = st.number_input("Enter the second parallel side", key="trap_b")
            h = st.number_input("Enter the height", key="trap_h")
            area = trapezium_area(a, b, h)
            st.write(f"The area of the trapezium is: {area}")
        if per == "Perimeter":
            a = st.number_input("Enter first side", key="trap_side_a")
            b = st.number_input("Enter second side", key="trap_side_b")
            c = st.number_input("Enter third side", key="trap_side_c")
            d = st.number_input("Enter fourth side", key="trap_side_d")
            perimeter = trapezium_perimeter(a, b, c, d)
            st.write(f"The perimeter of the trapezium is: {perimeter}")
    
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
        elif cir == "Quater Circle":
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

if shapes == "3D Shape":
    cal = st.radio("Select the figure", ("Cube", "Cuboid", "Cylinder","Sphere","Cone", "Prism", "Ellipsoid", "Octahedron","Pyramid"))

    if cal == "Cube":
        per =  st.radio("Select the calculation", ("Volume", "Total Surface Area"))
        if per == "Volume":
            a = st.number_input("Enter a side of the cube")
            volume = cube_volume(a)
            st.write(f"The volume of the cube is: {volume}")
        elif per == "Total Surface Area":
            a = st.number_input("Enter a side of the cube")
            tsa = cube_tsa(a)
            st.write(f"The total surface area of the cube  is: {tsa}")

    elif cal == "Cuboid":
        per =  st.radio("Select the calculation", ("Volume", "Total Surface Area"))
        if per == "Volume":
            a = st.number_input("Enter a side of the cube")
            volume = cube_volume(a)
            st.write(f"The volume of the cube is: {volume}")
        elif per == "Total Surface Area":
            a = st.number_input("Enter a side of the cube")
            tsa = cube_tsa(a)
            st.write(f"The total surface area of the cube  is: {tsa}")

    elif cal == "Cylinder":
        cy = st.radio("Select the Cylinder", ("Normal Cylinder", "Hollow Cylinder"))
        if cy == "Normal Cylinder":
            per =  st.radio("Select the calculation", ("Volume", "Total Surface Area"))
            if per == "Volume":
                r = st.number_input("Enter the radius of the cylinder")
                h = st.number_input("Enter the height of the cylinder")
                volume = cylinder_volume(r,h)
                st.write(f"The volume of the cylinder is: {volume}")
            elif per == "Total Surface Area":
                r = st.number_input("Enter the radius of the cylinder")
                h = st.number_input("Enter the height of the cylinder")
                tsa = cylinder_tsa(r,h)
                st.write(f"The total surface area of the cylinder is: {tsa}")
        elif cy == "Hollow Cylinder":
            per =  st.radio("Select the calculation", ("Volume", "Total Surface Area"))
            if per == "Volume":
                R = st.number_input("Enter the outer radius of the cylinder")
                r = st.number_input("Enter the inner radius of the cylinder")
                h = st.number_input("Enter the height of the cylinder")
                volume = hollow_cylinder_volume(R,r,h)
                st.write(f"The volume of the hollow cylinder is: {volume}")
            elif per == "Total Surface Area":
                R = st.number_input("Enter the outer radius of the cylinder")
                r = st.number_input("Enter the inner radius of the cylinder")
                h = st.number_input("Enter the height of the cylinder")
                tsa = hollow_cylinder_tsa(R,r,h)
                st.write(f"The total surface area of the hollow cylinder is: {tsa}")

    elif cal == "Sphere":
        sp = st.radio("Select the Sphere", ("Sphere", "Hemisphere"))
        if sp == "Sphere":
            per =  st.radio("Select the calculation", ("Volume", "Total Surface Area"))
            if per == "Volume":
                r = st.number_input("Enter the radius of the sphere")
                volume = sphere_volume(r)
                st.write(f"The volume of the sphere is: {volume}")
            elif per == "Total Surface Area":
                r = st.number_input("Enter the radius of the sphere")
                tsa = sphere_tsa(r)
                st.write(f"The total surface area of the sphere is: {tsa}")
        elif sp == "Hemisphere":
            per =  st.radio("Select the calculation", ("Volume", "Total Surface Area"))
            if per == "Volume":
                r = st.number_input("Enter the radius of the hemisphere")
                volume = hemisphere_volume(r)
                st.write(f"The volume of the hemisphere is: {volume}")
            elif per == "Total Surface Area":
                r = st.number_input("Enter the radius of the hemisphere")
                tsa = hemisphere_tsa(r)
                st.write(f"The total surface area of the hemisphere is: {tsa}")

    elif cal == "Cone":
        cn = st.radio("Select the Sphere", ("Cone", "Frustum of Cone"))
        if cn == "Cone":
            per =  st.radio("Select the calculation", ("Volume", "Total Surface Area"))
            if per == "Volume":
                r = st.number_input("Enter the radius of the cone")
                h = st.number_input("Enter the height of the cone")
                volume = cone_volume(r)
                st.write(f"The volume of the cone is: {volume}")
            elif per == "Total Surface Area":
                r = st.number_input("Enter the radius of the cone")
                h = st.number_input("Enter the slant height of the cone")
                tsa = cone_tsa(r)
                st.write(f"The total surface area of the cone is: {tsa}")
        elif cn == "Frustum of Cone":
            per =  st.radio("Select the calculation", ("Volume", "Total Surface Area"))
            if per == "Volume":
                R = st.number_input("Enter the outer radius of the frustum of cone")
                r = st.number_input("Enter the inner radius of the frustum of cone")
                h = st.number_input("Enter the height of the frustum of cone")
                volume = frustum_of_cone_volume(R,r,h)
                st.write(f"The volume of the frustum of cone is: {volume}")
            elif per == "Total Surface Area":
                R = st.number_input("Enter the outer radius of the frustum of cone")
                r = st.number_input("Enter the inner radius of the frustum of cone")
                s = st.number_input("Enter the slant height of the frustum of cone")
                tsa = frustum_of_cone_tsa(R,r,s)
                st.write(f"The total surface area of the frustum of cone is: {tsa}")
    
    elif cal == "Prism":
        pr = st.radio("Select the Prism", ("Prism", "Triangular Prism"))
        if pr == "Prism":
            per =  st.radio("Select the calculation", ("Volume", "Total Surface Area"))
            if per == "Volume":
                base_area = st.number_input("Enter the base area of the prism")
                h = st.number_input("Enter the height of the prism")
                volume = prism_volume(base_area, h)
                st.write(f"The volume of the prism is: {volume}")
            elif per == "Total Surface Area":
                B = st.number_input("Enter the base area of the  prism")
                P = st.number_input("Enter the base perimeter of the prism")
                h = st.number_input("Enter the height of the prism")
                tsa = prism_tsa(B, P, h)
                st.write(f"The total surface area of the prism is: {tsa}")
        elif pr == "Triangular Prism":
            per =  st.radio("Select the calculation", ("Volume", "Total Surface Area"))
            if per == "Volume":
                b = st.number_input("Enter the base of the triangular face of the triangular prism")
                l = st.number_input("Enter the  length of the prism")
                h = st.number_input("Enter the height of the triangular face of the triangular prism")
                volume = triangular_prism_volume(b,h,l)
                st.write(f"The volume of the triangular face is: {volume}")    
            elif per == "Total Surface Area":
                triangular_area = st.number_input("Enter the triangular area of the triangular face of the triangular prism", key="triangular_prism_area")
                l = st.number_input("Enter the length of the triangular prism", key="triangular_prism_length")
                a = st.number_input("Enter the first side of the triangular face of the triangular prism", key="triangular_prism_first_side")
                b = st.number_input("Enter the second side of the triangular face of the triangular prism", key="triangular_prism_second_side")
                c = st.number_input("Enter the third side of the triangular face of the triangular prism", key="triangular_prism_third_side")
                tsa = triangular_prism_tsa(triangular_area, l, a, b, c)
                st.write(f"The total surface area of the triangular prism is: {tsa}")

    elif cal == "Ellipsoid":
        per =  st.radio("Select the calculation", ("Volume"))
        if per == "Volume":
            a = st.number_input("Enter Semi-axis length along x-axis")
            b = st.number_input("Enter Semi-axis length along y-axis")
            c = st.number_input("Enter Semi-axis length along z-axis")
            volume = ellipsoid_volume(a, b, c)
            st.write(f"The volume of the ellipsoid is: {volume}")

    elif cal == "Octahedron":
        per =  st.radio("Select the calculation", ("Total Surface Area"))
        if per == "Total Surface Area":
            a = st.number_input("Enter Edge length of the octahedron")
            b = st.number_input("Enter Semi-axis length along y-axis")
            c = st.number_input("Enter Semi-axis length along z-axis")
            tsa = octahedron_tsa(a)
            st.write(f"The total surface area of the octahedron is: {tsa}")

    elif cal == "Pyramid":
        cir = st.radio("Select the pyramid", ("Pyramid", "Square Pyramid" ,"Rectangular Pyramid", "Frustum of Pyramid", "Tetrahedron"))
        if cir == "Pyramid":
            per =  st.radio("Select the calculation", ("Volume", "Total Surface Area"))
            if per == "Volume":
                base_area = st.number_input("Enter the base area of the pyramid")
                h = st.number_input("Enter the height of the pyramid")
                volume = pyramid_volume(base_area,h)
                st.write(f"The area of the pyramid is: {volume}")
            elif per == "Total Surface Area":
                B = st.number_input("Enter the base area of the pyramid of the square pyramid")
                P = st.number_input("Enter the base perimeter of the pyramid")
                s = st.number_input("Enter the side of the pyramid")                
                tsa = pyramid_tsa(B,P,s)
                st.write(f"The total surface area of the pyramid is: {tsa}")
        elif cir == "Square Pyramid":
            per =  st.radio("Select the calculation", ("Volume", "Total Surface Area"))
            if per == "Volume":
                a = st.number_input("Enter the length of the base side of the square pyramid")                
                h = st.number_input("Enter the height of the square pyramid")
                volume = square_pyramid_volume(a,h)
                st.write(f"The volume of the square pyramid is: {volume}")
            elif per == "Total Surface Area":
                a = st.number_input("Enter the base side of the square pyramid")
                s = st.number_input("Enter the slant height of the square pyramid")
                tsa = square_pyramid_tsa(a,s)
                st.write(f"The total surface area of the square pyramid is: {tsa}")
        elif cir == "Rectangular Pyramid":
            per =  st.radio("Select the calculation", ("Volume", "Total Surface Area"))
            if per == "Volume":
                l = st.number_input("Enter the base length of the reactangular pyramid")                
                w = st.number_input("Enter the base width of the rectangular pyramid")
                h = st.number_input("Enter the height of the rectangular pyramid")
                volume = rectangular_pyramid_volume(l,w,h)
                st.write(f"The volume of the rectangular pyramid is: {volume}")
            elif per == "Total Surface Area":
                l = st.number_input("Enter the base length of the reactangular pyramid")                
                w = st.number_input("Enter the base width of the rectangular pyramid")
                s1 = st.number_input("Enter the slant height along the length side of the square pyramid")
                s2 = st.number_input("Enter the slant height along the width side of the square pyramid")
                tsa = rectangular_pyramid_tsa(l,w,s1,s2)
                st.write(f"The total surface area of the rectangular pyramid is: {tsa}")
        elif cir == "Frustum of Pyramid":
            per =  st.radio("Select the calculation", ("Volume"))
            if per == "Volume":
                A1 = st.number_input("Enter the area of lower base of the frustum of pyramid")
                A2 = st.number_input("Enter the area of upper base of the frustum of pyramid")
                h = st.number_input("Enter the height of the frustum of pyramid")
                theta=st.number_input("Enter the value of theta of the circular sector")
                volume = frustum_of_pyramid_volume(A1, A2, h)
                st.write(f"The volume of the frustum of pyramid: {volume}")    
        elif cir == "Tetrahedron":
            per =  st.radio("Select the calculation", ("Total Surface Area"))
            if per == "Total Surface Area":
                a = st.number_input("Enter the edge of the tetrahedron")
                tsa = tetrahedron_tsa(a)
                st.write(f"The total surface area of the tetrahedron is: {tsa}")    