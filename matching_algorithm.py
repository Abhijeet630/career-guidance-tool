def match_careers(user_profile, careers):
    matched_careers = []

    for career in careers:
        if user_profile["education_level"] == career["education_level"]:
            if user_profile["marks"] >= career["required_marks"]:
                if user_profile["stream"] is None or user_profile["stream"] in career["streams"]:
                    matched_skills = set(user_profile["skills"]).intersection(career["skills"])
                    if matched_skills:
                        matched_careers.append({
                            "career": career["career"],
                            "description": career["description"],
                            "average_salary": career["average_salary"],
                            "matched_skills": list(matched_skills)
                        })

    # If no suitable career is found and marks are below 35%, suggest retaking exams
    if not matched_careers and user_profile["marks"] < 35:
        matched_careers.append({
            "career": "Retake Exams",
            "description": "If your marks are below 35%, consider retaking your exams to improve your career prospects.",
            "average_salary": "None (until you pass)",
            "matched_skills": []
        })

    # If still no suitable career and marks are low, suggest basic jobs
    if not matched_careers:
        if user_profile["education_level"] == "10th pass":
            matched_careers.append({
                "career": "Data Entry Operator",
                "description": "Enters data into computer systems, ensuring accuracy and completeness.",
                "average_salary": 25000,
                "matched_skills": ["typing", "attention to detail", "basic computer knowledge"]
            })
            matched_careers.append({
                "career": "Retail Associate",
                "description": "Assists customers in a retail environment, processes sales, and maintains inventory.",
                "average_salary": 25000,
                "matched_skills": ["customer service", "sales", "communication"]
            })
        elif user_profile["education_level"] == "12th pass":
            matched_careers.append({
                "career": "Clerk",
                "description": "Performs administrative tasks such as data entry and managing records.",
                "average_salary": 30000,
                "matched_skills": ["organization", "attention to detail", "basic accounting"]
            })
            matched_careers.append({
                "career": "Technician",
                "description": "Installs and repairs technical equipment and systems.",
                "average_salary": 40000,
                "matched_skills": ["technical knowledge", "problem-solving", "mechanical skills"]
            })
            matched_careers.append({
                "career": "Sales Executive",
                "description": "Promotes and sells products or services to customers.",
                "average_salary": 35000,
                "matched_skills": ["communication", "sales", "customer service"]
            })

    return matched_careers
