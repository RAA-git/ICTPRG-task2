# Define the available courses and their prerequisites
courses = {
    1: {"name": "Certificate II in IT", "prerequisites": []},
    2: {"name": "Certificate III in IT - Programming", "prerequisites": [1]},
    3: {"name": "Certificate III in IT - Networking", "prerequisites": [1]},
    4: {"name": "Certificate IV in IT - Programming", "prerequisites": [1, 2]},
    5: {"name": "Certificate IV in IT - Networking", "prerequisites": [1, 3]},
    6: {"name": "Diploma in IT", "prerequisites": [1, 4 or 5]},
}
# Function to get the list of completed courses
def get_completed_courses():
    print("Enter the numbers of the courses you have completed (comma-separated), or type 'none':")
    print("1. Certificate II in IT")
    print("2. Certificate III in IT - Programming")
    print("3. Certificate III in IT - Networking")
    print("4. Certificate IV in IT - Programming")
    print("5. Certificate IV in IT - Networking")
    print("6. Diploma in IT")
    
    selected = input().strip().lower()
    
    if selected == "none":
        return []
    
    return [int(course) for course in selected.split(",") if course.isdigit()]

# Function to list available courses based on completed courses
def list_available_courses(completed):
    available = []
    for course_id, course_info in courses.items():
        if course_id not in completed and all(req in completed for req in course_info["prerequisites"]):
            available.append(course_id)
    
    return available

# Main program 
def main():
    completed_courses = get_completed_courses()
    available_courses = list_available_courses(completed_courses)
    
    if not available_courses:
        print("No courses available to enrol in based on your completed courses.")
    else:
        print("You can enroll in the following courses:")
        for course_id in available_courses:
            print(f"{course_id}. {courses[course_id]['name']}")
        
        selected_course = int(input("Enter the course number to enroll: ").strip())
        if selected_course in available_courses:
            print(f"Enrollment confirmed for {courses[selected_course]['name']}.")
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()
