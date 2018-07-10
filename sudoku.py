# pylint: disable=missing-docstring

class SudokuSolver:
    def __init__(self, grid):
        self.grid = grid
        self.transpose_grid = list(zip(*self.grid))
        self.grid_squares = self.__grid_square()

    def is_valid(self):
        #import pdb; pdb.set_trace()
        valid = True

        print(self.grid)
        print('-'*20)
        print(self.transpose_grid)
        print('-'*20)
        print(self.grid_squares)

        if not self.is_grid_valid(self.grid):
            valid = False
        elif not self.is_grid_valid(self.transpose_grid):
            valid = False
        elif not self.is_grid_valid(self.grid_squares):
            valid = False

        return valid

    def is_grid_valid(self, aGrid):
        valid = True

        for item in aGrid:
            for value in range(10):
                if value not in item:
                    valid = False
                    break

        return valid


    def __grid_square(self):
        squares = []

        for offset in range(0, 9, 3):
            aSquares1 = []
            aSquares2 = []
            aSquares3 = []

            for index in range(3):
                aSquares1.append(list(self.grid[offset + index][:3]))
                aSquares2.append(list(self.grid[offset + index][3:6]))
                aSquares3.append(list(self.grid[offset + index][6:]))

            squares.append(sum(aSquares1, []))
            squares.append(sum(aSquares2, []))
            squares.append(sum(aSquares3, []))

        return squares

