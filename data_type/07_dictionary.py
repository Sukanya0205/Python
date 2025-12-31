marks ={"Om":78,"Yash":80,"Sahil":100}
print(marks,type(marks))

print(marks["Om"])
marks["Yash"]= 89
print(marks)

print(marks.keys())
marks.pop("Sahil")
print(marks)