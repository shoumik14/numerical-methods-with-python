from sympy import *
# this function takes the equation from the user as a mathematical expression
def get_user_input():
    expression_str = input("Enter a mathematical function using 'x' as the variable(must be a valid python expression): ")
    x = symbols('x')
    
    try:
        expression = sympify(expression_str)
        return expression, x
    except Exception as e:
        print(f"Error: {e}")
        return None, None
    

func,x=get_user_input()
res=float(input("Enter the initial guess: "))

if func is not None and x is not None:
    for i in range(10):
        #the usual Newton-Rapshon iteration formula
        res=res-(func.evalf(subs={x:res})/diff(func).evalf(subs={x:res}))
        print(f"after iteration {i+1}, the result = {res}")