file = open("input.txt", "r")
data = file.read()
file.close()
seat_number = 0
col_number = 0
row_number = 0
# splitting text and converting to list
phrase_to_list = data.split()
# define a list with valid seat ID range (not very front not very back)
# we assume that input data is also in this range
seat_list = list(range(12, 872))
# since the arrangment is binary we can calculate seat ID with converting every 10 character to number
for i in range(0, len(phrase_to_list)):
    temp_Str = phrase_to_list[i]
    # check if list item has valid length
    if len(temp_Str) == 10:
        for j in range(0, 10):
            # Calculating row by B and F characters
            if j >= 0 and j < 7:
                # check valid characters and their order.first 7 character can be F or B and last 3 character R or L
                if (temp_Str[j] == 'B' or temp_Str[j] == 'F'):
                    # B and R characters are as bit '1'
                    if temp_Str[j] == 'B':
                        row_number = row_number*2 + 1
                    # F and L characters are as bit '0'
                    if temp_Str[j] == 'F':
                        row_number = row_number*2
                else:
                    # in case of invalid character
                    row_number = 0
            # Calculating column by R and L characters        
            if j >= 7 and j < 10:
                if (temp_Str[j] == 'R' or temp_Str[j] == 'L'):
                    # B and R characters are as bit '1'
                    if temp_Str[j] == 'R':
                        col_number = col_number*2 + 1
                    # F and L characters are as bit '0'
                    if temp_Str[j] == 'L':
                        col_number = col_number*2
                else:
                    # in case of invalid character
                    col_number = 0
    seat_number = row_number*8 + col_number
    row_number = 0
    col_number = 0
    # check if number exist in the list or not
    exist_count = seat_list.count(seat_number)
    if exist_count > 0:
        # remove converted numbers from list of seats
        seat_list.remove(seat_number)
        seat_number = 0

# In case of more than one seat we will uncomment these two lines
# if len(a_list) > 1:
#     print("Your seat ID is one of "+ str(a_list))

if len(seat_list) == 1:
    print("\nYour seat ID is " + str(seat_list) + '\n')
