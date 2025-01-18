# Program: Room Access Management

This program is designed to manage and control access to various rooms for different members. It provides an interface for users to perform the following tasks:

1. Check which members have access to a specific room.
2. Identify the rooms that a specific member cannot access.
3. Add a new member along with their room access permissions.

## Features
User-Friendly Interface: The program uses a text-based menu system to guide users through different functionalities.
Dynamic Member Management: Users can easily add new members and assign them room permissions.
Access Control Queries: Users can check which members have access to specific rooms or determine restricted rooms for a particular member.

## Techniques Used
1. Data Structures
    Dictionary:
    The members_access dictionary maps member names to the set of rooms they can access.
    Set:
    The rooms variable is a set containing all rooms. This allows efficient membership checks and set operations like difference.

2. Input Validation
    User inputs are validated to ensure correctness before performing operations. For example:
    Ensuring the room name or member name is valid.
    Handling cases where inputs are empty or invalid.

3. Functional Programming
    The program is modular, with distinct functions for each operation:
        accessible(): Checks which members can access a specific room.
        not_accessible(): Lists rooms a member cannot access.
        new_member(): Adds a new member and their permissions.

4. Recursive Function Calls
    The program uses recursion to restart a function if the user input is invalid, ensuring a smooth user experience.

5. Dynamic Dictionary Updates
    The program allows for adding new members dynamically by updating the members_access dictionary.

6. Set Operations
The program uses set operations to compute differences between accessible and total rooms.

## How to Use
Run the Program: Execute the script in a Python environment.
Choose an Option:
[1] Check which members have access to a specific room.
[2] Identify rooms a member cannot access.
[3] Add a new member and assign their room permissions.
[4] Exit the program.
Follow Prompts: Input the required information when prompted.
Repeat: After completing an operation, the menu will reappear for additional actions.
Example Scenarios
Checking Room Access:

Input: room2
Output: "room2 can be accessed by ['Alice', 'Bob']."
Finding Inaccessible Rooms:

Input: Charlie
Output: "Charlie cannot enter {'room2', 'room4'}"
Adding a New Member:

Input:
Member Name: Eve
Accessible Rooms: room3,room4
Output: "Eve now has access to ['room3', 'room4']"

## Future Improvements
Add persistent storage to save member data between program runs.
Implement a graphical user interface (GUI) for a more interactive experience.
Provide error messages for invalid room names or members more explicitly.