def relu(x):
    if x < 0 :
        return 0
    else:
        return x

for i in range(-10, 11):
    relu_i = relu(i)
    print(f"Relu at value {i}: {relu_i}")