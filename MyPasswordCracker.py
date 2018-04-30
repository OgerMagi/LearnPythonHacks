import crypt

def testPass(cryptPass):
    salt = cryptPass[3:11]
    dictfile = open('dictionary.txt', 'r') # Dictionary and accounts.txt in the same directory as script
    cryptandsalt = '$6$' + salt #$6$ == sha512
    for word in dictfile.readlines():
        cryptword = crypt.crypt(word.strip(), cryptandsalt)
        if cryptword == cryptPass:
            return word
        
    return "Not Found!"


def getaccounts(): 
    PFile = open('accounts.txt', 'r') #cat /etc/shadow > accounts.txt
    PasswordFile = PFile.readlines()
    Accounts = []
    for PLine in PasswordFile:
            thisline = PLine.split(':')
            if thisline[1].startswith('$'):
                Accounts.append(thisline)

    return Accounts

def main():
    accounts = getaccounts()
    for account in accounts:
        passwordcheck = testPass(account[1])
        print "User: " + account[0] + " Password: " + passwordcheck       
    

if __name__ == "__main__":
    main()
