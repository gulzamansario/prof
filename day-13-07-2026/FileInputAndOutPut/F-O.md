# TYPE OF FILES. 
**There are 2 types of files:** 
1. Text files (.txt, .c, etc) 
2. Binary files (.jpg, .dat, etc) 

### Python has a lot of functions for reading, updating, and deleting files. 


# OPENING A FILE 
***Python has an open() function for opening files. It takes 2 parameters:  filename and 
mode.***


**open("filename", "mode of opening(read mode by default)")**

```
open("this.txt", "r") 
```
# MODES OF OPENING A FILE 
1. r – open for reading 
2. w - open for writing  
3. a - open for appending 
4. "+"  - open for updating. 
5. ‘rb’ will open for read in binary mode. 
6. ‘rt’ will open for read in text mode. 

# WRITE FILES IN PYTHON 

**In order to write to a file, we first open it in write or append mode after which, we use 
the python’s f.write() method to write to the file!**


```markdown
# Open the file in write mode 
f = open("this.txt", "w") 
# Write a string to the file 
f.write("this is nice") 
# Close the file 
f.close() 
```


# `WITH` STATEMENT 
**The best way to open and close the file automatically is the `with` statement.**
**Open the file in read mode using 'with', which automatically closes the
file**


```markdown
with open("this.txt", "r") as f: 
# Read the contents of the file 
text = f.read() 
# Print the contents 
print(text)
```