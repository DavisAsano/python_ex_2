# Python refresher exercises 2 - task 1

# Write and test a function is_valid_email_address(s) that evaluates string s as a valid email address 
# Returns: tuple of 2 elements (res, err):
#          res contains the result (None or error code)
#          err contains an error string ("seems legit" for None,  a short error message for the error code
#
# Rules: (these are mine, not the official web standards!)
# must have 3 parts: <A>@<B>.<C>
# A must have between 3 and 16 alpha numeric chars (test: isalnum()) 
# B must have between 2 and 8 alpha numeric chars (test: isalnum()) 
# C must be one of these:  com edu org gov 
#
# Here are some tests and the expected results:
# 
# charding@iastate.edu (None, 'Seems legit')
# chris.edu (1, 'Must have exactly one @!') x 
# chris@edu (4, 'post @ part must have exactly one dot!') x
# @bla.edu (2, 'pre @ part must contain 3 - 16 alfanum chars') x 
# throatwobblermangrove@mpfc.org (2, 'pre @ part must contain 3 - 16 alfanum chars') x
# chris@X.com (5, 'part after @ and before . must contain 2 - 8 alfanum chars') x
# chris.harding@iastate.edu (3, 'pre @ part must only contain alfanum chars') x
# chris@pymart.biz (7, 'past-dot part invalid, must be from: com, edu, org, gov') x 
# chris@letsgo!.org (6, 'part after @ and before . must only contain alfanum chars') x
# chris@megasavings.org (5, 'part after @ and before . must contain 2 - 8 alfanum chars') x 
# tc@tank.com (2, 'pre @ part must contain 3 - 16 alfanum chars')
#
# your function MUST react the same (OK or error) but you don't have to use my exact error messages or codes 
# just something similar to that effect. You could even be more helpful e.g. 
# "throatwobblermangrove is too long (21 chars), must be 3 - 16"
# It's OK to bail out at the first proven error, even if there would have been more errors later!
# Also, I prb. forgot some possible edge cases, please add more if needed!

# As proof, please manually copy/paste the console output for one run into a file called
# results1.txt

def is_valid_email_address(s):
    
    # your code here

    count_at = s.count("@")
    if count_at != 1:
        return 1, 'Must have exactly one @!'

    split_addy = s.split("@") #split email at @
    count_dot = split_addy[1]  #count number of . after @
    if count_dot.count(".") != 1:
        return 4, 'post @ part must have exactly one dot!'

    count_pre = len(split_addy[0]) #count length of pre @
    alf_pre = split_addy[0]
    if count_pre < 3 or count_pre > 16: # pre @ contains 3-16 alfnum
        return 2, 'pre @ part must contain 3 - 16 alfanum chars'
    if alf_pre.isalnum() == False:
        return 3, 'pre @ part must only contain alfanum chars'
    
    after = count_dot.split(".") #split at .
    count_predot = after[0]
    count_afterdot = after[1]
    if len(count_predot) < 2 or len(count_predot) > 8: # before and after @ 2-8 characters alfnum
        return 5, 'part after @ and before . must contain 2 - 8 alfanum chars'
    if len(count_afterdot) < 2 or len(count_afterdot) > 8:
        return 5, 'part after @ and before . must contain 2 - 8 alfanum chars'
    if count_predot.isalnum() == False or count_afterdot.isalnum == False:
        return 6, 'part after @ and before . must only contain alfanum chars'

    if count_afterdot not in ["com","edu","org","gov"]: 
        return 7, 'past-dot part invalid, must be from: com, edu, org, gov'

    else:
        return None, 'Seems legit'





# This if ensures that the following is NOT run if this file was imported as a module (which we'll do next!)
if __name__ == "__main__":

    # tests, including edge cases (incomplete? add more!)
    email_list = ["charding@iastate.edu", 
        "chris.edu",
        "chris@edu",
        "@bla.edu",
        "throatwobblermangrove@mpfc.org", 
        "chris@X.com",
        "chris.harding@iastate.edu",
        "chris@pymart.biz",
        "chris@letsgo!.org",
        "chris@megasavings.org",
        "tc@tank.com",
        ]
    # validate each email from the list
    for e in email_list:
        r, s = is_valid_email_address(e) 
        if r == None:
            print(e, s) # OK
        else:
            print(f"{e} - error: {s}, error code: {r}") # Error

        
