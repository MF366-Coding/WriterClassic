def plugin(a, b, c, *args):
    try:
        for i in args:
            print(id(a))
            print(type(a))
    except:
        print(id(b))
        print(type(b))
    else:
        print("An error was not raised.")
    finally:
        print(id(c))
        print(type(c))

class a:
    title = "Example II"

title = a.title