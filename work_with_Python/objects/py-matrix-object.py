"""
This scripts demonstrates th work with matrix presented as Python object
We will use this object in the intro-to-pytest chapter
"""
class Matrix:
    def __init__(self, data: list[list[int]]):
        """
        Initialize the Matrix with a list of lists.
        """
        self.data = data

    def is_empty(self) -> bool:
        """
        Returns True if the matrix is empty, otherwise False.
        """
        return not self.data or not self.data[0]

    def dimensions(self) -> tuple:
        """
        Returns a tuple (rows, columns) representing the dimensions of the matrix.
        If the matrix is empty, returns (0, 0).
        """
        if self.is_empty():
            return (0, 0)
        
        return (len(self.data), len(self.data[0]))

    def swap_diagonal(self) -> None:
        """
        Swap the elements on the main diagonal with those on the
        secondary (anti-)diagonal.
        """
        n = len(self.data)
        for i in range(n):
            # use tuple unpacking for a pythonic swap
            self.data[i][i], self.data[i][n-i-1] = self.data[i][n-i-1], self.data[i][i]

    def transpose(self) -> None:
        """
        Transpose the matrix in-place.
        """
        x = len(self.data)
        y = len(self.data[0])
        for i in range(x):
            for j in range(i, y):
                # sap elements to transpose the matrix
                self.data[i][j], self.data[j][i] = self.data[j][i], self.data[i][j]
                
    def __str__(self) -> str:
        """
        Return a formatted string representation of the matrix.
        """
        if self.is_empty():
            return "[[]]"
            
        rows, cols = self.dimensions()
        result = f"Dimensions: {rows} x {cols}\n-----------\n"
        for row in self.data:
            result += " ".join(str(item) for item in row) + "\n"
        
        return result


# usage example
if __name__ == '__main__':
    print("Matrix as the Python Object")
    # create the matrix
    mx1 = Matrix([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 0, 2, 3],
        [4, 5, 6, 7]
    ])
    print("The initial matrix is:")
    print(mx1)
    
    # transpose the matrix and print the result
    mx1.transpose()
    print("After transposing:")
    print(mx1)
    
    # create a 3x3 matrix
    mx2 = Matrix([
        [3, 1, 2],
        [1, 0, 1],
        [2, 1, 3]
    ])
    print("The initial matrix is:")
    print(mx2)
    
    # swap the diagonals
    mx2.swap_diagonal()
    print("After diagonal swap:")
    print(mx2)
    