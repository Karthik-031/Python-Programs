try:
    file=open("myfile.txt","r")
except I0Error:
    print("Error:unable to read the file!")
finally:
    file.close()
