members_access = { "Alice": {"room1", "room2", "room3"}, "Bob": {"room2",
"room4"}, "Charlie": {"room1", "room3", "room5"}, "David": {"room3",
"room4", "room5"} }
rooms = {"room1", "room2", "room3", "room4", "room5"}

def main():
  choice = int(input("\n======Main Program======\n[1]Check access to a room\n[2]Unaccessible room(s) for a member\n[3]Add new member\n[4]Exit\nMake a selection: "))
  if choice == 1:
    accessible()
  elif choice == 2:
    not_accessible()
  elif choice == 3:
    new_member()
  elif choice == 4:
    print("See you later!\n=====Brought to you by tibiCoding====\n")
  else:
    print("Wrong input, try again!")
    main()    

def accessible():
  room = input(f"{rooms}\nFor which room of the above list would you like to check the access: ")
  allowed_members = []
  if room:
    for member in members_access.keys():
      if room in members_access.get(member):
        allowed_members.append(member)
      else:
        continue
    if allowed_members !=[]:
      print(f"{room} can be accessed by {allowed_members}.")
    else:
      print(f"{room} does not have any access yet!")
  else:
    print("Wrong input, try again!")
    accessible()
  main()

def not_accessible():
  person = input(f"{members_access.keys()}\nFor which person from the above list would you like to check the access: ")
  if person:
    rooms_accessible = members_access.get(person)
    rooms_inaccessible = rooms - rooms_accessible
    print(f"{person} can not enter {rooms_inaccessible}")
  else:
    print("Wrong input, try again!")
    not_accessible()
  main()

def new_member():
  person = input("What is the name of the new member? ")
  if person:
    rooms_permission = input(f"{rooms}\nWhich rooms can {person} access from the above list?(seperated by comma's) ").split(",")
    if rooms_permission:
      members_access.update({person:rooms_permission})
      print(f"{person} now has access to {rooms_permission}")
    else:
      print("Wrong input, try again!")
  main()


main()