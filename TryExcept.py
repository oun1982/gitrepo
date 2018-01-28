__author__ = 'oun1982'
'''
try:
    fh = open("myfile", "w")
    fh.write("This is my file exception handling!!!")
except IOError:
    print("Error : Can\'t find file ore read data")
else:
    print("Write content in the file successfully")
    fh.close()

while True:
    try:
        n = int(input("Please enter an interger :"))
        break
    except ValueError:
        print("No valid value! Please try again...")
print("Great ,you sucessfully enter an integer!")
'''
def temp_convert(var):
    try:
        return int(var)
    except ValueError as Args:
        print("Argument doesn't contain number\n", Args.args)
temp_convert("xyz")


