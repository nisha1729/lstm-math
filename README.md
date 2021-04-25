# lstm-math

See the accompanying blog post here: http://cpury.github.io/learning-math/

Train a LSTM-based Seq2Seq network to predict the result of math equations on
the character level.
Configuration through global variables because I'm lazy.

Written by Max Schumacher (@cpury) in Summer 2017. Updated in Summer 2019.

## Details

This uses a Seq2Seq model based on LSTMs in Keras. Depending on the complexity
of equations you choose, it will train on some small percentage of the complete
equation space and validate on another small percentage. The model then learns 
to predict the right hand side for new equations as given below

` 67 + 38 =  108   (expected:  105)` \
`15 + 49 =   69   (expected:   64)` \
`84 - 91 =   -5   (expected:   -7)` \
`71 + 53 =  123   (expected:  124)` \
`72 -  1 =   75   (expected:   71)`
