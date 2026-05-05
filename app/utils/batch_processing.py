def batch_process(data, func):
    return [func(item) for item in data]