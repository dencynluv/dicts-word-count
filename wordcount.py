# write a function 
# open test.txt
# count how many times each space_seperated word occurs
# print out the counts 

# empty dictionary
words = {}

# open the test.txt file
data = open("test.txt")

# for loop that iterates over the test.txt file
for line in data:
# strips the new line character from the right side of the line 
    line = line.rstrip()
# spliting each line at the spaces and binding the line to data
    data = line.split(" ")
    # print data
    # break

# create if statement(with .get) that checks for keys in dictionary
    # words = data.get("As", )

    if "As" in words:
        #quantity = data["As"]
        print "quantity"
    else:
        words["As"] = 1 
        print words
        # print data 


# data = each unique word is a key     
# now that we have the data
# identify each unique word (by space on either side)
# how do we count the number of times a word appears
    

# data is a list 
# we want to loop over this list 
# and add every unique item to the words dictionary as a key
