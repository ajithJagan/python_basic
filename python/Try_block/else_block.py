
try :
    a =10 /0
    print(a)
except Exception as e:
    print(e)
else:
    print("No error")
finally:
    print("Finally block")
    
    
try :
    print(b)
except Exception as e:
    print(e)
else:
    print("No error")
finally:
    print("Finally block")

