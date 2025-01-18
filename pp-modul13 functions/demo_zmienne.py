#zmienna lokalna vs zmienna globalna
 def scope_test():
     x = 123
     print(x)

 scope_test()
 print(x) #nie dziala bo nie ma x globalnie, x pojawia sie tylko w funkcji i jest widoczne przez chwile tylko

 #####################

 def scope_test2():


 x = 123

 scope_test2()