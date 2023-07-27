# ================================================================================================
# ====        ///// Python code to demonstrate the use of docstring in RST format \\\\        ====
# ================================================================================================

"""
Date : 27/07/2023

Designed by : 
    - Damien Mascheix @Hagzilla https://www.linkedin.com/in/damien-mascheix/

Notes :
    The function used for the demo is a cylinder volume compute.

"""

import math

def cylinder_volume(radius_m, height_m):
    """
    Compute the volume of a cylinder.

    :param radius_m: The radius of the cylinder's base in meters.
    :type radius_m: float
    :param height_m: The height of the cylinder in meters.
    :type height_m: float
    :return: The volume of the cylinder in cubic meters (m³).
    :rtype: float
    """
    if radius_m <= 0 or height_m <= 0:
        raise ValueError("Both radius and height must be positive numbers for volume computation.")

    volume_m3 = math.pi * radius_m ** 2 * height_m
    
    return volume_m3



if __name__ == "__main__":

    # User input
    print(" === Welcome to the cylinder volume compute === ")
    radius_m = int(input("Enter the radius of the cylinder in meter : "))
    height_m = int(input("Enter the heigth of the cylinder in meter : "))

    # Print the result
    try:
        print(f"The volume of a cylinder r= {radius_m} m & h= {height_m} m is {cylinder_volume(radius_m, height_m)} m3")
    except ValueError as e:
        print(e)

    # Print the function documentation just for the demo
    print(cylinder_volume.__doc__)






