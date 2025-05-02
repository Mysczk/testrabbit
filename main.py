import vect_calc as vc


if __name__ == "__main__":
    # Example usage of the vector calculator functions
    vector1 = [1, 2, 3]
    vector2 = [4, 5, 6]

    print("Vector 1:", vector1)
    print("Vector 2:", vector2)

    # Addition
    result_add = vc.add_vectors(vector1, vector2)
    print("Addition Result:", result_add)

    # Subtraction
    result_sub = vc.subtract_vectors(vector1, vector2)
    print("Subtraction Result:", result_sub)

    # Dot Product
    result_dot = vc.dot_product(vector1, vector2)
    print("Dot Product Result:", result_dot)

    # Cross Product
    result_cross = vc.cross_product(vector1, vector2)
    print("Cross Product Result:", result_cross)

    # Magnitude
    result_magnitude = vc.magnitude(vector1)
    print("Magnitude of Vector 1:", result_magnitude)

    # Angle between vectors
    angle = vc.angle_between_vectors(vector1, vector2)
    print("Angle between Vectors (in degrees):", angle)