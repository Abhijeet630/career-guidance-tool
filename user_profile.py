def get_user_profile():
    name = input("Enter your name: ")
    education_level = input("Enter your highest level of education (10th pass/12th pass/graduate): ").lower()
    if education_level not in ["10th pass", "12th pass", "graduate"]:
        print("Invalid education level.")
        return None
    
    marks = int(input("Enter your marks percentage: "))
    stream = None
    if education_level in ["12th pass", "graduate"]:
        stream = input("Enter your stream (Science/Commerce/Arts): ").capitalize()
    
    skills = input("Enter your skills (comma separated): ").split(',')
    interests = input("Enter your interests (comma separated): ").split(',')
    
    user_profile = {
        "name": name,
        "education_level": education_level,
        "marks": marks,
        "stream": stream,
        "skills": [skill.strip().lower() for skill in skills],
        "interests": [interest.strip().lower() for interest in interests],
    }
    
    return user_profile
