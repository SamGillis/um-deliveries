def deliveries(the_file):
    """Takes in a file, prints each line as a sentence and returns to
    main program  """
    ##loops through each line in the file
    for line in the_file: 
        ## strips each line to an idividual string
        line = line.rstrip()
        ## splits the line based on the separation'|'
        words = line.split('|')

        ##parses out the variable so they can be inputed correctly into the printed 
        melon = words[0]
        count = words[1]
        amount = words[2]

        ##prints the sales report
        print("Delivered {} {}s for total of ${}".format(
          count, melon, amount))
    return

print("Day 1")
the_file = open("um-deliveries-20140519.txt")
deliveries(the_file)
the_file.close()


print("Day 2")
the_file = open("um-deliveries-20140520.txt")
deliveries(the_file)
the_file.close()


print("Day 3")
the_file = open("um-deliveries-20140521.txt")
deliveries(the_file)
the_file.close()
