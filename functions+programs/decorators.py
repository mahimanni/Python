def wish(fx):
    def mfx(*args,**kwargs):
        print("Good morning")
        fx(*args,**kwargs)
        print("Thankyou")
    return mfx

@wish
def hello():
    print("Hello!")

def add(a,b):
    print("Addition:",a+b)

hello()
wish(add)(1,2)

