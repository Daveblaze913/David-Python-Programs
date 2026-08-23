name = input("Enter your name, : ")
gender = input("Enter your gender, : ")

Age = 10
is_active=True

print("Name:", name ,"->Type",type (name))
print("Gender:", gender ,"->Type",type (gender))
print("Age:", Age ,"->Type",type (Age))
print("Activity status:",is_active ,"->Type",type (is_active))

#Typecasting
Age_text = str(Age)

print("Age:", Age ,"->Type",type (Age_text))

first_three= name[0:3]
print("First three letter of name:", first_three)


badge_line1= "AGENT: " + first_three
badge_line2= "ID", Age_text  +  "| Mission : " , name
print(badge_line1, "\n" ,badge_line2)