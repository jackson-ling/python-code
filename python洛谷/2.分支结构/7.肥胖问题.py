# m表示体重（kg）,h表示身高（m）
m,h=map(float,input().split())
BMI=m/(h**2)
if BMI<18.5:
    print('Underweight')
elif 18.5<=BMI<24:
    print('Normal')
elif BMI>=24:
    print(f'{BMI:.6g}')
    print('Overweight')