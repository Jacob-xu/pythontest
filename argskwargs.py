#arg
def test_args(first, *args):
    print(first)
    for v in args:
        print("args %s" %v)

test_args(1, 2, 3, 4, 5)

#kwargs
def test_kwargs(first, *args, **kwargs):
    print(first)
    for v in args:
        print("args %s" %v)
    for k,v in kwargs.items():
        print("kwargs",(k, v))

test_kwargs(1, 2, 3, 4, 5, k0=4, k1=5, k2=6)