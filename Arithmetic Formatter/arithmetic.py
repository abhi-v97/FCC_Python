def arithmetic_arranger(problems, ans=False):
    #Easy challenge, tedious to get the output the solution checker wanted as a single wrong space
    #broke the solution checker. Good starter challenge overall.
    
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    if len(problems) > 5:  # check number of problems
        return "Error: Too many problems."

    for x in problems:

        y = x.split(" ")

        num = y[0]
        den = y[2]
        op = y[1]

        #check digits and length
        if len(num) > 4 or len(den) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if not num.isnumeric() or not den.isnumeric():
            return 'Error: Numbers must only contain digits.'

        maxlen = max(len(num), len(den))
        num2 = num.rjust(maxlen + 2)
        den2 = op + " " + den.rjust(maxlen)

        # add white space to space out the problems as required
        line1 += num2 + "    "
        line2 += den2 + "    "
        line3 += ("-"*(maxlen+2)) + "    "

        if op == "+":
            total = str(int(num) + int(den)).rjust(maxlen + 2)
            line4 += total + "    "
        elif op == "-":
            total = str(int(num) - int(den)).rjust(maxlen + 2)
            line4 += total + "    "
        else:
            return "Error: Operator must be '+' or '-'."

    # solution checker didn't like extra white space on the right, rstrip removes it
    line1 = line1.rstrip()
    line2 = line2.rstrip()
    line3 = line3.rstrip()
    line4 = line4.rstrip()

    if ans == True:
        arranged_problems = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4

    else:
        arranged_problems = line1 + "\n" + line2 + "\n" + line3

    return arranged_problems

if __name__ == "__main__":
    print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
    print("    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----")
