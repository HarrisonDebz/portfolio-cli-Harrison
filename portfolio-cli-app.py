def show_menu():
    """Display the main menu"""
    print("\n" + "="*40)
    print("         MY PORTFOLIO APP")
    print("="*40)
    print("1. About Me")
    print("2. Skills I Want to Learn")
    print("3. My Projects")
    print("4. My Future Plans")
    print("5. Exit")
    print("="*40)

def show_about():
    """Display My Info"""
    print("\n--- About Me ---")
    print("Hello! I'm Harrison Malisawa, a 2nd year student at The Copperbelt University studying Computer Science. I'm obsessed with coding and technology, and I'm always eager to learn new things and take on exciting projects.")

def show_skills():
    """Display Skills I Want to Learn"""
    print("\n--- Skills I Want To Learn ---")
    skills = [
        "1. CyberSec Basic and Advanced Fundamentals",
        "2. Hackathons & CTF Readiness",
        "3. Top 5 programming languages Mastery",
        "4. Full-stack Development",
        "5. Framework Mastery",
        "6. AI/ML Foundations",
        "7. Product Design & UI/UX Mastery"
    ]
    for skill in skills:
        print(f" • {skill}")

def show_projects():
    """Display My Projects"""
    print("\n--- My Projects ---")
    projects = [
        "1. Portfolio Website.",
        "2. Website Vulnerability Scanner.",
        "3. Recipe App.",
        "4. Client Websites.",
        "5. Graphic Design Projects.",
        "6. EventPulse. (In Development)"
    ]
    for project in projects:
        print(f" • {project}")

def show_future_plan():
    """Display My Future Plans"""
    print("\n--- My Future Plans ---")
    plans = [
        "1. Complete my Computer Science degree.",
        "2. Gain practical experience through internships and projects.",
        "3. Master key programming languages and frameworks.",
        "4. Become a CyberSec Professional.",
        "5. Build networks with professionals in and out of the tech industry.",
        "6. Stay updated with the latest technology trends.",
        "7. Contribute to open-source projects."
    ]
    for plan in plans:
        print(f" • {plan}")

def main():
    """Main program loop"""
    while True:
        try:
            show_menu()
            choice = input("\nSelect an option (1-5): ").strip()
            
            if choice == '1':
                show_about()
            elif choice == '2':
                show_skills()
            elif choice == '3':
                show_projects()
            elif choice == '4':
                show_future_plan()
            elif choice == '5':
                print("Thanks for viewing my portfolio. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a number between 1 and 5.")
        except KeyboardInterrupt:
            print("\nThanks for viewing my portfolio. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()