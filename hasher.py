import hashlib, sys, time, random, os
from colorama import init

def banner():
    
    global rand
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    rnd = ['91', '92', '93', '94', '95']
    rand = random.choice(rnd)
    print('''\033[%sm 

    |                 |
    | Create By j0hn  |          /\     
    |_________________|         /  \      h  e r (c)  
    |for redants Team |        /____\     s
    |                 |       /      \\


''' % rand)
def encode():
    
    m = hashlib.md5()
    e = bytes(i.encode('utf-8'))
    m.update(e)
    print ('\033[92m[ + ] This is your Hash => %s' % m.hexdigest())

def crack():
    f = open(i, 'r')
    for v in f.readlines():
        v = v.replace('\n','')
        m = hashlib.md5()
        e = bytes(v.encode('utf-8'))
        m.update(e)
        sh = m.hexdigest()
        if sh == a:
            print ('\033[92m[ + ] Password Found :) This is Pass : %s ' % v)
            exit()
        else:
            print ('\033[91m[ * ] Please wait... Not Match :( Pass : %s ' % v)
        pass
def main():
    global i
    global a    
    global l
    init()
    banner()
    print ('[1] Encode Text To md5')
    print ('[2] Decode md5 To Text')
    print ('[99] Exit')
    try:
        l = input('\n ~~> ')
    except:
        exit()
   

    if l == '1':  
        i = input('[ + ] Enter your text : ')
        encode()
    if l == '2':        
        a = input('Enter md5 Hash ~~> ')
        i = input('Enter Passwordlist ~~> ')
        crack()
    if l == '99':
        print ('\033[91mExiting ...')
        exit()
    else:
        pass


while True:
    main()
    o = input('\033[93m[ ~ ] Do You Want to Continue? (Default Y). [y or n] ~~> ')
    if o == 'Y' or 'y':
        main()
    if o == 'N' or 'n':
        print ('\033[91mExiting ...')
        time.sleep(2)
        exit()
    else:
        main()

