#Importamos las librerias
from flask import Flask, redirect, render_template, request, url_for
#Intanciar la aplicacion
app = Flask(__name__, template_folder='templates')

#Array donde almacenaremos los datos
lista_clientes = []

#Decorador para definir la ruta del inicio
@app.route('/')
def index():
    return render_template('index.html', lista_clientes = lista_clientes)

#Decorador para definir la ruta del login
@app.route('/login')
def login():
    return render_template('login.html', lista_clientes = lista_clientes)

#Decorador para definir la ruta del registro
@app.route('/registro')
def registro():
    return render_template('registro.html', lista_clientes = lista_clientes)

#Decorador para definir la ruta del home
@app.route('/home')
def home():
    return render_template('home.html', lista_clientes = lista_clientes)

#Decorador para definir la ruta del chat
@app.route('/chat')
def chat():
    return render_template('chat.html', lista_clientes = lista_clientes)

#Controlador de la ruta de envio de datos
@app.route('/enviar', methods=['POST'])                             
def enviar():                                                       #crea la funcion enviar
    if request.method == 'POST':                                    #Condicion que solicita que el metodo sea igual a post
        nombre_usuario = request.form['nombre_usuario']             #Extrae los datos ingresados en el input de la descripcion del usuario
        email_usuario = request.form['email_usuario']               #Extrae los datos ingresados en el input del correo electronico
        contrasenia_usuario = request.form['contrasenia_usuario']   #Extrae los datos ingresados en el input de la contraseña
        #Crea la condicion de que no guarde el registro cuando el campo de la tarea y el del correo estan vacios
        if nombre_usuario == '' or email_usuario == '' or contrasenia_usuario == '':            
            return redirect(url_for('login'))                       
        else:
            #Agrega a la lista los campos llenos
            lista_clientes.append({'nombre_usuario': nombre_usuario, 'email_usuario': email_usuario, 'contrasenia_usuario': contrasenia_usuario})
            return redirect(url_for('home'))

#Controlador de la ruta de comparacion de datos
@app.route('/ingresar', methods=['POST'])                             
def ingresar():                                                         #crea la funcion ingresar
    if request.method == 'POST':                                        #Condicion que solicita que el metodo sea igual a post
        nombre_usuario = request.form['nombre_usuario']                 #Extrae los datos ingresados en el input de la descripcion del usuario
        email_usuario = request.form['email_usuario']                   #Extrae los datos ingresados en el input del correo electronico
        contrasenia_usuario = request.form['contrasenia_usuario']       #Extrae los datos ingresados en el input de la contraseña
        #Crea la condicion de que no guarde el registro cuando el campo de la tarea y el del correo estan vacios
        if nombre_usuario == '' or email_usuario == '' or contrasenia_usuario == '' or lista_clientes == [] or lista_clientes != lista_clientes:            
            return redirect(url_for('login'))                       
        else:
            #re dirije a la pagina de inicio
            return redirect(url_for('home'))


#Controlador de la ruta para chatear
@app.route('/chat', methods=['POST'])
def chatear():
    return redirect(url_for('chat'))  # Redireccionar a la página de chat

#Controlador de la ruta para salir del chat
@app.route('/home', methods=['POST'])
def salir():
    return redirect(url_for('home'))  # Redireccionar a la página de home
        
#Controlador de la ruta para cerrar sesion
@app.route('/logout', methods=['POST'])
def logout():
    return redirect(url_for('index'))  # Redireccionar a la página de inicio

#main del programa
if __name__ == '__main__':
    app.run(debug=True)     #debug para reiniciar el servidor