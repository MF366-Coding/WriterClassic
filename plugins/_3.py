def plugin(a, b, c, *args, **kargs):
    for i in args:
        print("...")
    
    h = args
    j = kargs
    
    try:
        print(kargs)
    except:
        print(id(b))
    finally:
        print(type(a))
    
    g = c
    
    print(g is c)
    
title = "Example I - v2.0"