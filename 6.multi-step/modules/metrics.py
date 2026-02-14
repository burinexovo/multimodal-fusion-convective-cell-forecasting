import tensorflow as tf
from tensorflow.keras import backend as K


def rmse(y_true, y_pred):
    """
    Calculate the Root Mean Squared Error (RMSE) between true and predicted values.

    Args:
        y_true (tf.Tensor): True labels.
        y_pred (tf.Tensor): Predicted labels.

    Returns:
        tf.Tensor: RMSE value.
    """
    return K.sqrt(K.mean(K.square(y_pred - y_true)))