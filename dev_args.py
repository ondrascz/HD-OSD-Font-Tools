import sys


print(sys.argv[1:])

parsed_args = []
switch_values = []
switch = ""

# iterate over a list of arguments except the first (program file name)
for arg in sys.argv[1:]:
    
    # is the argument a switch?
    if arg[0:1] == "-":
        # append previous switch and its values to parsed arguments list
        parsed_args.append([switch, switch_values])
        # set the name of the current switch
        switch = (arg[1:])
        # clean the list of values for the current switch
        switch_values = []

    # is the argument a switch value?
    else:
        # add argument to the current list of switch's values
        switch_values.append(arg)

# append the last swicth and its values to parsed arguments list
parsed_args.append([switch, switch_values])

print(parsed_args)

for switch in parsed_args:
    print("For an argument \"" + switch[0] + "\" we have following values:")
    for value in switch[1]:
        print("   " + value)