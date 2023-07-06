from databases import Student

try:
    jina = input("Enter Name\n")
    nambari = input("Enter Phone Number\n")
    umri = input("Enter Age\n")
    jinsia = input("Enter Gender\n")
    kitambulishi = input("Enter Studentcode\n")

    Student.create(name = jina, phoneno = nambari, age = umri, gender = jinsia, studentcode = kitambulishi)
    print("Student Created Successfully")

except:
    print("Failed to create student")
