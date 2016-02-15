#define a function that computes the length of a given list and string.
#(it is true that python has the len() function built in,
#but writing it yourself is nevertheless a good exercise.)

message=()
sum=int()


message=input("Write the string: ")
i=int(message.count("i"))
a=int(message.count("a"))       #do it with all the letters
letters=int(i+a)

print(letters)