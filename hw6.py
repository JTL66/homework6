#P1
import os
import sys

number_of_command_line_arguments = len(sys.argv)

print(number_of_command_line_arguments)

print(os.path.abspath(sys.argv[0]))

while os.path.exists(str(sys.argv[0])):
	os.path.exists(str(sys.argv[0]))
	continue
	print("True")
else:
	print("Alert")


#P2
import json, os
import shutil

PARENT_DIR = "quotes_output"

with open("quotes.json", 'r') as quotes_file:
	data = json.load(quotes_file)

#if the parent directory already there, we will delete it
if os.path.exists(PARENT_DIR):
	shutil.rmtree(PARENT_DIR)#os.rmdir(PARENT_DIR)

os.mkdir(PARENT_DIR) #parent directory
os.chdir(PARENT_DIR) #change directory so that we are inside the parent directory
print("Created parent directory ", PARENT_DIR)

for node in data:
	corrected_author = node["author"] if node["author"] is not None else "Unknown"
	dir_name = corrected_author.replace(" ", "_")
	os.mkdir(dir_name) 
	if not(os.path.exists(dir_name)):
		print("{} already exists".format(dir_name))
		os.chdir(dir_name) # go inside the newly created directory
		out = open("quote.txt", "a")
		out.write(node["text"])
		out.write("\n\n")
		out.close()
	if os.path.exists(quote.txt):
		if not os.path.exists(quote_2.txt):
			out = open("quote_2.txt","a")
			out.write(node["text"])
			out.write("\n\n")
			out.close()
		else:
			out = open("quote_3.txt","a")
			out.write(node["text"])
			out.write("\n\n")
			out.close()
	else:
			out = open("quote.txt", "a")
			out.write(node["text"])
			out.write("\n\n")
			out.close()
			os.chdir("..") # go one level up in the directory tree

#P3
import sys
import os

def main():
    # Process command-line arguments
    if len(sys.argv) > 2:  # Command-line arguments are kept in a list 'sys.argv'
        print(__doc__)
        sys.exit(1)        # Return a non-zero value to indicate abnormal termination
    elif len(sys.argv) == 2:
        dir = sys.argv[1]  # directory given in command-line argument
    else:
        dir = '.'          # default current directory

    # Verify dir
    if not os.path.isdir(dir):
        print('error: {} does not exists'.format(dir))
        sys.exit(1)

    # Recursively walk thru from dir using os.walk()
    for curr_dir, subdirs, files in os.walk(dir):
        print('D:', os.path.abspath(curr_dir))    # print currently walk dir
        for subdir in sorted(subdirs):  # print all subdirs under "curr_dir"
            print('SD:', os.path.abspath(subdir))
        for file in sorted(files):      # print all files under "curr_dir"
            print(os.path.join(os.path.abspath(curr_dir), file))  # full filename

if __name__ == '__main__':
    main()




#P4
import timeit
def shelf():
	def dictionary():
	def timer(function):
		def new_function():
    start_time = timeit.default_timer()
    function()
    elapsed = timeit.default_timer() - start_time
    print('Function "{name}" took {time} seconds to complete.'.format(name=function.__name__, time=elapsed))
  return new_function()
@timer
def addition():
  total = 0
  for i in range(0,1000000):
    total += i
  return total




