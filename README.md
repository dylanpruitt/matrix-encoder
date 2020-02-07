# matrix-encoder
An attempt to create a matrix encoder in Python.

#### What is matrix encoding?

A matrix encoder uses matrix multiplication to encode and decode messages.

First, we start with a message - for example, "scrumptious pineapple".

Next, we make a list of integers corresponding to characters in the message. 
For the example above, the list is [19, 3, 18, 21, 13, 16, 20, 9, 15, 21, 19, 0, 16, 9, 14, 5, 1, 16, 16, 12, 5].

Then we create an instance of the Encoder class and set the encoder matrix with size ```n```.

Splitting up the list into ```n``` size chunks, using matrix multiplication between the list and the encoder matrix, we obtain the encoded message.
In this case, the encoded message is [160, 120, 184, 198, 212, 240, 170, 171, 203, 116, 234, 154, 159, 157, 191, 122, 56, 140, 111, 166, 140].

Next we create an instance of the Decoder class and set the decoder matrix, with the same size as the encoder matrix.

The decoder matrix is the [inverse matrix](http://mathworld.wolfram.com/MatrixInverse.html) of the encoder matrix. 
Using the same process as encoding, only with the decoder matrix this time, we obtain the original list.

Converting it back to a string, we obtain our original message : "scrumptious pineapple".

[This website provides a good explanation of matrix encoding.](https://www.austincc.edu/lrosen/1314/webact2/webact2.htm)
