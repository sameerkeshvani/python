class student:
    sname = "Sameer"
    marks = 69
print(f"Student Name:{getattr(student,'sname')}\nMarks:{getattr(student,'marks')}")
print("After modification")
setattr(student,'sname',"Sameer Keshvani")
setattr(student,'marks',"96")
print(f"Student Name:{getattr(student,'sname')}\nMarks:{getattr(student,'marks')}")  