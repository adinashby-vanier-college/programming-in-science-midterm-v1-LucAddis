import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    result = (math.pi * radius ** 2)
    
    return round(result, 2)

# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    result = ""
    number_of_spaces = 0
    
    for i in range(1, n + 1):
        
        if n <= 3:
            result = "The triangle height should be at least 4."

        else:
            
            if i == 1:
                result += ("*" + "\n")
            
            elif i == n:
                result += ("*" * n)
            
            else:
                result += ("*" + " " * number_of_spaces + "*" + "\n")
                
                number_of_spaces += 1
    
    return result

# Q3: Inverted Pyramid
def inverted_pyramid(n):
    result = ""
    number_of_spaces = 0
    number_of_stars = ((2 * n) - 1)

    if n <= 2:
        result = "The pyramid height should be at least 3."
   
    else:
        
        for i in range(1, n + 1):
            result += (" " * number_of_spaces + "*" * number_of_stars + "\n")
            
            number_of_spaces += 1
            
            number_of_stars -= 2
    
    return result.rstrip()

# ----------------------------------------------------------------
print(area_of_circle(5))
print()

print(hollow_right_triangle(3))
print()

print(hollow_right_triangle(4))
print()

print(hollow_right_triangle(5))
print()

print(inverted_pyramid(3))
print()

print(inverted_pyramid(4))
print()

print(inverted_pyramid(5))
print()