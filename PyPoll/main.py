
import os
import csv
vote_count = 0
chingis_count = 0
correy_count = 0
li_count = 0
#I couldn't resist this one.  
# "You movie buffs might likes this, both of his names are slang for penis." --Peter Griffin
peter_count = 0


#tells what file we're working on. Need to look up what the os.path.join means
input_file = os.path.join('..', 'Resources', 'election_data.csv')

#open file and skip line, rename work file as pypollwork, I don't like underscores
#the profession will bend to my will
with open (input_file, newline = '' ) as pypollwork:
    pypollwork = csv.reader(pypollwork, delimiter = ',')
    next(pypollwork)
    for row in pypollwork:
        #set counters.  And they're off!
        vote_count = vote_count + 1
        if row[2] == "Khan":
            chingis_count = chingis_count + 1
        if row[2] == "Correy":
            correy_count = correy_count + 1
        if row[2] == "Li":
            li_count = li_count + 1
        if row[2] == "O'Tooley":
            peter_count = peter_count + 1

#Calculate percentages, I like details
chingis_percentage = float((chingis_count/vote_count)*100)
correy_percentage = float((correy_count/vote_count)*100)
li_percentage = float((li_count/vote_count)*100)
peter_percentage = float((peter_count/vote_count)*100)

#Calculate Winner
#I know there are better, less "hard coded" ways to do this, but this seems shortest (mostly in time)for the 
#given data. And my experience level.  If there were 50 candidates, I would have looked to do it that way. 
if chingis_count > correy_count and chingis_count > li_count and chingis_count > peter_count:
    most_corrupt = str("Khan")
if correy_count > chingis_count and correy_count > li_count and correy_count > peter_count:
    most_corrupt = str("Correy")
if li_count > correy_count and li_count > chingis_count and li_count > peter_count:
    most_corrupt = str("Li")
if peter_count > correy_count and peter_count > li_count and peter_count > chingis_count:
    most_corrupt = str("O'Tooley")



print(f"")
print(f"")
most_corrupt_results = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {vote_count}\n"
    f"-------------------------\n"
    f"Khan: {chingis_percentage}%" + f" ({chingis_count})\n"
    f"Correy: {correy_percentage}%" + f" ({correy_count})\n"
    f"Li: {li_percentage}%" + f" ({li_count})\n"
    f"O'Tooley: {peter_percentage}%" + f" ({peter_count})\n"
    f"-------------------------\n"
    f"Winner: {most_corrupt}\n"
    f"-------------------------\n")
print(most_corrupt_results)

#Output to csv not working. I thought pypollwork would work but it doesn't/  What
# goes in the last parentheses?  Am I supposed to put all the print statements into something?
# triesd that.  My output file is still empty.  Need help. Going to bed.
output_path = os.path.join('..', 'PyOut', 'poll_analysis.csv')
with open (output_path,  "w", newline = "") as datafile:
    writer = csv.writer(datafile, delimiter=',')
    writer.writerows(most_corrupt_results)
