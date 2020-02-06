import os


class Element:
    def __init__(self, row, column, value):
        self.row = row
        self.column = column
        self.value = value


class Matrix:
    def __init__(self, rows, columns):
        self.matrix = []
        self.rows = rows
        self.columns = columns
        self.__create_blank_matrix(rows, columns)

    def __create_blank_matrix(self, rows, columns):
        for i in range(rows):
            for j in range(columns):
                self.matrix.append(Element(i, j, len(self.matrix)))

    def __mul__(self, other):
        return self.multiply_with_matrix(other)

    def __str__(self):
        matrix_string = ""
        for i in range(self.rows):
            for j in range(self.columns):
                matrix_string += str(self.matrix[self.columns*i + j].value)
                matrix_string += " "
            if i < self.rows - 1:
                matrix_string += os.linesep
        return matrix_string

    def multiply_with_matrix(self, other_matrix):
        dimensions = self.get_matrix_product_dimensions(other_matrix)

        if dimensions is not None:
            new_matrix = Matrix(dimensions[0], dimensions[1])
            new_matrix.matrix.clear()

            for i in range(new_matrix.rows):
                for j in range(new_matrix.columns):
                    new_matrix.matrix.append(self.new_element_from_multiplication(other_matrix, i, j))
            return new_matrix
        else:
            return None

    def new_element_from_multiplication(self, other_matrix, row, column):
        new_element = Element(row, column, 0)
        sum = 0

        for i in range(self.columns):
            sum += self.matrix[self.columns*row + i].value * other_matrix.matrix[other_matrix.columns*i + column].value
        new_element.value = sum
        return new_element

    def get_matrix_product_dimensions(self, other_matrix):
        if self.can_be_multiplied_with_matrix(other_matrix):
            return self.rows, other_matrix.columns
        else:
            return None

    def can_be_multiplied_with_matrix(self, other_matrix):
        if self.columns == other_matrix.rows:
            return True
        else:
            return False
