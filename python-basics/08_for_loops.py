names = ['lucy', 'john', 'jenny' , 'bob' , 'mary']
for item in names:
    print(item.capitalize())


names = []   # لیست خالی

# گرفتن 5 اسم از کاربر
for i in range(5):
    name = input("Enter a name: ")
    names.append(name)

# چاپ همه اسم‌ها با حرف اول بزرگ
for item in names:
    print(item.capitalize())