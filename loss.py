import tensorflow as tf
from tensorflow import math

def cross_entropy_loss(logits: tf.Tensor, labels: tf.Tensor) -> tf.Tensor:

   # import pdb; pdb.set_trace()
    # why is loss 0 sometimes!?


    one_hot_labels = tf.one_hot(labels, logits.shape[3])
    #labels = tf.convert_to_tensor(labels, dtype=tf.float32)
    #import pdb; pdb.set_trace()
    batch_loss = tf.nn.softmax_cross_entropy_with_logits(one_hot_labels, logits)
    loss_value = math.reduce_mean(tf.reduce_sum(batch_loss, 1))
    return loss_value
