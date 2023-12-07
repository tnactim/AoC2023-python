calibrationValues = []

def sum_calibration_values(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            
            # find the digits per line
            first_digit = next((char for char in line if char.isdigit()), None)
            last_digit = next((char for char in line[::-1] if char.isdigit()))
            
            # concat the string digits and convert to int
            coordinate = first_digit + last_digit
            coordinate = int(coordinate)

            # add converted coordinate to a list to summed
            calibrationValues.append(coordinate)
    
    # sum the list at the end
    print(sum(calibrationValues))
    
file_path = 'input.txt'
sum_calibration_values(file_path)