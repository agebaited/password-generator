import string
import random
from colorama import init, Fore, Style

def on_ready():
    init(autoreset=True)
    print(Fore.CYAN + r"""
              %%%%%%%#%%%                                                  
            %%%%%+:::::-%%%%%                                              
        ####=.            -*##%%                                           
      #=--                 .-+#%%                                          
    ##:   .                 .++#%                                          
  #*-     ::..                =*#%                                         
 #=      .=++=:               ++*%%%                                       
 #=     .===:    ..            -+*%%%                                      
 #=.   .-=--=====+=:           =*++#%%%%%%%%%%%%%%%%%%%%                   
 #+.   :===--=---:::::=***++++****+++-         =######%%%                  
 #+:. .::..=+==+++++++++++++++#%*-.............=###%%%%@                   
 %+:..::-++++++++++++++++*****-----:...:::::--*%%@@@@                      
 %#+-=++++++++++++++**###=-::::::-**********##%@@                          
  %#*++++++++*********=............*#%                                  ## 
 %#*+++*##%+---:...........  ......:+#                             ######* 
%%****#+-@#-......... .-%%@+........=*                     #####***=....-* 
%%%#=*--*%+:..........=#:#%%*.......=*                 ###*-----........=* 
  %*:*-=#%%-..........+%#%###.......=*             ###*:...............=*  
 %*+-*=::=:....+:......:===-.:---:..=*#   ####=====:...................=*  
 %%%%=-:...................-=------..-*###=............................=*  
 %%%@*=:....:==--===.......:-------..-+................................=*  
  %%%%+-:..................:------=..=+...............................+*   
  %%%@%*-...................:::-=-.:.-+-..............................+*   
   %@ %*+=..................:=+:.. ..=*#:..........=++++++++++++++++++**   
      %=.-=+=::.........:-=+=.    ...=*##=:....:=###                       
     %*-.  =**---=====---*-.     ....=*%%#=....-*%%                        
     %+:..  :+*-::::::-=+..    .....:.:**%#+....:+##                       
     %*-...  :*:......-+..........:-:.:** %*:.....+#%                      
      %=...  .+*-....=-.........:-+:..:*##=........=*%                     
      %+:...  .+-...--:........:--....:-*:.........:+#                     
      %#*:.....+-..:+:........:+-.......*-......-****#                     
     %+**+:..:=-:..:=:......:+=:........*-:=*****                          
   %#---=##=::*:....=+-...:=+...........+*##                               
   %#-----++++=::::..:--=+=:............*=+##                              
   ##-----------:::::::::::::......:..::*=-=##                             
   ##-------------------::::::::::::::::*######                            
   ##*=---------------------------------*#  ##                             
     ##*=----------------------------=+##                                  
      ###**+==++**************------+*#                                    
      #***#*+++##           ####***##                                      
     ##***#######             ###****                                      
    """)


def generate_password(length: int, include_special: bool, include_numbers: bool) -> str:
    characters = string.ascii_letters

    if include_special:
        characters += string.punctuation

    if include_numbers:
        characters += string.digits

    if len(characters) == 0:
        raise ValueError("No characters available to generate a password.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_input(prompt: str, valid_options: list = None) -> str:
    while True:
        choice = input(prompt).strip().lower()
        if valid_options and choice not in valid_options:
            print(f"Invalid choice! Please choose from {valid_options}.")
        else:
            return choice

def save_passwords_to_file(passwords: list, filename: str = "passwords.txt"):
    with open(filename, "a") as file:
        for password in passwords:
            file.write(password + "\n")
    print(f"\nPasswords added to {filename}")

def main():
    try:
        on_ready()

        num_passwords = int(input("Enter the number of passwords to generate: "))
        length = int(input("Enter the password length: "))
        include_special = get_user_input("Include special characters (!?\".>:# etc.) [Y/N]: ", ["y", "n"]) == 'y'
        include_numbers = get_user_input("Include numbers [Y/N]: ", ["y", "n"]) == 'y'

        passwords = [generate_password(length, include_special, include_numbers) for _ in range(num_passwords)]

        print("\nGenerated passwords:")
        for idx, password in enumerate(passwords, 1):
            print(f"{idx}: {password}")

        save_passwords_to_file(passwords)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
