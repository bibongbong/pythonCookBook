def noyield(n):
    l1 = []
    print("noyied %d"%n)
    for x in range(n):
        l1.append(x*x)
    print("noyied %d complete" % n)
    return l1

def yield_test(n):
    print("yield_test(%d) start" % n)
    for x in range(n):
        print("     yield_test(): get %d from __main__" % x)
        yield x*x

    print("yield_test(%d) complete" % n)


y = 0
for x in yield_test(5):
    y+=1
    print("The %d st loop: get %d from yield_test" %(y,x)),


#for y in noyield(5):
#    print("for %d in noyield(5)" %y),



