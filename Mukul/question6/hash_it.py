import json

with open('hashes_and_answer.json', 'r') as f:
    data = json.load(f)

string01 = "yoo ISDF"  
string02 = "Hide and Seek"  
string03 = "Bypass CTF"  

for i in range(3):
    print(string01)
    x = input("Enter the md5 hashed value: ")
    if x == data['hashes']['md5']:
        print(string02)
        y = input("Enter the md2 hashed value: ")
        if y == data['hashes']['md2']:
            print(string03)
            z = input("Enter the md4 hashed value: ")
            if z == data['hashes']['md4']:
                print(data['answer'])
                break
            else:
                print("Try Again")
        else:
            print("Try Again")
    else:
        print("Try Again")
