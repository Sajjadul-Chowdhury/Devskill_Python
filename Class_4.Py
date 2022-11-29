print('Hello')
"""
num_1= float(input("Enter a number : "))
square_value= int(num_1**2)
print(square_value)
"""
#new_input = int(input("Enter a number "))
new_list = [ ]
for i in range(10):
    new_input = int(input("Enter a number "))
    if new_input==0:
        print("End of loop")
        break
    elif new_input>0 or new_input<0:
        
        if new_input not in new_list:
            new_list.append(new_input)
            #new_list.remove(new_input)
            #print("Already in the lest")
        else:
            print("Already in the lest")   
            continue
        #print(new_list)
print(new_list)