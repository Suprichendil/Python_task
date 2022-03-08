from datetime import datetime
now=datetime.now()
format1 = now.strftime("%m/%d/%Y")
print("Date Format-1",format1)

format2 = now.strftime("%d/%m/%y")
print("Date Format-2",format2)

format3 = now.strftime("%d/%m/%Y")
print("Date Format-3", format3)

format4 = now.strftime("%m-%d-%Y")
print("Date Format-4", format4)

format5 = now.strftime("%d-%m-%Y")
print("Date Format-5", format5)

format6 = now.strftime("%B/%d/%Y")
print("Date Format-6", format6)

format7 = now.strftime("%B %dth,%Y")
print("Date Format-7", format7)
 

format8 = now.strftime("%dth %B,%Y")
print("Date Format-8", format8)

format9 = now.strftime("%b-%d-%Y")
print("Date Format-9",format9)

format10 = now.strftime("%d-%b-%Y")
print("Date Format-10", format10)

format11 = now.strftime("%d/%B/%Y")
print("Date Format-11", format11)

format12 = now.strftime("%Y-%m-%d")
print("Date Format-12",format12)


with open('date-time-format.txt','w') as a:
    a.write("Date in different formats\n")
    a.writelines('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'
            .format(format1,format2,format3,format4,format5,format6,format7,
                    format8,format9,format10,format11,format12))
