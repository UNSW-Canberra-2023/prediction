def predict():
    """Return a simple rain-prediction message."""
    print("bob threshold 0.5")
    print(2 + 2)


def rmse(y, yhat):
    return ((y - yhat) ** 2).mean() ** 0.5
