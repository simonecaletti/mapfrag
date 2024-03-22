import argparse
import re
import os

def modify_line(line):
    # Define a regular expression pattern to match the JET function and extract its arguments
    pattern = r'JET(\d+)\((.*?)\)'
    matches = re.findall(pattern, line)
    
    # Iterate over the matches found in the line
    for match in matches:
        jet_function = match[0]  # JET function number
        arguments = match[1]     # Arguments inside the JET function
        
        # Check if '3' is present in the arguments of JET function
        if '3' in arguments:
            # Replace '3' with 'hfrag(3)' inside the JET function
            modified_arguments = arguments.replace('3', 'hfrag(3)')
            
            # Construct the modified JET function string
            modified_jet_function = f'JET{jet_function}({modified_arguments})'
            
            # Replace the original JET function with the modified one in the line
            line = line.replace(f'JET{jet_function}({arguments})', modified_jet_function)

        # Check if 'hfrag(3)' is present in the arguments of JET function
        if '3' not in arguments:
            # If '3' is not found, return None to indicate line removal
            return None            


#        jet_chars = ''
#        jet_numbers = re.findall(r'JET(\d+)\((.*?)\)', line)
#        for jet_number, arguments in jet_numbers:
#            # Extract the next 2 characters after "JET"
#            jet_chars = line[line.find('JET')+3 : line.find('JET')+5]
##            print(jet_chars(0),jet_chars(1))
#                # Transform jet_chars into a vector [X, Y]
#            X, Y = map(int, jet_chars.split(','))
#            print(f"Vector after 'JET': [{X}, {Y}]")




    return line

def main(input_file, output_file):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line in f_in:
            if line.startswith('FN:='+str(os.path.splitext(input_file)[0])):
                line = line.replace(str(os.path.splitext(input_file)[0]),str(os.path.splitext(output_file)[0]) )
            if 'j' in line:
                line = line.replace('j', '3')
            #if 'Q' in line:
            #    line = line.replace('Q', '3')

            modified_line = modify_line(line)
            if modified_line is not None:
                f_out.write(modified_line)





    print("Output file")
    print(str(os.path.splitext(output_file)[0])+'.map')
    print("has been generated successfully.")
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process the input file and modify its content according to specified conditions.")
    parser.add_argument("input_file", help="Path to the input file")
    parser.add_argument("output_file", help="Path to the output file")
    args = parser.parse_args()

    main(args.input_file, args.output_file)

