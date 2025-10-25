"""
Student Information System
A Python script to collect, store, and manage student information.
"""

def get_student_details():
    """
    Prompts user for student details and returns a dictionary.
    
    Returns:
        dict: Dictionary containing student information
    """
    print("\n--- Enter Student Details ---")
    name = input("Enter student name: ").strip()
    student_id = input("Enter student ID: ").strip()
    favorite_ai_tool = input("Enter favorite AI tool: ").strip()
    
    student_dict = {
        'name': name,
        'student_id': student_id,
        'favorite_AI_tool': favorite_ai_tool
    }
    
    return student_dict


def display_students(students_list):
    """
    Displays all students in a neatly formatted manner.
    
    Args:
        students_list (list): List of student dictionaries
    """
    num_students = len(students_list)
    
    print("\n" + "="*60)
    print(f"{'STUDENT INFORMATION SYSTEM':^60}")
    print("="*60)
    print(f"\nTotal Number of Students: {num_students}\n")
    
    if num_students == 0:
        print("No students registered yet.")
        return
    
    for i, student in enumerate(students_list, 1):
        print(f"Student #{i}")
        print(f"  Name:            {student['name']}")
        print(f"  Student ID:      {student['student_id']}")
        print(f"  Favorite AI Tool: {student['favorite_AI_tool']}")
        print("-" * 60)


def save_to_file(students_list, filename='students.txt'):
    """
    Saves the list of students to a text file.
    
    Args:
        students_list (list): List of student dictionaries
        filename (str): Name of the file to save to (default: 'students.txt')
    """
    try:
        with open(filename, 'w') as file:
            file.write("="*60 + "\n")
            file.write(f"{'STUDENT INFORMATION SYSTEM':^60}\n")
            file.write("="*60 + "\n\n")
            file.write(f"Total Number of Students: {len(students_list)}\n\n")
            
            if len(students_list) == 0:
                file.write("No students registered yet.\n")
            else:
                for i, student in enumerate(students_list, 1):
                    file.write(f"Student #{i}\n")
                    file.write(f"  Name:             {student['name']}\n")
                    file.write(f"  Student ID:       {student['student_id']}\n")
                    file.write(f"  Favorite AI Tool: {student['favorite_AI_tool']}\n")
                    file.write("-" * 60 + "\n")
        
        print(f"\n✓ Student data successfully saved to '{filename}'")
    
    except Exception as e:
        print(f"\n✗ Error saving to file: {e}")


def main():
    """
    Main function to run the student information system.
    """
    students = []  # List to store all student dictionaries
    
    print("="*60)
    print(f"{'WELCOME TO STUDENT INFORMATION SYSTEM':^60}")
    print("="*60)
    
    while True:
        print("\n--- MENU ---")
        print("1. Add new student")
        print("2. Display all students")
        print("3. Save to file")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            # Get student details and add to list
            student = get_student_details()
            students.append(student)
            print(f"\n✓ Student '{student['name']}' added successfully!")
        
        elif choice == '2':
            # Display all students
            display_students(students)
        
        elif choice == '3':
            # Save to file
            save_to_file(students)
        
        elif choice == '4':
            # Exit program
            print("\n--- Thank you for using Student Information System! ---")
            
            # Ask if user wants to save before exiting
            if students:
                save_choice = input("Do you want to save data before exiting? (yes/no): ").strip().lower()
                if save_choice in ['yes', 'y']:
                    save_to_file(students)
            
            break
        
        else:
            print("\n✗ Invalid choice! Please enter a number between 1-4.")


if __name__ == "__main__":
    main()