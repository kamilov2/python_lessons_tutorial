import random

clients = {}

for i in range(1,6):
    code_client = random.randint(10000, 99999)
    name = input(f"{code_client} raqam ostidagi user uchun ism kiriting: ").strip().capitalize()
    surname = input(f"{code_client} raqam ostidagi user uchun familiya kiriting: ").strip().capitalize()
    age = input(f"{code_client} raqam ostidagi user uchun yosh kiriting: ").strip()
    if name.isalpha() and surname.isalpha() and age.isdigit():
        if int(age) < 100:
            clients[code_client] = {"ism":name,"familiyasi":surname, "yosh":age}
        else:
            print("Yoshingizni togri kiriting!")

  
    else:
        print("Kiritilishda hatolik!")
        break
print(clients)

        

    
