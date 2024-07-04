from career_data import load_career_data
from user_profile import get_user_profile
from matching_algorithm import match_careers

def provide_recommendations(matched_careers):
    if not matched_careers:
        print("Sorry, no careers matched your profile.")
        return

    print("Here are some career recommendations for you:")
    for career in matched_careers:
        print(f"\nCareer: {career['career']}")
        print(f"Description: {career['description']}")
        print(f"Average Salary: ${career['average_salary']}")
        if career['matched_skills']:
            print(f"Matched Skills: {', '.join(career['matched_skills'])}")

def main():
    careers = load_career_data()
    user_profile = get_user_profile()
    if user_profile:
        matched_careers = match_careers(user_profile, careers)
        provide_recommendations(matched_careers)

if __name__ == "__main__":
    main()
