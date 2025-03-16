"""
Pascal's triangle for number 10:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
1 7 21 35 35 21 7 1
1 8 28 56 70 56 28 8 1
1 9 36 84 126 126 84 36 9 1

Observe three ways to generate the Pascal triangle.
The first way that uses the recursion is possible but not recommended.
"""


def pascal_triangle(n: int) -> list[list]:
    """
    Generate Pascal's Triangle with n rows with recursive call.

    :param n: Number of rows in the triangle.
    :return: A list of lists representing Pascal's Triangle.
    """
    result = []
    pt_run(n, result)

    return result


def pt_run(n: int, results: list) -> list[list]:
    """
    Pascal's Triangle recursive function.

    :param n: Number of rows in the triangle.
    :param results: A list of lists representing Pascal's triangle.
    :return: A final list of lists representing the triangle.
    """

    # the first line
    if n == 1:
        results.append([1])
    else:
        prev_lst = pt_run(n - 1, results)

        # comprehend the current list 
        curr_lst = [prev_lst[i] + prev_lst[i + 1] for i in range(len(prev_lst) - 1)]
        results.append([1] + curr_lst + [1])

    return results[n - 1]


def pt_with_generator(n: int):
    """
    Generate Pascal's Triangle lazily as a generator.
    
    :param n: Number of rows to generate.
    :yield: Next row of Pascal's Triangle as a list of integers.
    """
    row = [1]
    for _ in range(n):
        yield row
        # compute the next row using list comprehension.
        # the next row is 1, then each pair-sum from current row, then 1.
        row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]


def pt_generate(n: int) -> list[list[int]]:
    """
    Generate Pascal's Triangle with n rows.
    
    :param n: Number of rows in the triangle.
    :return: A list of lists representing Pascal's Triangle.
    """
    triangle = []
    for i in range(n):
        # Create a new row with 1's, length equals to i+1.
        row = [1] * (i + 1)
        # Each element (except the first and last) is the sum of the two elements above it.
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle


def main():
    print("Generate Pascal's triangle for number 10")

    print("Using Recursion:")
    for line in pascal_triangle(10):
        print(line)

    p_triangle = pt_generate(10)
    print("\nUsing Simple Loop:")
    for row in p_triangle:
        # join the numbers in the row as a string.
        print(" ".join(str(num) for num in row))

    print("\nUsing Generator:")
    for row in pt_with_generator(10):
        print(" ".join(str(num) for num in row))


if __name__ == "__main__":
    main()
