from schoolfilesystem import SchoolAssessmentSystem

# filename1 = input("File name: ")
# type_file = input("File type: ")
# if type_file == "csv":
#     if not filename1.endswith('.csv'):
#         filename1 += '.csv'
# elif type_file == "txt":
#     if not filename1.endswith('.txt'):
#         filename1 += '.txt'
# elif type_file == "xlsx":
#     if not filename1.endswith('.xlsx'):
#         filename1 += '.xlsx'
# SchoolAssessmentSystem.process_file(filename1)

url = input("URL: ")
SchoolAssessmentSystem.fetch_web_data(url)

if SchoolAssessmentSystem.fetch_web_data(url) is None:
    print("Failed")
else:
    destination_file = input("Destination file: ")
    type_file = input("File type: ")
    if type_file == "csv":
        if not destination_file.endswith('.csv'):
            destination_file += '.csv'
    elif type_file == "txt":
        if not destination_file.endswith('.txt'):
            destination_file += '.txt'
    elif type_file == "xlsx":
        if not destination_file.endswith('.xlsx'):
            destination_file += '.xlsx'

    SchoolAssessmentSystem.transfer_data(SchoolAssessmentSystem.process_file(url), destination_file)




