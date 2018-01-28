__author__ = 'oun1982'
def tmp_covert(var):
    try:
        return int(var)
    except ValueError as err:
        print ("Argument doesn't contain number \n",err.args)
tmp_covert("aaa")