import re
def main():
    M_num = "+919100904055"
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[1-9][A-Za-z\d@$!#%*?&]{6,20}$"

    # compiling regex
    pat = re.compile(reg)

    # searching regex
    mat = re.search(pat, M_num)

    # validating conditions
    if mat:
        print("Password is valid.")
    else:
        print("Password invalid !!")


# Driver Code
if __name__ == '__main__':
    main()