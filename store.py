def store_func(data, store) -> bool:
    return store and data, store


var1 = str(store_func(True, True))
var2 = str(store_func(True, False))
var3 = str(store_func(False, False))
var4 = str(store_func(False, True))


def space(x, y) -> str:
    if x == 1:
        return " "*(17-len(y))
    elif x == 2:
        return " "*(17-len(y))


out1 = "True, True"
out2 = "True, False"
out3 = "False, False"
out4 = "False, True"
print("     Output      |  Function Input   |  Expected")
print("-----------------|-------------------|----------------")
print(var1+space(1, var1)+f"|  {out1}"+space(2, out1)+"|  True, True")
print(var2+space(1, var2)+f"|  {out2}"+space(2, out2)+"|  False, False")
print(var3+space(1, var3)+f"|  {out3}"+space(2, out3)+"|  False, False")
print(var4+space(1, var4)+f"|  {out4}"+space(2, out4)+"|  False, True")
