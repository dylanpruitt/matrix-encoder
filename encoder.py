from matrix import Matrix


class Encoder:
    def __init__(self, encoder_matrix):
        self.message_list = []
        self.characters = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
                           "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.encoder_matrix = encoder_matrix
        self.chunk_size = encoder_matrix.rows

    def set_message(self, message):
        self.__convert_message_to_list(message)

    def __convert_message_to_list(self, message):
        for message_character in message:
            for index in range(len(self.characters)):
                if message_character == self.characters[index]:
                    self.message_list.append(index)

    def encode_message(self):
        number_of_chunks = int(len(self.message_list) / self.chunk_size)
        encoded_message = []

        for i in range(number_of_chunks):
            message_chunk = self.message_list[i * self.chunk_size: (i * self.chunk_size) + self.chunk_size]
            matrix = Matrix(3, 1)
            matrix.set_matrix_values(message_chunk)

            encoded_matrix = self.encoder_matrix.__mul__(matrix)

            for element in encoded_matrix.matrix:
                encoded_message.append(element.value)
        if len(self.message_list) % 3 > 0:
            message_chunk = self.message_list[
                            number_of_chunks * self.chunk_size: (number_of_chunks * self.chunk_size) + self.chunk_size]
            for i in range(3 - len(message_chunk)):
                message_chunk.append(-1)
            matrix = Matrix(3, 1)
            matrix.set_matrix_values(message_chunk)

            encoded_matrix = self.encoder_matrix.__mul__(matrix)

            for element in encoded_matrix.matrix:
                encoded_message.append(element.value)

        return encoded_message
