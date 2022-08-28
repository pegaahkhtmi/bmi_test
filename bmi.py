name=input("please insert your name")
weight=float(input("dear"+name+"please insert your weight"))
height=float(input("dear"+name+"please insert your height(as m)"))
bmi=float(weight/(height**2))

if bmi<18.5:
    print("your bmi is:"+str(format(bmi,".2f"))+"you should encrease your weight")
elif bmi>18.5 and bmi<=24.9:
        print("your bmi is:"+str(format(bmi,".2f"))+"your body is in the best situation")
elif bmi>24.9 and bmi<=29.9:
            print("your bmi is:"+str(format(bmi,".2f"))+"you have owerweight it is better for you to decrease your weight")
elif bmi>29.9 and bmi <=39.9:
                print("your bmi is:"+str(format(bmi,".2f"))+"You are considered fat, it is better to think seriously about losing weight")
                
else:
    print("your bmi is:"+str(format(bmi,".2f"))+"if you dont lose your weight.you will Facing very serious problems")

    print("thanks for choosing our program")
