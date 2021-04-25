# lstm-math

See the accompanying blog post here: http://cpury.github.io/learning-math/

Train a LSTM-based Seq2Seq network to predict the result of math equations on
the character level.
Configuration through global variables because I'm lazy.

Written by Max Schumacher (@cpury) in Summer 2017. Updated in Summer 2019.

## Details

This uses a Seq2Seq model based on LSTMs in Keras. Depending on the complexity
of equations you choose, it will train on some small percentage of the complete
equation space and validate on another small percentage. So all the equations you
see in the example above have not been seen by the network before.
