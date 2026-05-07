from multipledispatch import dispatch
class overloading:
    @dispatch(float)
    def area(r):
        res=3.14*r*r
        print(f"Area of circle={res:3f}")
    @dispatch(int)
    def area(s):
        res=s*s
        print(f"Area of square={res}")
    @dispatch(float,float)
    def area(l,b):
        res=l*b
        print(f"Area of rectangle={res}")
obj=overloading()
obj.area(7.9)
obj.area(4)
obj.area(12.5,23.6)