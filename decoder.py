from matrix import Matrix
from math import ceil


class Decoder:
    def __init__(self, decoder_matrix):
        self.message_list = []
        self.characters = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
                           "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.decoder_matrix = decoder_matrix
        self.chunk_size = decoder_matrix.rows

    def set_message(self, message):
        self.message_list = message

    def __convert_list_to_message(self, message_list):
        message = ""
        for element in message_list:
            if element != -1:
                message += self.characters[element]
        return message

    def decode_message(self):
        number_of_chunks = int(len(self.message_list) / self.chunk_size)
        decoded_message_list = []

        for i in range(number_of_chunks):
            message_chunk = self.message_list[i * self.chunk_size: (i * self.chunk_size) + self.chunk_size]
            matrix = Matrix(3, 1)
            matrix.set_matrix_values(message_chunk)

            decoded_matrix = self.decoder_matrix.__mul__(matrix)

            for element in decoded_matrix.matrix:
                decoded_message_list.append(int(element.value))
        if len(self.message_list) % 3 > 0:
            message_chunk = self.message_list[
                            number_of_chunks * self.chunk_size: (number_of_chunks * self.chunk_size) + self.chunk_size]
            matrix = Matrix(3, 1)
            matrix.set_matrix_values(message_chunk)

            decoded_matrix = self.decoder_matrix.__mul__(matrix)

            for element in decoded_matrix.matrix:
                decoded_message_list.append(int(element.value))

        decoded_message = self.__convert_list_to_message(decoded_message_list)
        return decoded_message
