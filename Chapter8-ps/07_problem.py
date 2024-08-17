def mlp_table(n,t=10):
    if(t==0):
        return
    
    mlp_table(n,t-1)
    print(f"{n} x {t} = {n*t}")
    
    
    return

mlp_table(5)