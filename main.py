import vect_calc as vc


if __name__ == "__main__":
    # Example usage of the vector calculator functions
    vector1 = [1, 2, 3]
    vector2 = [4, 5, 6]

    print("Vector 1:", vector1)
    print("Vector 2:", vector2)

    # Addition
    result_add = vc.Calculator.add(vector1, vector2)
    print("Addition Result:", result_add)

    # Subtraction
    result_sub = vc.Calculator.subtract(vector1, vector2)
    print("Subtraction Result:", result_sub)

    # Dot Product
    result_dot = vc.Calculator.multiply(vector1, vector2)
    print("Dot Product Result:", result_dot)