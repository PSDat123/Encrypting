# This is a sample Python script.
import sys
import gc
import os
import Methods


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# try_again_opt_no = {'0', 'n', 'no', 'nah'}
try_again_opt_yes = {'1', 'y', 'yes', 'yep', 'ok'}
exit_opt = {'exit', 'stop', 'quit', 'leave'}
to_encrypt_dir = "to_be_encrypted\\"

enc = "encrypted"

en_m = {
    1: Methods.caesar_cipher
}
is_running = True
while is_running:
    option = input("Encrypt(1) or Decrypt(2): ").lower()
    if option in exit_opt:
        print('shutting down...')
        break

    if option in {'1', 'encrypt'}:
        clear_screen()
        print("Encrypting it is then.")
        print("-" * 30)
        print("---Enter file name to open it---")
        e_file = input("{0}\\{1}".format(os.getcwd(), to_encrypt_dir))
        try:
            with open(to_encrypt_dir + e_file) as f:
                content = f.read()
                e_file_n = e_file.replace(".txt", '')
                print(en_m)
                index = int(input("Choose your encrypting method:"))
                clear_screen()
                print(en_m[index].__name__)

                param = [input("Enter {}: ".format(x)) for x in en_m[index].__code__.co_varnames if x != "content"]
                out = en_m[index](content, *param)
                print("\nOriginal: " + content)
                print("\nNew: " + out)
                with open("{0}\\{1}_{2}.txt".format(enc, e_file_n, en_m[index].__name__), "w") as o:
                    print("\nNew file at {}\n".format(os.getcwd() + "\\" + o.name))
                    o.write(out)

        except FileNotFoundError:
            clear_screen()
            print("File unavailable, try again")
            continue
        except KeyError:
            clear_screen()
            print("Method unavailable, try again")
            continue
        except ValueError:
            clear_screen()
            print("Wrong type of value, try again")
            continue

    elif option in {'2', 'decrypt'}:
        clear_screen()
        print("Decrypting it is then.")
    else:
        try_again = input("Option unavailable, try again ? (yes/no)  :").lower()
        if try_again in try_again_opt_yes:
            clear_screen()
            print('restarting...')
            continue
        else:
            print('shutting down...')
            break

clear_screen()
gc.collect()
sys.exit()
