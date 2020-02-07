from matrix import Matrix
from encoder import Encoder
from decoder import Decoder

encoder_matrix = Matrix(3,3)
encoder_matrix.set_matrix_values([1, 5, 7,
                                  3, 9, 2,
                                  1, 7, 8])

decoder_matrix = Matrix(3,3)
decoder_matrix.set_matrix_values([29/16, 9/32, -53/32,
                                  -11/16, 1/32, 19/32,
                                  3/8, -1/16, -3/16])

encoder = Encoder(encoder_matrix)
encoder.set_message("gnome country")
print("Message in integer format: " + str(encoder.message_list))
encoded_message = encoder.encode_message()
print("Encoded message: " + str(encoded_message))

decoder = Decoder(decoder_matrix)
decoder.set_message(encoded_message)
decoded_message = decoder.decode_message()
print("Decoded message: " + decoded_message)