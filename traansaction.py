#Using without params

def balaji():
    return "This is my bank balance"

#initializing dictionary
#check for function name as a key
test_dict={"fname":balaji,"age":500,"address":"salem"}

#printing original dictionary
print("The original dictionary is:"+str(test_dict))

#calling function using brackets
res=test_dict['fname']()

#printing result
print("The required call result:"+str(res))

#calling function using brackets
test_dict['fname'](10,20)

