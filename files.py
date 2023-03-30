# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname,'r')
fc=fh.read()
fi=(fc.upper())
print(fi.rstrip())