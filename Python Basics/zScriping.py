def test_func():
    print('ge')

test_func()

def another_tf(para1: int, para2: int) -> int: 
    output = para1 + para2
    return output

test = another_tf(1,2)
print(test)

