#Envuelven a otra funcion y permiten ejecutar codigo antes y despues que es llamada.
PASSWORD='12345'

def password_required(func):
    def wrapper():
        password=input('Cual es tu contraseña? ')

        if password == PASSWORD:
            return func()
        else:
            print('La contraseña no es correcta.')
            
    return wrapper

@password_required  #Permite ejecutar logica antes y despues de la funcion
def needs_password():
    print("La contraseña es correcta")

def upper(func):
    def wrapper(*args,**kwargs): #Son los argumentos los keywords o posicionales kwargs
        result=func(*args,**kwargs)
        return result.upper()
    
    return wrapper

@upper
def say_my_name(name):
    return 'Hola, {}'.format(name)

if __name__ == '__main__':
    needs_password()
    print(say_my_name('Daniel'))