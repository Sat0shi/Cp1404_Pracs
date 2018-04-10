from Prac_7.programming_language import ProgrammingLanguage
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(ruby)
print(python)
print(visual_basic)

program_list = [["Ruby", "Dynamic", True, 1995], ["Python", "Dynamic", True, 1991], ["Visual Basic", "Static", False, 1991]]
print('The dynamically typed languages are:')
for item in program_list:
    list_value = ProgrammingLanguage(item[0], item[1], item[2], item[3])
    if list_value.is_dynamic():
        print(item[0])