"""
================================================================================
            INTELLIGENT FAQ CHATBOT FOR COLLEGE INFORMATION SYSTEM
================================================================================
Project for: M.Sc. / M.Com (Computer Science / Commerce)
Session: 2025-2026
College: T.R.S. College Rewa
University: APS University, Rewa
Student: [Your Name]
Roll No: [Your Roll No.]
Guide: [Guide Name]
================================================================================
"""

# ================================================================================
# SELECT YOUR OPTION
# ================================================================================

# A = 3 Years BCA + 2 Years MSc = 5 Years
# B = 4 Years BCA + 1 Year MSc = 5 Years
# C = 3 Years BCom + 2 Years MCom = 5 Years
# D = 4 Years BCom + 1 Year MCom = 5 Years

EDUCATION_OPTION = "C"  # ← CHANGE: A, B, C, or D

if EDUCATION_OPTION in ["A", "B"]:
    STUDENT_INFO = {
        "name": "[Your Name]",
        "roll_no": "[Your Roll No.]",
        "course_type": "Computer Science",
        "bca_duration": "3 Years" if EDUCATION_OPTION == "A" else "4 Years",
        "bca_complete": "Completed ✓",
        "msc_duration": "2 Years" if EDUCATION_OPTION == "A" else "1 Year",
        "msc_current": "MSc Computer Science",
        "msc_year": "Year 1",  # Change: Year 1 or Year 2
        "session": "2025-2026",
        "college": "T.R.S. College Rewa",
        "university": "APS University, Rewa"
    }
else:  # Option C or D - Commerce
    STUDENT_INFO = {
        "name": "[Your Name]",
        "roll_no": "[Your Roll No.]",
        "course_type": "Commerce",
        "bcom_duration": "3 Years" if EDUCATION_OPTION == "C" else "4 Years",
        "bcom_complete": "Completed ✓",
        "mcom_duration": "2 Years" if EDUCATION_OPTION == "C" else "1 Year",
        "mcom_current": "M.Com",
        "mcom_year": "Year 1",  # Change: Year 1 or Year 2
        "session": "2025-2026",
        "college": "T.R.S. College Rewa",
        "university": "APS University, Rewa"
    }

# ================================================================================
# COMPLETE FAQ DATABASE
# ================================================================================

FAQ_DB = {
    # 1. Student Profile
    "profile": {
        "keywords": ["profile", "my", "me", "student", "about", "details"],
        "question": "My Profile",
        "answer": f"""👤 MY PROFILE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Name        : {STUDENT_INFO['name']}
Roll No.   : {STUDENT_INFO['roll_no']}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ COMPLETED: {STUDENT_INFO.get('bca_complete') or STUDENT_INFO.get('bcom_complete')}
📚 CURRENT: {STUDENT_INFO.get('msc_current') or STUDENT_INFO.get('mcom_current')}

Session   : {STUDENT_INFO['session']}
College   : {STUDENT_INFO['college']}
University: {STUDENT_INFO['university']}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""
    },

    # 2. All Courses
    "all_courses": {
        "keywords": ["all courses", "course list", "available courses", "both"],
        "question": "All Courses",
        "answer": """📚 ALL COURSES OFFERED (2025-2026):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎓 UNDER GRADUATION (UG):
━━━━━━━━━━━━━━━━━━━━━━━━━━━
COMPUTER SCIENCE:
- BCA (3 Years)
- BCA Honors (4 Years)
- BSc Computer Science (3 Years)

COMMERCE:
- BCom (3 Years) - Plain
- BCom Honors (4 Years)

SCIENCE:
- BSc Physics (3 Years)
- BSc Mathematics (3 Years)

ARTS:
- BA (Various subjects)

🎓 POST GRADUATION (PG):
━━━━━━━━━━━━━━━━━━━━━━━━━━━
COMPUTER SCIENCE:
- MSc Computer Science (2 Years)
- MSc (1 Year - Intensive)

COMMERCE:
- MCom (2 Years)
- MCom (1 Year - Intensive)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""
    },

    # 3. BCA Courses
    "bca": {
        "keywords": ["bca", "bachelor computer applications", "bcsc"],
        "question": "BCA Course",
        "answer": """🎓 BCA (Bachelor of Computer Applications):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Duration: 3 Years (6 Semesters)
        4 Years (8 Semesters) - Honors

Eligibility: 12th Pass (Any Stream)

📖 SUBJECTS (3 Years):
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sem 1: C Programming, Math
Sem 2: C++, Digital Electronics
Sem 3: Data Structures, DBMS
Sem 4: Java, Operating Systems
Sem 5: Python, Web Technologies
Sem 6: Project Work

📖 SUBJECTS (4 Years - Honors):
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sem 1-6: Same as above +
Sem 7: Advanced Python, Research
Sem 8: Major Project, Thesis

💻 LABS: C, C++, Java, Python, DBMS"""
    },

    # 4. BSc Courses
    "bsc": {
        "keywords": ["bsc", "bachelor science", "bsc cs", "computer science"],
        "question": "BSc Course",
        "answer": """🎓 BSc COMPUTER SCIENCE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Duration: 3 Years (6 Semesters)

Eligibility: 12th Science (Physics, Math)

📖 SUBJECTS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Year 1: C Programming, Math, Physics
Year 2: Data Structures, DBMS, Java
Year 3: Python, Web Tech, Project

💻 LABS: Computer Lab, Physics Lab"""
    },

    # 5. BCom Courses
    "bcom": {
        "keywords": ["bcom", "bachelor commerce", "commerce"],
        "question": "BCom Course",
        "answer": """🎓 BCOM (Bachelor of Commerce):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Duration: 3 Years (6 Semesters)
        4 Years (8 Semesters) - Honors

Eligibility: 12th Pass (Any Stream)

📖 SUBJECTS (3 Years):
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sem 1-2: Financial Accounting
       Business Mathematics
       Economics

Sem 3-4: Corporate Accounting
       Business Law
       Cost Accounting

Sem 5-6: Income Tax
       Auditing
       Business Finance

📖 SUBJECTS (4 Years - Honors):
━━━━━━━━━━━━━━━━━━━━━━━━━━━
+ Advanced Financial Management
+ International Trade
+ Business Research Methods"""
    },

    # 6. MSc Courses
    "msc": {
        "keywords": ["msc", "master science", "computer", "pg computer"],
        "question": "MSc Course",
        "answer": """🎓 MSC COMPUTER SCIENCE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Duration: 2 Years (4 Semesters)
        1 Year (Intensive)

Eligibility: BCA/BSc in relevant field
            45-50% marks

📖 SUBJECTS (2 Years):
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Year 1: Advanced Data Structures
       Machine Learning
       Python Programming

Year 2: Deep Learning
       Cloud Computing
       Thesis

📖 SUBJECTS (1 Year - Intensive):
━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Accelerated ML
- Research Methods
- Major Project"""
    },

    # 7. MCom Courses
    "mcom": {
        "keywords": ["mcom", "master commerce", "pg commerce"],
        "question": "MCom Course",
        "answer": """🎓 MCOM (Master of Commerce):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Duration: 2 Years (4 Semesters)
        1 Year (Intensive)

Eligibility: BCom with 45-50% marks

📖 SUBJECTS (2 Years):
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Year 1: Advanced Accounting
       Business Research
       Corporate Finance

Year 2: International Trade
       Taxation
       Dissertation

📖 SUBJECTS (1 Year - Intensive):
━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Advanced Financial Management
- Business Research
- Project Work"""
    },

    # 8. College Info
    "college": {
        "keywords": ["college", "trs", "about", "information"],
        "question": "College",
        "answer": """🏛️ T.R.S. COLLEGE, REWA:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📜 Managed by: Tilak Education & Welfare Society

📚 Affiliated to: APS University, Rewa

📍 Location: NH-7, Rewa, MP

🌐 Website: trscollegerewa.org

📚 COURSES OFFERED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━
COMPUTER SCIENCE | COMMERCE | SCIENCE | ARTS
BCA | BCom | BSc | BA
BSc CS | BCom Honors
MSc | MCom | MSc | MA"""
    },

    # 9. Fee Structure - All
    "fee_all": {
        "keywords": ["fee", "fees", "charge", "cost", "all fee"],
        "question": "Fee Structure",
        "answer": """💰 FEE STRUCTURE (2025-2026):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

UNDER GRADUATION:
━━━━━━━━━━━━━━━━━
📚 BCA: ₹20,000 - ₹30,000/yr
📚 BSc CS: ₹15,000 - ₹25,000/yr
📚 BCom: ₹10,000 - ₹20,000/yr
📚 BCom Hons: ₹15,000 - ₹25,000/yr

POST GRADUATION:
━━━━━━━━━━━━━━━━━
📚 MSc (2 yr): ₹25,000 - ₹35,000/yr
📚 MSc (1 yr): ₹35,000 - ₹45,000/yr
📚 MCom (2 yr): ₹15,000 - ₹25,000/yr
📚 MCom (1 yr): ₹25,000 - ₹35,000/yr

Contact for exact fees"""
    },

    # 10. Fee BCA/BSc
    "fee_cs": {
        "keywords": ["fee bca", "fee bsc", "cs fee"],
        "question": "CS Fee",
        "answer": """💰 COMPUTER SCIENCE FEES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 BCA (3 Years): ₹20,000 - ₹30,000/yr
📚 BCA Honors (4 Years): ₹20,000 - ₹30,000/yr
📚 BSc CS: ₹15,000 - ₹25,000/yr
📚 MSc (2 Years): ₹25,000 - ₹35,000/yr
📚 MSc (1 Year): ₹35,000 - ₹45,000/yr"""
    },

    # 11. Fee BCom/MCom
    "fee_commerce": {
        "keywords": ["fee bcom", "fee mcom", "commerce fee"],
        "question": "Commerce Fee",
        "answer": """💰 COMMERCE FEES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 BCom (3 Years): ₹10,000 - ₹20,000/yr
📚 BCom Honors (4 Years): ₹15,000 - ₹25,000/yr
📚 MCom (2 Years): ₹15,000 - ₹25,000/yr
📚 MCom (1 Year): ₹25,000 - ₹35,000/yr"""
    },

    # 12. Eligibility - All
    "eligibility_all": {
        "keywords": ["eligibility", "qualification", "who can apply", "criteria"],
        "question": "Eligibility",
        "answer": """✅ ELIGIBILITY (2025-2026):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

COMPUTER SCIENCE:
━━━━━━━━━━━━━━━
BCA/BSc CS: 12th Pass (Any Stream/Science)
MSc: BCA/BSc with 45-50%

COMMERCE:
━━━━━━━━━━━━━━━
BCom: 12th Pass (Any Stream)
MCom: BCom with 45-50%

Note: Min marks vary by category"""
    },

    # 13. MSc Program
    "msc_program": {
        "keywords": ["msc program", "msc subjects", "computer"],
        "question": "MSc Program",
        "answer": """🎓 MSC COMPUTER SCIENCE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

2 Years Program:
━━━━━━━━━━━━━━━
Year 1: DS, ML, Python, Networks
Year 2: Deep Learning, Cloud, Thesis

1 Year Program (Intensive):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Advanced ML + Research
- Major Project"""
    },

    # 14. MCom Program
    "mcom_program": {
        "keywords": ["mcom program", "mcom subjects", "commerce"],
        "question": "MCom Program",
        "answer": """🎓 MCOM PROGRAM:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

2 Years Program:
━━━━━━━━━━━━━━━
Year 1: Adv. Accounting, Research
Year 2: Intl. Trade, Tax, Thesis

1 Year Program (Intensive):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Advanced Financial Mgmt
- Business Research
- Project"""
    },

    # 15. Thesis
    "thesis": {
        "keywords": ["thesis", "dissertation", "project", "research"],
        "question": "Thesis",
        "answer": """🎓 THESIS: MSc / MCom:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

2 Years: 4th Semester
1 Year: Last 6 months

Requirements:
━━━━━━━━━━━━━━━
- Pages: 200-500
- Original Research
- Viva Voce

Topics (CS): ML, AI, Data Mining
Topics (Commerce): Finance, Tax, Trade"""
    },

    # 16. Contact
    "contact": {
        "keywords": ["contact", "phone", "email", "address"],
        "question": "Contact",
        "answer": """📞 CONTACT T.R.S. COLLEGE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📍 Address: NH-7, Rewa, MP

📞 Phone: [Check Website]

📧 Email: [Check Website]

🌐 Website: trscollegerewa.org

⏰ Hours: Mon-Sat, 10 AM - 5 PM"""
    },

    # 17. Placement
    "placement": {
        "keywords": ["placement", "job", "jobs", "career"],
        "question": "Placement",
        "answer": """💼 PLACEMENT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

COMPUTER SCIENCE:
━━━━━━━━━━━━━━━
BCA/BSc: ₹2-5 LPA
MSc: ₹3-7 LPA

COMMERCE:
━━━━━━━━━━━━━━━
BCom: ₹2-4 LPA
MCom: ₹3-6 LPA

Note: Depends on skills"""
    },

    # 18. Greeting
    "greeting": {
        "keywords": ["hello", "hi", "hey", "namaste"],
        "question": "Greeting",
        "answer": f"""👋 Namaste!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎓 Session: {STUDENT_INFO['session']}
Course Type: {STUDENT_INFO.get('course_type', 'N/A')}

I help with:
📚 All Courses (BCA, BSc, BCom)
🎓 PG (MSc, MCom)
💰 Fee Details
📞 Contact
🎓 Eligibility
📖 Programs

What to know?"""
    },

    # 19. Thanks
    "thanks": {
        "keywords": ["thanks", "thank", "great", "nice"],
        "answer": "😊 Welcome! Press 'bye' to exit."
    },

    # 20. Bye
    "bye": {
        "keywords": ["bye", "goodbye", "exit", "quit"],
        "answer": f"""👋 Thank You!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Student: {STUDENT_INFO['name']}
Course: {STUDENT_INFO.get('course_type', 'All')}

College: {STUDENT_INFO['college']}
University: {STUDENT_INFO['university']}

Goodbye! 🎓"""
    }
}

# ================================================================================
# FUNCTIONS
# ================================================================================

def clean_text(text):
    return text.lower().strip()

def find_answer(user_input):
    text = clean_text(user_input)
    
    best_match = None
    best_score = 0
    
    for category, data in FAQ_DB.items():
        score = 0
        for kw in data["keywords"]:
            if kw in text:
                score += 1
        
        if score > best_score:
            best_score = score
            best_match = category
    
    if best_score > 0:
        return FAQ_DB[best_match]["answer"]
    
    return "Sorry! Ask about:\n• Courses\n• Fees\n• Eligibility\n• Contact\n• Programs"

# ================================================================================
# MAIN
# ================================================================================

def main():
    print("\n" + "="*50)
    print("   🏛️ COLLEGE INFORMATION CHATBOT")
    print("="*50)
    course = STUDENT_INFO.get('course_type', 'All')
    print(f"\n   Option: {EDUCATION_OPTION}")
    print(f"   Student: {STUDENT_INFO['name']}")
    print(f"   Courses: BCA, BSc, BCom, MSc, MCom")
    print("\n   Type 'bye' to exit")
    print("="*50 + "\n")
    
    while True:
        user = input("You: ").strip()
        
        if not user:
            print("Chatbot: Ask something!\n")
            continue
        
        if clean_text(user) in ["bye", "exit", "quit"]:
            print("\nChatbot: " + FAQ_DB["bye"]["answer"])
            break
        
        response = find_answer(user)
        print(f"Chatbot: {response}\n")

if _name_ == "_main_":
    main()
