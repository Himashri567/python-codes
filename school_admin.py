import csv
def write_csv_info(info_list):
    with open("student_info.csv","a",newline="") as csv_file:
        writer= csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["Name", "Age", "Contact Number", "Email ID"])
        
        writer.writerow(info_list)

if __name__=='main':
    condition=True
    
    while(condition):
        student_info= input("Enter the students information in the following format: [Name, Age, Contact Number, Email ID]")
        student_info_list=student_info.split(' ')
        
        print("\nThe entered information is- \nName: {} \nAge: {} \nContact Number: {} \nEmail ID: {} ".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))

        check_info=input("Check the Entered Student information. If correct enter 'y' otherwise 'n': ")
        if check_info=="y":
            write_csv_info(student_info_list)

            more_info=input("Enter (yes/no) if you want to enter information for another student: ")
            if more_info=="yes":
                condition=True
            elif more_info=="no":
                condition=False
        elif check_info=='n':
            print("Please re-enter the values!")
            