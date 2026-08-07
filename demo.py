name = input("Enter your name, Agent: ")
gadget = input("Enter your favourite gadget, Agent")

agent_number = 10
speed_rating=7.2
mission_count=8
height = 1.89
is_active=True

print("Name:", name ,"->Type",type (name))
print("Gadget:", gadget ,"->Type",type (gadget))
print("Agent Number:", agent_number ,"->Type",type (agent_number))
print("Mission Count:", mission_count ,"->Type",type (mission_count))
print("Height:", height ,"->Type",type (height))
print("Activity status:",is_active ,"->Type",type (is_active))

#Typecasting
agent_number_text= str(agent_number)
speed_rating_text= str(speed_rating)
mission_count_text= str(mission_count)

print("Agent Number:", agent_number_text ,"->Type",type (agent_number_text))
print("Speed rating:", speed_rating_text ,"->Type",type (speed_rating_text))
print("Mission count:", mission_count_text ,"->Type",type (mission_count_text))

first_three= name[0:3]
print("First three letter of name:", first_three)


badge_line1= "AGENT: " + first_three
badge_line2= "ID", agent_number_text  +  "| Mission : " , mission_count_text
print(badge_line1, "\n" ,badge_line2)