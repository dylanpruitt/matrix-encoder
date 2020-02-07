from matrix import Matrix
from encoder import Encoder

encoder_matrix = Matrix(3,3)
encoder_matrix.set_matrix_values([1, 5, 7,
                                  3, 9, 2,
                                  1, 7, 8])

encoder = Encoder(encoder_matrix)
encoder.set_message("scrumptious pineapple")
print(encoder.message_list)
encoded_message = encoder.encode_message()
print(encoded_message)