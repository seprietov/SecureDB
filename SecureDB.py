from site import execusercustomize
from matplotlib.rcsetup import validate_color_or_auto
import mysql.connector as mysql
import requests
import json

from sklearn.model_selection import validation_curve


# connect to db created called "users info"
db = mysql.connect(host="localhost",user="root",password="",database="users info") ### aqui puede que no funcione por el espacio
#db object thata allows to run different querys, and buffered = True to run multiples querys
command_handler = db.cursor(buffered=True)

def update():
    '''
    this function auto-updates each day the db
    pulling the information from api'''
    command_handler.execute("DELETE FROM users")
    db.commit()
    response_api = requests.get("https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios")
    #print(response_api.status_code)
    data=response_api.text
    parse_json = json.loads(data)
    #print(type(parse_json))
    for dict in parse_json:
        username = (dict["user_name"],)
        command_handler.execute("SELECT * FROM users WHERE user_name = %s",username)
        if command_handler.rowcount <= 0: #se actualiza la informacion para nuevos usuarios, pero la de viejos usuarios no
            vals = []
            for item in dict:
                vals.append(dict[item])
            vals = tuple(vals)  
            #print(vals)
            command_handler.execute("INSERT INTO users (fec_alta,user_name,codigo_zip,credit_card_num,credit_card_ccv,cuenta_numero,direccion,geo_latitud,geo_longitud,color_favorito,foto_dni,ip,auto,auto_modelo,auto_tipo,auto_color,cantidad_compras_realizadas,avatar,fec_birthday,id) Values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",vals)
    db.commit()


def admin_session():
    update()
    '''
    In this function we have the logic for when the adming
    acces with the valid credentials, here he could create 
    and delete Requesters.
    '''
    print("")
    print("Login success welcomme admin: ")
    print("")
    while 1:
        print("Admin Menu")
        print("1. Create new Requester")
        print("2. Delete existing Requester")
        print("3. Log out")

        user_option = input(str(("Option:  ")))
        if user_option == "1":
            print("")
            print("Register new Requester")
            requestername = input(str("Requester name:  "))
            password = input(str("Requester password:  "))    
            inside = input(str("Requester from inside company? (y/n):  "))
            responsable = input(str("What is the name of the person in charged?:  "))
            query_vals = (requestername,password,inside,responsable)
            command_handler.execute("INSERT INTO Requesters (requestername, password, inside) Values (%s,%s,%s)",query_vals)
            db.commit()
            print(requestername + " has been registered as a requester")
        elif user_option == "2":
            print("")
            print("Delete Requester Student Account: ")
            requestername = input(str("Studen Requestername:  "))
            inside = input(str("Requester from inside company? (y/n):  "))
            responsable = input(str("What is the name of the person in charged?:  ")) #esta parte se agrega como seguridad de confirmacion
            query_vals = (requestername,inside, responsable)
            command_handler.execute("DELETE FROM requesters WHERE requestername = %s AND inside = %s AND responsable = %s",query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("")
                print("There is no {} requester found".format(requestername))
            else: 
                print("")
                print(requestername + " has been deleted") 
        elif user_option == "3":
            break
        else:
            print("")
            print("NOT VALID CREDENTIAL.")

def requester_session():
    while 1:
        print("")
        print("Requester's Menu")
        print("1. Make a Query")
        print("2. Logout")
        user_option = input(str("Option:  "))
        if user_option == "1":
            while 1:
                print("Whats your Query? ")
                query = input(str(""))
                query = query.lower()
                no_allowed = ["admins","requesters","delete"] ## esto se hace para lograr mas seguridad impique que cualquier apueda ingreasar a la info
                count = 0
                for item in no_allowed:
                    if item not in query:
                        count = count + 1
                if count == len(no_allowed):
                    command_handler.execute(query)
                    records = command_handler.fetchall()
                    for record in records:
                        print("")
                        print(record)
                    break
                else: 
                    print("QUERY NOT ALLOWED.")
        elif user_option == "2":
            break
        else:
            print("NOT VALID OPTION")


def auth_admin():
    '''
    This function works to authenticate de admin, if credentials corrects
    run admin_session function else, return to main()
    '''
    print("")
    print("Admin login")
    print("")
    username = input(str("Adminname:  "))
    password = input(str("Password:  "))
    query_vals = (username,password)
    command_handler.execute("SELECT * FROM admins WHERE admin_name = %s AND password = %s",query_vals)
    if command_handler.rowcount <=0:
        print("Login not recognized")
    else:
        print("Welcome Admin: {}".format(username))
        requester_session()


def auth_requester():
    '''
    this function allows for the authentication of the requeter by asking
    only access if all information is correct, else returns to main()
    '''
    print("")
    print("Requester's Login. ")
    print("")
    requestername = input(str("Requester name:  "))
    password = input(str("Password:  "))
    inside = input(str("Requester from inside company? (y/n):  "))
    query_vals=(requestername,password, inside)
    command_handler.execute("SELECT * FROM requesters WHERE requestername = %s AND password = %s AND inside = %s",query_vals)
    if command_handler.rowcount <=0:
        print("Login not recognized")
    else:
        print("Welcome requester {}".format(requestername))
        requester_session()



def main():
    
    while 1:
        print("")
        print("Welcome to users info database")
        print("")
        print("1. Login as Admin")
        print("2. Login as Requester")

        user_option = input(str("Option :   "))
        if user_option == "1":
            auth_admin()
        elif user_option == "2":
            auth_requester()
        else:
            print("")
            print("NOT VALID CREDENTIAL.")


main()