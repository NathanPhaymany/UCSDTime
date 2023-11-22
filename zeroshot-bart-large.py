from transformers import pipeline

pipe = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

categories = """Lower Division
    Upper Division
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
    Biology/Animal Physiol&Neurosci
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
    Mechanical Engineering
    Aerospace Engineering
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
    
category_list = categories.splitlines()

sequence_to_classify = "mechanical engineering courses"
categorized = pipe(sequence_to_classify, category_list, multi_label=True)
scores = categorized['scores']
ranked = categorized['labels']
tally = 0
while scores[tally] >= 0.50:
    tally += 1

# print(ranked)
# print(ranked)
# print(scores)
kept_ranked = ranked[:tally]
kept_scores = scores[:tally]
print (kept_ranked)
# print (kept_scores)