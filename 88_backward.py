# 곱셈 계층의 구현
class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None

    def forward(self, x, y):
        self.x = x
        self.y = y

        return x * y

    def backward(self, dout):
        dx = dout * self.y
        dy = dout * self.x

        return dx, dy

# 덧셈 계층의 구현
class AddLayer:
    def __init__(self):
        pass

    def forward(self, x, y):
        out = x + y
        return out

    def backward(self, dout):
        dx = dout * 1
        dy = dout * 1
        return dx, dy

mul_apple_layer = MulLayer()
mul_orange_layer = MulLayer()

mul_tax_layer = MulLayer()
add_apple_orange_layer = AddLayer()

apple = 100
apple_num = 2
orange = 150
orange_num = 3
tax = 1.1

# 순전파
apple_price = mul_apple_layer.forward(apple, apple_num)
orange_price = mul_orange_layer.forward(orange, orange_num)
all_price = add_apple_orange_layer.forward(apple_price, orange_price)
price = mul_tax_layer.forward(all_price, tax)

# 역전파
dprice = 1
dall_price, dtax = mul_tax_layer.backward(dprice)
dapple_price, dorange_price = add_apple_orange_layer.backward(dall_price)
dapple, dapple_num = mul_apple_layer.backward(dorange_price)
dorange, dorange_num = mul_orange_layer.backward(dorange_price)

print("Total price: ", price)
print(
    "\ndapple_num = ", dapple_num,
    "\ndapple = ", dapple,
    "\ndorange_num = ", dorange_num,
    "\ndorange = ", dorange,
    "\ndtax = ", dtax
)
