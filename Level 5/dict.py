marks = {
    "Math" : 95,
    "Physics" : 97,
    "Chemistry": 94
}
print(marks)

print(marks["Physics"])

#add
marks["English"] = 95
print(marks)

#update
marks["Physics"] = 100
print(marks)

print("Math" in marks)

for subject in marks:
    print(subject, marks[subject])