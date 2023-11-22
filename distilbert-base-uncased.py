from transformers import pipeline

# Set up the pipeline for question answering
pipe = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

# Context for question answering
# context_refinement = ""
context_categories = """
    Below is a catalog of all University of San Diego courses, the code entry is the tag that the department of course has, and the Course  labelled \"Course \" right beneath each code is the formal name of the department.
    Your job is to identify the names of departments within the question prompt and return their names separated by spaces. This most likely will be more than name.
    The input name can be vague, if vague just output any and ALL department names that relate.
    {
        "code": "AIP",
        "Course ": "Academic Internship Program"
    },
    {
        "code": "AAS",
        "Course ": "African American Studies"
    },
    {
        "code": "AWP",
        "Course ": "Analytical Writing Program"
    },
    {
        "code": "ANES",
        "Course ": "Anesthesiology"
    },
    {
        "code": "ANBI",
        "Course ": "Anthro/Biological Anthropology"
    },
    {
        "code": "ANAR",
        "Course ": "Anthropological Archaeology"
    },
    {
        "code": "ANTH",
        "Course ": "Anthropology"
    },
    {
        "code": "ANSC",
        "Course ": "Anthropology/Sociocultural"
    },
    {
        "code": "AESE",
        "Course ": "ArchitectureBsdEntrpSystmsEngr"
    },
    {
        "code": "BENG",
        "Course ": "Bioengineering"
    },
    {
        "code": "BNFO",
        "Course ": "Bioinformatics"
    },
    {
        "code": "BIEB",
        "Course ": "Biol/Ecology, Behavior, & Evol"
    },
    {
        "code": "BICD",
        "Course ": "Biol/Genetics,Cellular&Develop"
    },
    {
        "code": "BIPN",
        "Course ": "Biology/Animal Physiol&Neurosc"
    },
    {
        "code": "BIBC",
        "Course ": "Biology/Biochemistry"
    },
    {
        "code": "BGGN",
        "Course ": "Biology/Grad/General"
    },
    {
        "code": "BGJC",
        "Course ": "Biology/Grad/Journal Club"
    },
    {
        "code": "BGRD",
        "Course ": "Biology/Grad/Research Discussn"
    },
    {
        "code": "BGSE",
        "Course ": "Biology/Grad/Seminar"
    },
    {
        "code": "BILD",
        "Course ": "Biology/Lower Division"
    },
    {
        "code": "BIMM",
        "Course ": "Biology/Molec Biol, Microbiol"
    },
    {
        "code": "BISP",
        "Course ": "Biology/Special Studies"
    },
    {
        "code": "BIOM",
        "Course ": "Biomedical Sciences"
    },
    {
        "code": "CMM",
        "Course ": "Cellular & Molecular Medicine"
    },
    {
        "code": "CENG",
        "Course ": "Chemical Engineering"
    },
    {
        "code": "CHEM",
        "Course ": "Chemistry and Biochemistry"
    },
    {
        "code": "CHIN",
        "Course ": "Chinese Studies"
    },
    {
        "code": "CLAS",
        "Course ": "Classical Studies"
    },
    {
        "code": "CCS",
        "Course ": "Climate Change Studies"
    },
    {
        "code": "CLIN",
        "Course ": "Clinical Psychology"
    },
    {
        "code": "CLRE",
        "Course ": "Clinical Research"
    },
    {
        "code": "COGS",
        "Course ": "Cognitive Science"
    },
    {
        "code": "COMM",
        "Course ": "Communication"
    },
    {
        "code": "COGR",
        "Course ": "Communication/Graduate"
    },
    {
        "code": "CSS",
        "Course ": "Computational Social Science"
    },
    {
        "code": "CSE",
        "Course ": "Computer Science & Engineering"
    },
    {
        "code": "CCE",
        "Course ": "Critical Community Engagement"
    },
    {
        "code": "CGS",
        "Course ": "Critical Gender Studies"
    },
    {
        "code": "CAT",
        "Course ": "Culture, Art, & Technology"
    },
    {
        "code": "TDDM",
        "Course ": "Dance/Dance Making"
    },
    {
        "code": "TDHD",
        "Course ": "Dance/History"
    },
    {
        "code": "TDMV",
        "Course ": "Dance/Movement"
    },
    {
        "code": "TDPF",
        "Course ": "Dance/Performance"
    },
    {
        "code": "TDTR",
        "Course ": "Dance/Theory"
    },
    {
        "code": "DSC",
        "Course ": "Data Science"
    },
    {
        "code": "DSE",
        "Course ": "Data Science and Engineering"
    },
    {
        "code": "DERM",
        "Course ": "Dermatology"
    },
    {
        "code": "DSGN",
        "Course ": "Design"
    },
    {
        "code": "DOC",
        "Course ": "Dimensions of Culture"
    },
    {
        "code": "DDPM",
        "Course ": "Drug Development & Product Mgt"
    },
    {
        "code": "ECON",
        "Course ": "Economics"
    },
    {
        "code": "EDS",
        "Course ": "Education Studies"
    },
    {
        "code": "ERC",
        "Course ": "Eleanor Roosevelt College"
    },
    {
        "code": "ECE",
        "Course ": "Electrical & Computer Engineer"
    },
    {
        "code": "EMED",
        "Course ": "Emergency Medicine"
    },
    {
        "code": "ENG",
        "Course ": "Engineering"
    },
    {
        "code": "ENVR",
        "Course ": "Environmental Studies"
    },
    {
        "code": "ESYS",
        "Course ": "Environmental Systems"
    },
    {
        "code": "ETIM",
        "Course ": "Ethnic St/Interdis Res Methods"
    },
    {
        "code": "ETHN",
        "Course ": "Ethnic Studies"
    },
    {
        "code": "EXPR",
        "Course ": "Exchange Programs"
    },
    {
        "code": "FMPH",
        "Course ": "Family Med & Public Health"
    },
    {
        "code": "FPM",
        "Course ": "Family and Preventive Medicine"
    },
    {
        "code": "FILM",
        "Course ": "Film Studies"
    },
    {
        "code": "GPCO",
        "Course ": "GPS/Core"
    },
    {
        "code": "GPEC",
        "Course ": "GPS/Economics"
    },
    {
        "code": "GPGN",
        "Course ": "GPS/General"
    },
    {
        "code": "GPIM",
        "Course ": "GPS/International Management"
    },
    {
        "code": "GPLA",
        "Course ": "GPS/Language"
    },
    {
        "code": "GPPA",
        "Course ": "GPS/Policy Analytics"
    },
    {
        "code": "GPPS",
        "Course ": "GPS/Political Science"
    },
    {
        "code": "GLBH",
        "Course ": "Global Health"
    },
    {
        "code": "GSS",
        "Course ": "Global South Studies"
    },
    {
        "code": "HITO",
        "Course ": "History Topics"
    },
    {
        "code": "HIAF",
        "Course ": "History of Africa"
    },
    {
        "code": "HIEA",
        "Course ": "History of East Asia"
    },
    {
        "code": "HIEU",
        "Course ": "History of Europe"
    },
    {
        "code": "HILA",
        "Course ": "History of Latin America"
    },
    {
        "code": "HISC",
        "Course ": "History of Science"
    },
    {
        "code": "HINE",
        "Course ": "History of the Near East"
    },
    {
        "code": "HIUS",
        "Course ": "History of the United States"
    },
    {
        "code": "HIGR",
        "Course ": "History, Graduate"
    },
    {
        "code": "HILD",
        "Course ": "History, Lower Division"
    },
    {
        "code": "HDS",
        "Course ": "Human Developmental Sciences"
    },
    {
        "code": "HMNR",
        "Course ": "Human Rights"
    },
    {
        "code": "HUM",
        "Course ": "Humanities"
    },
    {
        "code": "INTL",
        "Course ": "International Studies"
    },
    {
        "code": "JAPN",
        "Course ": "Japanese Studies"
    },
    {
        "code": "JWSP",
        "Course ": "Jewish Studies Program"
    },
    {
        "code": "LATI",
        "Course ": "Latin American Studies"
    },
    {
        "code": "LAWS",
        "Course ": "Law and Society"
    },
    {
        "code": "LISL",
        "Course ": "Linguistics/Amer Sign Language"
    },
    {
        "code": "LIAB",
        "Course ": "Linguistics/Arabic"
    },
    {
        "code": "LIDS",
        "Course ": "Linguistics/Directed Stdy"
    },
    {
        "code": "LIFR",
        "Course ": "Linguistics/French"
    },
    {
        "code": "LIGN",
        "Course ": "Linguistics/General"
    },
    {
        "code": "LIGM",
        "Course ": "Linguistics/German"
    },
    {
        "code": "LIHL",
        "Course ": "Linguistics/Heritage Languages"
    },
    {
        "code": "LIIT",
        "Course ": "Linguistics/Italian"
    },
    {
        "code": "LIPO",
        "Course ": "Linguistics/Portuguese"
    },
    {
        "code": "LISP",
        "Course ": "Linguistics/Spanish"
    },
    {
        "code": "LTAM",
        "Course ": "Literature of the Americas"
    },
    {
        "code": "LTAF",
        "Course ": "Literature/African"
    },
    {
        "code": "LTCO",
        "Course ": "Literature/Comparative"
    },
    {
        "code": "LTCS",
        "Course ": "Literature/Cultural Studies"
    },
    {
        "code": "LTEU",
        "Course ": "Literature/European & Eurasian"
    },
    {
        "code": "LTFR",
        "Course ": "Literature/French"
    },
    {
        "code": "LTGM",
        "Course ": "Literature/German"
    },
    {
        "code": "LTGK",
        "Course ": "Literature/Greek"
    },
    {
        "code": "LTIT",
        "Course ": "Literature/Italian"
    },
    {
        "code": "LTKO",
        "Course ": "Literature/Korean"
    },
    {
        "code": "LTLA",
        "Course ": "Literature/Latin"
    },
    {
        "code": "LTRU",
        "Course ": "Literature/Russian"
    },
    {
        "code": "LTSP",
        "Course ": "Literature/Spanish"
    },
    {
        "code": "LTTH",
        "Course ": "Literature/Theory"
    },
    {
        "code": "LTWR",
        "Course ": "Literature/Writing"
    },
    {
        "code": "LTEN",
        "Course ": "Literatures in English"
    },
    {
        "code": "LTWL",
        "Course ": "Literatures of the World"
    },
    {
        "code": "LTEA",
        "Course ": "Literatures/East Asian"
    },
    {
        "code": "MMW",
        "Course ": "Making of the Modern World"
    },
    {
        "code": "MBC",
        "Course ": "MarineBiodiversity&Conservatn"
    },
    {
        "code": "MATS",
        "Course ": "Materials Sci & Engineering"
    },
    {
        "code": "MATH",
        "Course ": "Mathematics"
    },
    {
        "code": "MSED",
        "Course ": "Mathematics & Science Educ"
    },
    {
        "code": "MAE",
        "Course ": "Mechanical & Aerospace Engin"
    },
    {
        "code": "MED",
        "Course ": "Medicine"
    },
    {
        "code": "MCWP",
        "Course ": "Muir College Writing Program"
    },
    {
        "code": "MUS",
        "Course ": "Music"
    },
    {
        "code": "NANO",
        "Course ": "NanoEngineering"
    },
    {
        "code": "NEU",
        "Course ": "Neurosciences"
    },
    {
        "code": "NEUG",
        "Course ": "Neurosciences/Graduate"
    },
    {
        "code": "OBG",
        "Course ": "Obstetrics and Gynecology"
    },
    {
        "code": "OPTH",
        "Course ": "Ophthalmology"
    },
    {
        "code": "ORTH",
        "Course ": "Orthopaedics"
    },
    {
        "code": "PATH",
        "Course ": "Pathology"
    },
    {
        "code": "PEDS",
        "Course ": "Pediatrics"
    },
    {
        "code": "PHAR",
        "Course ": "Pharmacology"
    },
    {
        "code": "SPPS",
        "Course ": "Pharmacy"
    },
    {
        "code": "PHIL",
        "Course ": "Philosophy"
    },
    {
        "code": "PHYS",
        "Course ": "Physics"
    },
    {
        "code": "PHYA",
        "Course ": "Physics/Astronomy"
    },
    {
        "code": "POLI",
        "Course ": "Political Science"
    },
    {
        "code": "PSY",
        "Course ": "Psychiatry"
    },
    {
        "code": "PSYC",
        "Course ": "Psychology"
    },
    {
        "code": "PH",
        "Course ": "Public Health"
    },
    {
        "code": "RMAS",
        "Course ": "Radiation Med & Applied Sci"
    },
    {
        "code": "RAD",
        "Course ": "Radiology"
    },
    {
        "code": "MGTF",
        "Course ": "Rady Sch of Management Finance"
    },
    {
        "code": "MGT",
        "Course ": "Rady School of Management"
    },
    {
        "code": "MGTA",
        "Course ": "RadySchMgt Business Analytics"
    },
    {
        "code": "MGTP",
        "Course ": "RadySchMgt Profsnl Accountancy"
    },
    {
        "code": "RELI",
        "Course ": "Religion, Study of"
    },
    {
        "code": "RMED",
        "Course ": "Reproductive Medicine"
    },
    {
        "code": "REV",
        "Course ": "Revelle College"
    },
    {
        "code": "SPPH",
        "Course ": "SSPPS/Pharmaceutical Sciences"
    },
    {
        "code": "SOMI",
        "Course ": "Sch of Med Interdisciplinary"
    },
    {
        "code": "SOMC",
        "Course ": "School of Medicine Core Crses"
    },
    {
        "code": "SIOC",
        "Course ": "Scripps Inst of Oceanogr/COAP"
    },
    {
        "code": "SIOG",
        "Course ": "Scripps Inst of Oceanogr/GEO"
    },
    {
        "code": "SIOB",
        "Course ": "Scripps Inst of Oceanogr/OBP"
    },
    {
        "code": "SIO",
        "Course ": "Scripps Inst of Oceanography"
    },
    {
        "code": "SEV",
        "Course ": "Seventh College"
    },
    {
        "code": "SOCG",
        "Course ": "Soc/Graduate"
    },
    {
        "code": "SOCE",
        "Course ": "Soc/Ind Research & Honors Prog"
    },
    {
        "code": "SOCI",
        "Course ": "Sociology"
    },
    {
        "code": "SE",
        "Course ": "Structural Engineering"
    },
    {
        "code": "SURG",
        "Course ": "Surgery"
    },
    {
        "code": "SYN",
        "Course ": "Synthesis"
    },
    {
        "code": "TDAC",
        "Course ": "Theatre / Acting"
    },
    {
        "code": "TDDE",
        "Course ": "Theatre / Design"
    },
    {
        "code": "TDDR",
        "Course ": "Theatre / Directing&Stage Mgmt"
    },
    {
        "code": "TDGE",
        "Course ": "Theatre / General"
    },
    {
        "code": "TDGR",
        "Course ": "Theatre / Graduate"
    },
    {
        "code": "TDHT",
        "Course ": "Theatre / History & Theory"
    },
    {
        "code": "TDPW",
        "Course ": "Theatre / Playwriting"
    },
    {
        "code": "TDPR",
        "Course ": "Theatre Dance/Practicum"
    },
    {
        "code": "USP",
        "Course ": "Urban Studies & Planning"
    },
    {
        "code": "UROL",
        "Course ": "Urology"
    },
    {
        "code": "VIS",
        "Course ": "Visual Arts"
    },
    {
        "code": "WCWP",
        "Course ": "Warren College Writing Program"
    },
    {
        "code": "WES",
        "Course ": "Wireless Embedded Systems"
    }"""
context = """
This is a list of all course names. Can you please tell us which course names would be relevant?
    
Academic Internship Program
African American Studies
Analytical Writing Program
Anesthesiology
Anthro/Biological Anthropology
Anthropological Archaeology
Anthropology
Anthropology/Sociocultural
ArchitectureBsdEntrpSystmsEngr
Bioengineering
Bioinformatics
Biol/Ecology, Behavior, & Evol
Biol/Genetics,Cellular&Develop
Biology/Animal Physiol&Neurosc"
Biology/Biochemistry
Biology/Grad/General
Biology/Grad/Journal Club
Biology/Grad/Research Discussn
Biology/Grad/Seminar
Biology/Lower Division
Biology/Molecular Biology, Microbiology
Biology/Special Studies
Biomedical Sciences
Cellular & Molecular Medicine
Chemical Engineering
Chemistry and Biochemistry
Chinese Studies
Classical Studies
Climate Change Studies
Clinical Psychology
Clinical Research
Cognitive Science
Communication
Communication/Graduate
Computational Social Science
Computer Science & Engineering
Critical Community Engagement
Critical Gender Studies
Culture, Art, & Technology
Dance/Dance Making
Dance/History
Dance/Movement
Dance/Performance
Dance/Theory
Data Science
Data Science and Engineering
Dermatology
Design
Dimensions of Culture
Drug Development & Product Mgt
Economics
Education Studies
Eleanor Roosevelt College
Electrical & Computer Engineer
Emergency Medicine
Engineering
Environmental Studies
Environmental Systems
Ethnic St/Interdis Res Methods
Ethnic Studies
Exchange Programs
Family Med & Public Health
Family and Preventive Medicine
Film Studies
GPS/Core
GPS/Economics
GPS/General
GPS/International Management
GPS/Language
GPS/Policy Analytics
GPS/Political Science
Global Health
Global South Studies
History Topics
History of Africa
History of East Asia
History of Europe
History of Latin America
History of Science
History of the Near East
History of the United States
History, Graduate
History, Lower Division
   Human Developmental Sciences
Human Rights
Humanities
International Studies
Japanese Studies
Jewish Studies Program
Latin American Studies
Law and Society
Linguistics/Amer Sign Language
Linguistics/Arabic
Linguistics/Directed Stdy
Linguistics/French
Linguistics/General
Linguistics/German
Linguistics/Heritage Languages
Linguistics/Italian
Linguistics/Portuguese
Linguistics/Spanish
Literature of the Americas
Literature/African
Literature/Comparative
Literature/Cultural Studies
Literature/European & Eurasian
Literature/French
Literature/German
Literature/Greek
Literature/Italian
Literature/Korean
Literature/Latin
Literature/Russian
Literature/Spanish
Literature/Theory
Literature/Writing
Literatures in English
Literatures of the World
Literatures/East Asian
Making of the Modern World
   MarineBiodiversity&Conservatn
Materials Sci & Engineering
Mathematics
Mathematics & Science Educ
Mechanical & Aerospace Engin
Medicine
Muir College Writing Program
Music
NanoEngineering
Neurosciences
Neurosciences/Graduate
Obstetrics and Gynecology
Ophthalmology
Orthopaedics
Pathology
Pediatrics
Pharmacology
Pharmacy
Philosophy
Physics
Physics/Astronomy
Political Science
Psychiatry
Psychology
Public Health
Radiation Med & Applied Sci
Radiology
Rady Sch of Management Finance
Rady School of Management
RadySchMgt Business Analytics
RadySchMgt Profsnl Accountancy
Religion, Study of
Reproductive Medicine
Revelle College
SSPPS/Pharmaceutical Sciences
Sch of Med Interdisciplinary
School of Medicine Core Crses
Scripps Inst of Oceanogr/COAP
Scripps Inst of Oceanogr/GEO
Scripps Inst of Oceanogr/OBP
Scripps Inst of Oceanography
Seventh College
Soc/Graduate
Soc/Ind Research & Honors Prog
Sociology
Structural Engineering
Surgery
Synthesis
Theatre / Acting
Theatre / Design
Theatre / Directing&Stage Mgmt
Theatre / General
Theatre / Graduate
Theatre / History & Theory
Theatre / Playwriting
Theatre Dance/Practicum
Urban Studies & Planning
Urology
Visual Arts
Warren College Writing Program
Wireless Embedded Systems"""
# Ask a question related to the context


question = "give me all biology names"
prompt_addition = """ Please give us any course names that align with the question."""
total_question = question+prompt_addition
question_refinement_context = ""

# Get the answer using the pipeline
answer = pipe(question=total_question, context=context)

# Print the answer
print(f"Question: {question}")
print(f"Answer: {answer['answer']}")
print(f"Score: {answer['score']}")