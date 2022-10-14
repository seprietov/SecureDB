from site import execusercustomize
from matplotlib.rcsetup import validate_color_or_auto
import mysql.connector as mysql
from regex import R
import requests
import json

from sklearn.model_selection import validation_curve


# connect to db created called "users info"
db = mysql.connect(host="localhost",user="root",password="",database="users info") 
command_handler = db.cursor(buffered=True)

def update():
    ''' # tambien es seguro por que elimina lo que ya no se tenga en la base de datos.
    this function updates the db by deleting all information
    and replacing all the information the information that is 
    stored in the api.'''
    command_handler.execute("DELETE FROM users")
    db.commit()
    response_api = requests.get("https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios")
    data=response_api.text
    parse_json = json.loads(data)
    for dict in parse_json:
        username = (dict["user_name"],)
        command_handler.execute("SELECT * FROM users WHERE user_name = %s",username)
        if command_handler.rowcount <= 0: #se actualiza la informacion para nuevos usuarios, pero la de viejos usuarios no
            vals = []
            for item in dict:
                vals.append(dict[item])
            vals = tuple(vals)  
            command_handler.execute("INSERT INTO users (fec_alta,user_name,codigo_zip,credit_card_num,credit_card_ccv,cuenta_numero,direccion,geo_latitud,geo_longitud,color_favorito,foto_dni,ip,auto,auto_modelo,auto_tipo,auto_color,cantidad_compras_realizadas,avatar,fec_birthday,id) Values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",vals)
    db.commit()


def add_restriction():
    ''''
    add restrictions from different tables 
    as admin would choose '''
    print("")
    print("Register new retriction")
    insider = input(str("is the restriction for insiders? (y/n):   "))
    print("")
    restriction = input(str("What is the new restricted word:  ")).lower()
    
    query_vals = (restriction,)
    if insider == "y":
        command_handler.execute("SELECT * FROM insiders WHERE restriction = %s",query_vals )
        if command_handler.rowcount > 0:
            print("WORD ALREADY RESTRICTED")
            return
        command_handler.execute("INSERT INTO insiders (restriction) Values (%s)",query_vals)
        print(restriction + " WORD HAS BEEN ADDED AS A NEW RESTRICTION")
    elif insider == "n":
        command_handler.execute("SELECT * FROM outsiders WHERE restriction = %s",query_vals )
        if command_handler.rowcount > 0:
            print("WORD ALREADY RESTRICTED")
            return
        command_handler.execute("INSERT INTO outsiders (restriction) Values (%s)",query_vals) 
        print(restriction + " WORD HAS BEEN ADDED AS A NEW RESTRICTION")  
    else:
        ()
    db.commit()

def elim_restriction():
    ''''
    eliminate restrictions from different tables 
    as admin would choose 
    '''
    print("")
    print("Delete existence retriction")
    insider = input(str("is the restriction for insiders? (y/n):   "))
    print("")
    restriction = input(str("What is the restricted word:  ")).lower()
    query_vals = (restriction,)
    if insider == "y":
        command_handler.execute("SELECT * FROM insiders WHERE restriction = %s",query_vals )
        if command_handler.rowcount == 0:
            print(restriction+" WORD IS NOT RESTRICTED YET")
            return
        command_handler.execute("DELETE FROM insiders WHERE restriction = %s",query_vals)
        print(restriction+" HAS BEEN REMOVED FROM RESTRICTED WORDS")
    elif insider == "n":
        command_handler.execute("SELECT * FROM outsiders WHERE restriction = %s",query_vals )
        if command_handler.rowcount == 0:
            print(restriction+" WORD IS NOT RESTRICTED YET")
            return
        command_handler.execute("DELETE FROM outsiders WHERE restriction = %s",query_vals)
        print(restriction+" HAS BEEN REMOVED FROM RESTRICTED WORDS")
    else:
        print("INPUT NOT CLEAR") 
    db.commit()

def requester_query(inside):
    '''
    this function checks if the requester is from inside or outside company
    different restrictions are checked
    '''
    print("")
    print("Whats your Query? ")
    query = input(str(""))
    query = query.lower()
    if inside == "y":
        command_handler.execute("SELECT restriction FROM insiders")
        not_allowed = command_handler.fetchall()
    elif inside == "n":
        command_handler.execute("SELECT restriction FROM outsiders")
        not_allowed = command_handler.fetchall()
    else:
        print("INPUT NOT CLEAR")
        return (0,)
    count = 0

    for item in not_allowed:
        if item[0] in query:
            count = count + 1
    if count == 0:
        command_handler.execute(query)
        records = command_handler.fetchall()
    else:
        return (0,)

    return records

def admin_session():
    update()
    '''
    In this function we have the logic for when the adming
    access, here he can create and delete Requesters.
    '''
    print("")
    print("Login success welcomme admin: ")
    print("")
    while 1:
        print("Admin Menu")
        print("1. Create new Requester")
        print("2. Delete existing Requester")
        print("3. Create new restriction")
        print("4. Delete restriction")
        print("5. Log out")

        user_option = input(str(("Option:  ")))
        if user_option == "1":
            print("")
            print("Register new Requester")
            requestername = input(str("Requester name:  "))
            password = input(str("Requester password:  "))    
            inside = input(str("Requester from inside company? (y/n):  "))
            responsable = input(str("What is the name of the person in charged?:  "))
            query_vals = (requestername,password,inside,responsable)
            req_vals = (requestername,)
            command_handler.execute("SELECT * FROM requesters WHERE requestername = %s",req_vals)
            if command_handler.rowcount > 0:
                print("the requester "+requestername+" in already registered")
                continue
            command_handler.execute("INSERT INTO Requesters (requestername, password, inside,responsable) Values (%s,%s,%s,%s)",query_vals)
            db.commit()
            print(requestername + " has been registered as a requester")
        elif user_option == "2":
            print("")
            print("Delete Requester Account: ")
            requestername = input(str("Requestername:  "))
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
            add_restriction()
        elif user_option == "4":
            elim_restriction()
        elif user_option == "5":
            break
        else:
            print("")
            print("NOT VALID CREDENTIAL.")

def requester_session(inside):
    '''
    This is the function where the logic for the requester user
    is implemented, the requester can run querys with certain
    restrictions, this restrictions can be modified to the liking
    '''
    while 1:
        print("")
        print("Requester's Menu")
        print("1. Make a Query")
        print("2. Logout")
        user_option = input(str("Option:  "))
        if user_option == "1":
            while 1:
                records = requester_query(inside)
                if records == (0,):
                    print("QUERY NOT ALLOWED.")
                    break
                else:
                    for record in records:
                        print("")
                        print(record) 
                    break     
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
    username = input(str("Admin name:  "))
    password = input(str("Password:  "))
    query_vals = (username,password)
    command_handler.execute("SELECT * FROM admins WHERE admin_name = %s AND password = %s",query_vals)
    if command_handler.rowcount <=0:
        print("Login not recognized")
    else:
        print("Welcome Admin: {}".format(username))
        admin_session()


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
        requester_session(inside)



def main():
    '''
    a simple menu that runs on a loop and let you login as admin
    or requester
    '''
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
