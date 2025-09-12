# insert.py

internships = []

domains = [
    "AI/ML", "Web Development", "Cybersecurity", "Cloud & DevOps", "UI/UX Design", "Full Stack",
    "Generative AI", "Data Science & Analytics", "Product Management", "AR/VR Development",
    "Blockchain", "Game Development", "Mobile App Development", "EdTech & Learning Design",
    "Prompt Engineering", "DevRel & Community Building", "Digital Marketing",
    "Content Creation & SEO", "Business Analytics", "Finance & FinTech", "LegalTech"
]

companies = [
    "Microsoft", "Google", "Amazon", "Meta", "TCS", "Infosys", "Cisco", "Eduskills",
    "IBM", "Accenture", "Wipro", "Salesforce", "Adobe", "Zoho", "Deloitte", "Flipkart", "HCL",
    "SAP", "Capgemini"
]

types = ["Remote", "Hybrid", "In-office"]
durations = ["4 Weeks", "6 Weeks", "8 Weeks", "3 Months", "6 Months"]

base_links = {
    "Microsoft": "https://eduskillsfoundation.org/",
    "Google": "https://www.coursera.org/professional-certificates/google-ux-design",
    "Amazon": "https://www.aws.training/Details/Curriculum?id=20685",
    "Meta": "https://www.coursera.org/professional-certificates/meta-front-end-developer",
    "TCS": "https://www.tcs.com/careers/internship",
    "Infosys": "https://www.infosys.com/careers/internships.html",
    "Cisco": "https://www.netacad.com/courses/security",
    "Eduskills": "https://eduskillsfoundation.org/",
    "IBM": "https://www.ibm.com/in-en/careers/internships",
    "Accenture": "https://www.accenture.com/in-en/careers/internships",
    "Wipro": "https://careers.wipro.com/internships",
    "Salesforce": "https://www.salesforce.com/company/careers/university/",
    "Adobe": "https://www.adobe.com/careers/university.html",
    "Zoho": "https://www.zoho.com/careers/internships.html",
    "Deloitte": "https://www2.deloitte.com/in/en/pages/careers/articles/internships.html",
    "Flipkart": "https://www.flipkartcareers.com/internships",
    "HCL": "https://www.hcltech.com/careers/internships",
    "SAP": "https://www.sap.com/about/careers/internships.html",
    "Capgemini": "https://www.capgemini.com/in-en/careers/internships/"
}

skills_by_domain = {
    "AI/ML": ["Python", "TensorFlow", "Scikit-learn"],
    "Web Development": ["HTML", "CSS", "JavaScript"],
    "Cybersecurity": ["Wireshark", "Nmap", "Burp Suite"],
    "Cloud & DevOps": ["AWS", "Docker", "Kubernetes"],
    "UI/UX Design": ["Figma", "Adobe XD", "User Research"],
    "Full Stack": ["React", "Node.js", "MongoDB"],
    "Generative AI": ["LangChain", "OpenAI API", "Prompt Engineering"],
    "Data Science & Analytics": ["Pandas", "SQL", "Power BI"],
    "Product Management": ["Agile", "JIRA", "Roadmapping"],
    "AR/VR Development": ["Unity", "Unreal Engine", "C#"],
    "Blockchain": ["Solidity", "Ethereum", "Smart Contracts"],
    "Game Development": ["C++", "Godot", "Game Physics"],
    "Mobile App Development": ["Flutter", "Kotlin", "Firebase"],
    "EdTech & Learning Design": ["Storyline", "Canva", "Curriculum Design"],
    "Prompt Engineering": ["LLMs", "Few-shot Learning", "Chain-of-Thought"],
    "DevRel & Community Building": ["Discord", "GitHub", "Public Speaking"],
    "Digital Marketing": ["Meta Ads", "Google Analytics", "SEO"],
    "Content Creation & SEO": ["Blogging", "Keyword Research", "Canva"],
    "Business Analytics": ["Excel", "Tableau", "Forecasting"],
    "Finance & FinTech": ["FinTech APIs", "Excel", "Risk Modeling"],
    "LegalTech": ["Contract AI", "Legal Research", "Compliance"]
}

count = 0
for company in companies:
    for domain in domains:
        internships.append({
            "title": f"{domain} Internship",
            "company": company,
            "domain": domain,
            "type": types[count % len(types)],
            "duration": durations[count % len(durations)],
            "link": base_links.get(company, "https://www.example.com"),
            "skills": skills_by_domain.get(domain, ["Communication", "Problem Solving"]),
            "featured": (count % 17 == 0)  # Every 17th internship is featured
        })
        count += 1
