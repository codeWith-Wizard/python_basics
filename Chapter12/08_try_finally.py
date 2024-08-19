def new_func():
    try :
        a = int(input("enetr a no. : "))
        print(a)
        return
    except Exception as e:
        print(e)
        return
    finally: 
        print("code successfully executed !!")  #finally runs even after return and in bot try and except

new_func()