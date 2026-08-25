from django.core.management.base import BaseCommand
from jobportal.models import Exam, MockTestQuestion


# ============================================================
# QUESTION FORMAT
# ============================================================

def q(
    subject,
    question,
    option1,
    option2,
    option3,
    option4,
    answer,
    difficulty="Medium",
):
    return {
        "subject": subject,
        "question": question,
        "option1": option1,
        "option2": option2,
        "option3": option3,
        "option4": option4,
        "answer": answer,
        "difficulty": difficulty,
    }


# ============================================================
# AIR FORCE
# 50 questions
# ============================================================

AIR_FORCE = [

    q(
        "Indian Air Force",
        "When was the Indian Air Force established?",
        "1930",
        "1932",
        "1940",
        "1947",
        "1932",
    ),

    q(
        "Indian Air Force",
        "What is the motto of the Indian Air Force?",
        "Service Before Self",
        "Touch the Sky with Glory",
        "Victory Through Courage",
        "Nation First",
        "Touch the Sky with Glory",
    ),

    q(
        "Indian Air Force",
        "Where is the headquarters of the Indian Air Force located?",
        "Mumbai",
        "New Delhi",
        "Bengaluru",
        "Hyderabad",
        "New Delhi",
    ),

    q(
        "Indian Air Force",
        "Which aircraft is manufactured by Hindustan Aeronautics Limited as an indigenous fighter?",
        "Tejas",
        "MiG-21",
        "Mirage 2000",
        "Rafale",
        "Tejas",
    ),

    q(
        "Aviation",
        "What does IAF stand for?",
        "Indian Aviation Force",
        "Indian Air Force",
        "Indian Armed Force",
        "International Air Force",
        "Indian Air Force",
    ),

    q(
        "Aviation",
        "Which force provides air defence to India?",
        "Indian Navy",
        "Indian Air Force",
        "Border Security Force",
        "Coast Guard",
        "Indian Air Force",
    ),

    q(
        "Aviation",
        "What is the primary function of a fighter aircraft?",
        "Transport cargo",
        "Air combat",
        "Fire fighting",
        "Medical evacuation",
        "Air combat",
    ),

    q(
        "Aviation",
        "Which force is responsible for controlling India's airspace from a military perspective?",
        "Indian Army",
        "Indian Navy",
        "Indian Air Force",
        "BSF",
        "Indian Air Force",
    ),

    q(
        "Defence",
        "Which organization develops many indigenous defence aircraft in India?",
        "HAL",
        "ISRO",
        "DRDO",
        "SEBI",
        "HAL",
    ),

    q(
        "Defence",
        "What does DRDO stand for?",
        "Defence Research and Development Organisation",
        "Department of Research and Defence Operations",
        "Defence Railway Development Organisation",
        "Department of Research Development Office",
        "Defence Research and Development Organisation",
    ),

    q(
        "Aviation",
        "Which instrument is used to measure altitude?",
        "Barometer",
        "Altimeter",
        "Thermometer",
        "Ammeter",
        "Altimeter",
    ),

    q(
        "Aviation",
        "Which instrument indicates an aircraft's speed relative to surrounding air?",
        "Altimeter",
        "Airspeed indicator",
        "Compass",
        "Barometer",
        "Airspeed indicator",
    ),

    q(
        "Aviation",
        "What force keeps an aircraft flying upward against gravity?",
        "Drag",
        "Lift",
        "Weight",
        "Friction",
        "Lift",
    ),

    q(
        "Aviation",
        "Which force opposes the forward movement of an aircraft?",
        "Lift",
        "Drag",
        "Thrust",
        "Gravity",
        "Drag",
    ),

    q(
        "Aviation",
        "Which force propels an aircraft forward?",
        "Weight",
        "Lift",
        "Thrust",
        "Drag",
        "Thrust",
    ),

    q(
        "Aviation",
        "Which control surface primarily controls aircraft roll?",
        "Rudder",
        "Aileron",
        "Elevator",
        "Flap",
        "Aileron",
    ),

    q(
        "Aviation",
        "Which control surface controls aircraft yaw?",
        "Aileron",
        "Elevator",
        "Rudder",
        "Flap",
        "Rudder",
    ),

    q(
        "Aviation",
        "Which control surface controls pitch?",
        "Rudder",
        "Elevator",
        "Aileron",
        "Spoiler",
        "Elevator",
    ),

    q(
        "Aviation",
        "What is the purpose of aircraft flaps?",
        "Increase lift during take-off and landing",
        "Reduce fuel completely",
        "Control radio communication",
        "Measure altitude",
        "Increase lift during take-off and landing",
    ),

    q(
        "Aviation",
        "What does Mach number represent?",
        "Aircraft weight",
        "Speed relative to speed of sound",
        "Fuel quantity",
        "Altitude only",
        "Speed relative to speed of sound",
    ),

    q(
        "Defence",
        "Which missile is an air-to-air missile developed in India?",
        "Akash",
        "Astra",
        "Prithvi",
        "Agni",
        "Astra",
    ),

    q(
        "Defence",
        "Akash is primarily what type of missile?",
        "Surface-to-air missile",
        "Air-to-air missile",
        "Anti-tank missile",
        "Ballistic missile",
        "Surface-to-air missile",
    ),

    q(
        "Defence",
        "Which organization is primarily responsible for defence research in India?",
        "DRDO",
        "RBI",
        "ISRO",
        "UIDAI",
        "DRDO",
    ),

    q(
        "Defence",
        "Which of these is an Indian fighter aircraft?",
        "Tejas",
        "C-17",
        "C-130J",
        "CH-47",
        "Tejas",
    ),

    q(
        "Defence",
        "Which aircraft is primarily used for strategic airlift?",
        "C-17 Globemaster III",
        "Tejas",
        "MiG-21",
        "Apache",
        "C-17 Globemaster III",
    ),

    q(
        "Defence",
        "Which aircraft is a transport aircraft used by the Indian Air Force?",
        "C-130J Super Hercules",
        "Tejas",
        "Astra",
        "Akash",
        "C-130J Super Hercules",
    ),

    q(
        "Defence",
        "Which helicopter is operated by the Indian Air Force?",
        "Apache",
        "Tejas",
        "Rafale",
        "MiG-21",
        "Apache",
    ),

    q(
        "General Awareness",
        "The Indian Air Force is one of the three major wings of which organization?",
        "Indian Armed Forces",
        "United Nations",
        "Election Commission",
        "Central Reserve Police",
        "Indian Armed Forces",
    ),

    q(
        "General Awareness",
        "Which day is observed as Indian Air Force Day?",
        "15 August",
        "8 October",
        "26 January",
        "4 December",
        "8 October",
    ),

    q(
        "Defence",
        "What is the highest rank in the Indian Air Force?",
        "Air Marshal",
        "Air Chief Marshal",
        "Air Vice Marshal",
        "Group Captain",
        "Air Chief Marshal",
    ),

    q(
        "Defence",
        "Who is the professional head of the Indian Air Force?",
        "Chief of the Air Staff",
        "Chief of the Army Staff",
        "Chief of Naval Staff",
        "Defence Secretary",
        "Chief of the Air Staff",
    ),

    q(
        "Aviation",
        "What is aviation primarily concerned with?",
        "Aircraft and flight",
        "Ship building",
        "Railway transport",
        "Road construction",
        "Aircraft and flight",
    ),

    q(
        "Aviation",
        "What is the purpose of an aircraft radar?",
        "Detect and track objects",
        "Measure fuel only",
        "Increase engine temperature",
        "Control landing gear",
        "Detect and track objects",
    ),

    q(
        "Aviation",
        "What does GPS help an aircraft determine?",
        "Position and navigation",
        "Engine temperature only",
        "Fuel composition",
        "Wing pressure",
        "Position and navigation",
    ),

    q(
        "Aviation",
        "What is turbulence?",
        "Irregular movement of air",
        "Failure of an engine",
        "Aircraft fuel leakage",
        "Radio communication",
        "Irregular movement of air",
    ),

    q(
        "Aviation",
        "What is a runway primarily used for?",
        "Aircraft take-off and landing",
        "Aircraft manufacturing",
        "Fuel production",
        "Radar testing",
        "Aircraft take-off and landing",
    ),

    q(
        "Defence",
        "Which of the following is a surface-to-air missile system of India?",
        "Akash",
        "Astra",
        "BrahMos",
        "Nag",
        "Akash",
    ),

    q(
        "Defence",
        "BrahMos is primarily what type of missile?",
        "Supersonic cruise missile",
        "Air-to-air missile",
        "Anti-tank missile",
        "Surface-to-air missile",
        "Supersonic cruise missile",
    ),

    q(
        "Defence",
        "Which Indian organization is involved in development of military technology?",
        "DRDO",
        "NITI Aayog",
        "SEBI",
        "UGC",
        "DRDO",
    ),

    q(
        "General Awareness",
        "Which ministry is responsible for India's defence administration?",
        "Ministry of Defence",
        "Ministry of Home Affairs",
        "Ministry of Finance",
        "Ministry of External Affairs",
        "Ministry of Defence",
    ),

    q(
        "Aviation",
        "What is the cockpit of an aircraft?",
        "Area from which the aircraft is controlled",
        "Aircraft engine",
        "Fuel tank",
        "Landing gear",
        "Area from which the aircraft is controlled",
    ),

    q(
        "Aviation",
        "Which fuel is commonly used by jet aircraft?",
        "Petrol",
        "Jet fuel",
        "Diesel",
        "Kerosene oil only",
        "Jet fuel",
    ),

    q(
        "Aviation",
        "What is an aircraft hangar?",
        "Building used for aircraft storage and maintenance",
        "Runway",
        "Control tower",
        "Fuel pipeline",
        "Building used for aircraft storage and maintenance",
    ),

    q(
        "Aviation",
        "What is the function of an aircraft engine?",
        "Produce thrust",
        "Measure altitude",
        "Control radio",
        "Measure air pressure",
        "Produce thrust",
    ),

    q(
        "Defence",
        "Which of these is a transport aircraft?",
        "C-17 Globemaster III",
        "Tejas",
        "Astra",
        "Akash",
        "C-17 Globemaster III",
    ),

    q(
        "Defence",
        "Which aircraft is associated with India's Light Combat Aircraft programme?",
        "Tejas",
        "C-17",
        "C-130J",
        "Apache",
        "Tejas",
    ),

    q(
        "General Awareness",
        "The Indian Air Force operates under which branch of government?",
        "Ministry of Defence",
        "Ministry of Railways",
        "Ministry of Finance",
        "Ministry of Education",
        "Ministry of Defence",
    ),

    q(
        "Aviation",
        "What is the purpose of an aircraft control tower?",
        "Manage aircraft movement around an airport",
        "Manufacture aircraft",
        "Store ammunition only",
        "Repair engines only",
        "Manage aircraft movement around an airport",
    ),

    q(
        "Defence",
        "Which of the following is an important component of India's air defence?",
        "Air surveillance and missile systems",
        "Railway stations",
        "Agricultural markets",
        "Postal networks",
        "Air surveillance and missile systems",
    ),

    q(
        "Aviation",
        "Which branch of science deals with the motion of air and aircraft?",
        "Aerodynamics",
        "Geology",
        "Botany",
        "Zoology",
        "Aerodynamics",
    ),

    q(
        "Defence",
        "Which of the following is a major role of the Indian Air Force?",
        "Air defence and aerial operations",
        "Railway construction",
        "Bank regulation",
        "Forest administration",
        "Air defence and aerial operations",
    ),
]


# ============================================================
# ARMY
# 50 questions
# ============================================================

ARMY = [

    q(
        "Indian Army",
        "What is the motto of the Indian Army?",
        "Touch the Sky with Glory",
        "Service Before Self",
        "Truth Alone Triumphs",
        "Victory or Death",
        "Service Before Self",
    ),

    q(
        "Indian Army",
        "When is Indian Army Day observed?",
        "15 January",
        "26 January",
        "15 August",
        "4 December",
        "15 January",
    ),

    q(
        "Indian Army",
        "Who is the professional head of the Indian Army?",
        "Chief of the Army Staff",
        "Chief of the Air Staff",
        "Chief of Naval Staff",
        "Defence Secretary",
        "Chief of the Army Staff",
    ),

    q(
        "Indian Army",
        "Which is one of the three major services of India's Armed Forces?",
        "Indian Army",
        "Railway Protection Force",
        "Border Roads Organisation",
        "Central Bureau of Investigation",
        "Indian Army",
    ),

    q(
        "Defence",
        "What is the primary role of the Indian Army?",
        "Land-based defence",
        "Air traffic control",
        "Bank regulation",
        "Forest conservation",
        "Land-based defence",
    ),

    q(
        "Defence",
        "Which organization develops defence technologies in India?",
        "DRDO",
        "RBI",
        "ISRO",
        "SEBI",
        "DRDO",
    ),

    q(
        "Defence",
        "What does DRDO stand for?",
        "Defence Research and Development Organisation",
        "Department of Railway Development Organisation",
        "Defence Recruitment Development Office",
        "Department of Research and Defence Operations",
        "Defence Research and Development Organisation",
    ),

    q(
        "Defence",
        "Which of the following is an Indian main battle tank?",
        "Arjun",
        "Tejas",
        "Akash",
        "Astra",
        "Arjun",
    ),

    q(
        "Defence",
        "Which missile is known as an anti-tank guided missile developed in India?",
        "Nag",
        "Akash",
        "Astra",
        "Agni",
        "Nag",
    ),

    q(
        "Defence",
        "Which missile system is designed primarily for air defence?",
        "Akash",
        "Nag",
        "Prithvi",
        "Dhanush",
        "Akash",
    ),

    q(
        "General Awareness",
        "Which ministry administers the Indian Army?",
        "Ministry of Defence",
        "Ministry of Home Affairs",
        "Ministry of Finance",
        "Ministry of External Affairs",
        "Ministry of Defence",
    ),

    q(
        "Military",
        "What is a battalion?",
        "A military formation",
        "A type of aircraft",
        "A naval vessel",
        "A missile",
        "A military formation",
    ),

    q(
        "Military",
        "What is a regiment in the Army?",
        "An organized military unit or tradition-based formation",
        "A type of aircraft",
        "A military vehicle only",
        "A communication device",
        "An organized military unit or tradition-based formation",
    ),

    q(
        "Military",
        "Which terrain is characterized by very high mountains?",
        "Mountain terrain",
        "Desert terrain",
        "Coastal terrain",
        "Plain terrain",
        "Mountain terrain",
    ),

    q(
        "Military",
        "Why is high-altitude training important for soldiers?",
        "To adapt to low oxygen and harsh conditions",
        "To learn banking",
        "To operate trains",
        "To study agriculture",
        "To adapt to low oxygen and harsh conditions",
    ),

    q(
        "Defence",
        "What is a ballistic missile?",
        "A missile that follows a ballistic trajectory for much of its flight",
        "A naval ship",
        "A fighter aircraft",
        "A radar antenna",
        "A missile that follows a ballistic trajectory for much of its flight",
    ),

    q(
        "Defence",
        "Agni missiles belong primarily to which category?",
        "Ballistic missiles",
        "Anti-tank missiles",
        "Air-to-air missiles",
        "Surface-to-air missiles",
        "Ballistic missiles",
    ),

    q(
        "Defence",
        "Which organization is responsible for India's defence research?",
        "DRDO",
        "UGC",
        "RBI",
        "NITI Aayog",
        "DRDO",
    ),

    q(
        "Military",
        "What is camouflage used for?",
        "Concealing personnel or equipment",
        "Increasing fuel consumption",
        "Improving radio signals",
        "Measuring temperature",
        "Concealing personnel or equipment",
    ),

    q(
        "Military",
        "What is reconnaissance?",
        "Collection of information about an area or enemy",
        "Medical treatment",
        "Food preparation",
        "Vehicle manufacturing",
        "Collection of information about an area or enemy",
    ),

    q(
        "Military",
        "What is a military convoy?",
        "A group of vehicles travelling together",
        "A type of missile",
        "A naval rank",
        "A military uniform",
        "A group of vehicles travelling together",
    ),

    q(
        "Military",
        "What is field communication used for?",
        "Exchange of information during operations",
        "Cooking food",
        "Repairing roads",
        "Measuring rainfall",
        "Exchange of information during operations",
    ),

    q(
        "General Awareness",
        "Which day is observed as Republic Day in India?",
        "26 January",
        "15 August",
        "2 October",
        "14 November",
        "26 January",
    ),

    q(
        "General Awareness",
        "Who is the Supreme Commander of the Indian Armed Forces?",
        "President of India",
        "Prime Minister",
        "Defence Minister",
        "Chief of Defence Staff",
        "President of India",
    ),

    q(
        "Defence",
        "What is the role of the Chief of Defence Staff?",
        "Promote jointness among the armed forces",
        "Control the RBI",
        "Manage railways",
        "Administer forests",
        "Promote jointness among the armed forces",
    ),

    q(
        "Military",
        "Which of the following is essential for military discipline?",
        "Obedience to lawful orders",
        "Ignoring orders",
        "Avoiding training",
        "Working without coordination",
        "Obedience to lawful orders",
    ),

    q(
        "Military",
        "What is a military drill?",
        "Systematic training in movements and procedures",
        "A type of missile",
        "A medical operation",
        "A railway operation",
        "Systematic training in movements and procedures",
    ),

    q(
        "Military",
        "Why is physical fitness important for soldiers?",
        "It supports endurance and operational readiness",
        "It replaces military training",
        "It controls weather",
        "It increases weapon range",
        "It supports endurance and operational readiness",
    ),

    q(
        "Defence",
        "Which vehicle is designed for protected movement of troops?",
        "Armoured personnel carrier",
        "Passenger train",
        "Civilian bus",
        "Cargo ship",
        "Armoured personnel carrier",
    ),

    q(
        "Defence",
        "What is an armoured vehicle?",
        "A vehicle protected by armour",
        "An aircraft without wings",
        "A naval vessel",
        "A railway coach",
        "A vehicle protected by armour",
    ),

    q(
        "Military",
        "What does logistics in military operations mainly involve?",
        "Supply and movement of resources",
        "Only weapon firing",
        "Only physical exercise",
        "Only communication",
        "Supply and movement of resources",
    ),

    q(
        "Military",
        "What is military strategy?",
        "Planning and directing operations to achieve objectives",
        "Repairing vehicles",
        "Cooking meals",
        "Operating banks",
        "Planning and directing operations to achieve objectives",
    ),

    q(
        "Military",
        "What is military tactics?",
        "Methods used to conduct operations and engagements",
        "Banking procedures",
        "Forest surveys",
        "Railway signalling",
        "Methods used to conduct operations and engagements",
    ),

    q(
        "Defence",
        "Which of these is an Indian indigenous battle tank?",
        "Arjun",
        "Tejas",
        "Astra",
        "Akash",
        "Arjun",
    ),

    q(
        "Defence",
        "Which missile is associated with India's anti-tank missile programme?",
        "Nag",
        "Agni",
        "Astra",
        "Akash",
        "Nag",
    ),

    q(
        "Military",
        "What is a border area?",
        "Area near an international boundary",
        "Area inside an airport",
        "Area around a bank",
        "Area inside a railway station",
        "Area near an international boundary",
    ),

    q(
        "Military",
        "What is surveillance?",
        "Continuous observation or monitoring",
        "Weapon manufacturing",
        "Food distribution",
        "Road construction",
        "Continuous observation or monitoring",
    ),

    q(
        "Defence",
        "What is the purpose of bulletproof protection?",
        "Reduce the risk from projectiles",
        "Increase vehicle speed",
        "Improve radio signals",
        "Increase fuel capacity",
        "Reduce the risk from projectiles",
    ),

    q(
        "Military",
        "What is a military map used for?",
        "Navigation and operational planning",
        "Bank accounting",
        "School teaching",
        "Medical diagnosis",
        "Navigation and operational planning",
    ),

    q(
        "Military",
        "What is navigation?",
        "Determining position and route",
        "Repairing weapons",
        "Training animals",
        "Managing salaries",
        "Determining position and route",
    ),

    q(
        "Defence",
        "What does national security primarily concern?",
        "Protection of the nation and its interests",
        "Only economic taxation",
        "Only railway development",
        "Only agriculture",
        "Protection of the nation and its interests",
    ),

    q(
        "Military",
        "Why are communication systems important during military operations?",
        "They enable coordination and information exchange",
        "They replace weapons",
        "They provide food",
        "They control rainfall",
        "They enable coordination and information exchange",
    ),

    q(
        "Military",
        "What is a command structure?",
        "System defining authority and responsibility",
        "A type of weapon",
        "A railway signal",
        "A medical instrument",
        "System defining authority and responsibility",
    ),

    q(
        "Military",
        "What is leadership important for in the Army?",
        "Guiding personnel and making decisions",
        "Operating banks",
        "Writing software only",
        "Managing forests only",
        "Guiding personnel and making decisions",
    ),

    q(
        "General Awareness",
        "Which national event is celebrated on 15 August?",
        "Independence Day",
        "Republic Day",
        "Gandhi Jayanti",
        "Army Day",
        "Independence Day",
    ),

    q(
        "General Awareness",
        "Who was India's first Field Marshal?",
        "Sam Manekshaw",
        "Rajendra Prasad",
        "Jawaharlal Nehru",
        "Sardar Patel",
        "Sam Manekshaw",
    ),

    q(
        "Military",
        "What is the main purpose of military training?",
        "Prepare personnel for operational duties",
        "Teach banking",
        "Operate commercial airlines",
        "Manage hospitals",
        "Prepare personnel for operational duties",
    ),

    q(
        "Defence",
        "Which of the following is a defence research organization in India?",
        "DRDO",
        "RBI",
        "IRDAI",
        "SEBI",
        "DRDO",
    ),

    q(
        "Military",
        "What is operational readiness?",
        "Preparedness to perform assigned duties",
        "Annual financial accounting",
        "School examination preparation",
        "Railway ticket booking",
        "Preparedness to perform assigned duties",
    ),

    q(
        "Military",
        "What is the purpose of an army training exercise?",
        "Improve operational skills and coordination",
        "Increase taxation",
        "Operate banks",
        "Conduct elections",
        "Improve operational skills and coordination",
    ),

    q(
        "Defence",
        "Which organization is responsible for development of many Indian military technologies?",
        "DRDO",
        "ISRO",
        "RBI",
        "UGC",
        "DRDO",
    ),
]

BANKING_QUESTIONS = [

    q(
        "Banking",
        "What does RBI stand for?",
        "Reserve Bank of India",
        "Rural Bank of India",
        "Reserve Banking Institution",
        "Regional Bank of India",
        "Reserve Bank of India",
    ),

    q(
        "Banking",
        "Where is the headquarters of the Reserve Bank of India?",
        "New Delhi",
        "Mumbai",
        "Chennai",
        "Kolkata",
        "Mumbai",
    ),

    q(
        "Banking",
        "Which institution is the central bank of India?",
        "SBI",
        "RBI",
        "SEBI",
        "NABARD",
        "RBI",
    ),

    q(
        "Banking",
        "What is the full form of NEFT?",
        "National Electronic Funds Transfer",
        "National Exchange Fund Transfer",
        "New Electronic Financial Transaction",
        "National Economic Fund Transfer",
        "National Electronic Funds Transfer",
    ),

    q(
        "Banking",
        "What is the full form of RTGS?",
        "Real Time Gross Settlement",
        "Rapid Transfer Government System",
        "Real Transfer General Service",
        "Reserve Transaction Gross System",
        "Real Time Gross Settlement",
    ),

    q(
        "Banking",
        "What is the full form of KYC?",
        "Know Your Customer",
        "Keep Your Cash",
        "Know Your Credit",
        "Keep Your Customer",
        "Know Your Customer",
    ),

    q(
        "Banking",
        "Which institution regulates the securities market in India?",
        "RBI",
        "SEBI",
        "IRDAI",
        "PFRDA",
        "SEBI",
    ),

    q(
        "Banking",
        "Which institution regulates insurance in India?",
        "SEBI",
        "RBI",
        "IRDAI",
        "NABARD",
        "IRDAI",
    ),

    q(
        "Banking",
        "What is a bank deposit that generally earns interest and can be withdrawn subject to conditions?",
        "Deposit account",
        "Share account",
        "Tax account",
        "Bond account",
        "Deposit account",
    ),

    q(
        "Banking",
        "What is inflation?",
        "General rise in prices",
        "General fall in prices",
        "Rise in exports only",
        "Fall in employment only",
        "General rise in prices",
    ),

    q(
        "Banking",
        "Which institution is known as India's development bank for agriculture and rural development?",
        "NABARD",
        "SEBI",
        "IRDAI",
        "SIDBI",
        "NABARD",
    ),

    q(
        "Banking",
        "What does ATM stand for?",
        "Automated Teller Machine",
        "Automatic Transfer Machine",
        "Account Transfer Method",
        "Automated Transaction Method",
        "Automated Teller Machine",
    ),

    q(
        "Banking",
        "What is a cheque?",
        "A written order to a bank to pay money",
        "A tax receipt",
        "A loan agreement",
        "A share certificate",
        "A written order to a bank to pay money",
    ),

    q(
        "Banking",
        "What is the main function of a commercial bank?",
        "Accept deposits and provide loans",
        "Print currency",
        "Conduct elections",
        "Make laws",
        "Accept deposits and provide loans",
    ),

    q(
        "Banking",
        "What is a loan?",
        "Money borrowed and repayable",
        "Free government grant",
        "Bank profit",
        "Tax refund",
        "Money borrowed and repayable",
    ),

    q(
        "Banking",
        "What does EMI stand for?",
        "Equated Monthly Instalment",
        "Electronic Money Index",
        "Equal Market Investment",
        "Economic Monthly Income",
        "Equated Monthly Instalment",
    ),

    q(
        "Banking",
        "Which digital payment system is operated by NPCI?",
        "UPI",
        "FTP",
        "HTTP",
        "SMTP",
        "UPI",
    ),

    q(
        "Banking",
        "What does UPI stand for?",
        "Unified Payments Interface",
        "Universal Payment Institution",
        "United Payment India",
        "Unified Banking Interface",
        "Unified Payments Interface",
    ),

    q(
        "Banking",
        "What is a non-performing asset generally associated with?",
        "Loan repayment problems",
        "Currency printing",
        "Stock exchange listing",
        "Tax collection",
        "Loan repayment problems",
    ),

    q(
        "Banking",
        "Which body manages monetary policy in India?",
        "Reserve Bank of India",
        "Ministry of Railways",
        "Election Commission",
        "UPSC",
        "Reserve Bank of India",
    ),
]


# ============================================================
# RRB ALP
# ============================================================

RRB_ALP_QUESTIONS = [

    q(
        "RRB ALP",
        "What is the primary responsibility of an Assistant Loco Pilot?",
        "Assist in operating and monitoring the locomotive",
        "Issue railway tickets",
        "Maintain railway accounts",
        "Manage catering",
        "Assist in operating and monitoring the locomotive",
    ),

    q(
        "RRB ALP",
        "Which instrument measures electric current?",
        "Voltmeter",
        "Ammeter",
        "Ohmmeter",
        "Wattmeter",
        "Ammeter",
    ),

    q(
        "RRB ALP",
        "What is the SI unit of electric current?",
        "Volt",
        "Ampere",
        "Ohm",
        "Watt",
        "Ampere",
    ),

    q(
        "RRB ALP",
        "What is the SI unit of power?",
        "Joule",
        "Watt",
        "Newton",
        "Pascal",
        "Watt",
    ),

    q(
        "RRB ALP",
        "Which law relates voltage, current and resistance?",
        "Ohm's law",
        "Newton's law",
        "Boyle's law",
        "Faraday's law",
        "Ohm's law",
    ),

    q(
        "RRB ALP",
        "What is the formula for electrical power?",
        "P = VI",
        "P = V/I",
        "P = I/R",
        "P = R/V",
        "P = VI",
    ),

    q(
        "RRB ALP",
        "Which device converts electrical energy into mechanical energy?",
        "Motor",
        "Transformer",
        "Resistor",
        "Capacitor",
        "Motor",
    ),

    q(
        "RRB ALP",
        "Which device converts mechanical energy into electrical energy?",
        "Generator",
        "Motor",
        "Resistor",
        "Battery",
        "Generator",
    ),

    q(
        "RRB ALP",
        "What is the purpose of a railway signal?",
        "Control train movement",
        "Sell tickets",
        "Clean coaches",
        "Repair tracks",
        "Control train movement",
    ),

    q(
        "RRB ALP",
        "Which component stores electrical energy?",
        "Capacitor",
        "Switch",
        "Fuse",
        "Ammeter",
        "Capacitor",
    ),

    q(
        "RRB ALP",
        "What is a fuse designed to protect against?",
        "Excessive current",
        "Low temperature",
        "Low pressure",
        "Noise",
        "Excessive current",
    ),

    q(
        "RRB ALP",
        "Which material is generally a good conductor of electricity?",
        "Copper",
        "Rubber",
        "Glass",
        "Wood",
        "Copper",
    ),

    q(
        "RRB ALP",
        "What does AC stand for?",
        "Alternating Current",
        "Automatic Current",
        "Applied Current",
        "Active Circuit",
        "Alternating Current",
    ),

    q(
        "RRB ALP",
        "What does DC stand for?",
        "Direct Current",
        "Digital Current",
        "Dynamic Circuit",
        "Direct Circuit",
        "Direct Current",
    ),

    q(
        "RRB ALP",
        "Which unit measures resistance?",
        "Ohm",
        "Volt",
        "Ampere",
        "Watt",
        "Ohm",
    ),

    q(
        "RRB ALP",
        "Which force opposes motion between two surfaces?",
        "Friction",
        "Gravity",
        "Magnetism",
        "Thrust",
        "Friction",
    ),

    q(
        "RRB ALP",
        "Which simple machine is commonly used to lift loads?",
        "Pulley",
        "Thermometer",
        "Battery",
        "Ammeter",
        "Pulley",
    ),

    q(
        "RRB ALP",
        "What is the purpose of railway brakes?",
        "Reduce or stop train motion",
        "Increase fuel",
        "Increase voltage",
        "Control ticketing",
        "Reduce or stop train motion",
    ),

    q(
        "RRB ALP",
        "Which engine converts fuel energy into mechanical work?",
        "Internal combustion engine",
        "Transformer",
        "Battery",
        "Capacitor",
        "Internal combustion engine",
    ),

    q(
        "RRB ALP",
        "Which safety principle is essential for railway operation?",
        "Following signalling and operating rules",
        "Ignoring signals",
        "Increasing speed always",
        "Skipping inspections",
        "Following signalling and operating rules",
    ),
]


# ============================================================
# RRB TECHNICIAN
# ============================================================

RRB_TECHNICIAN_QUESTIONS = [

    q(
        "RRB Technician",
        "Which instrument measures voltage?",
        "Ammeter",
        "Voltmeter",
        "Ohmmeter",
        "Wattmeter",
        "Voltmeter",
    ),

    q(
        "RRB Technician",
        "Which instrument measures resistance?",
        "Voltmeter",
        "Ammeter",
        "Ohmmeter",
        "Galvanometer",
        "Ohmmeter",
    ),

    q(
        "RRB Technician",
        "Which metal is commonly used for electrical wiring?",
        "Copper",
        "Wood",
        "Rubber",
        "Glass",
        "Copper",
    ),

    q(
        "RRB Technician",
        "What is the function of insulation?",
        "Prevent unwanted current flow",
        "Increase current leakage",
        "Generate electricity",
        "Measure voltage",
        "Prevent unwanted current flow",
    ),

    q(
        "RRB Technician",
        "Which device protects an electrical circuit from excessive current?",
        "Fuse",
        "Motor",
        "Lamp",
        "Transformer",
        "Fuse",
    ),

    q(
        "RRB Technician",
        "What is the unit of frequency?",
        "Hertz",
        "Volt",
        "Ohm",
        "Watt",
        "Hertz",
    ),

    q(
        "RRB Technician",
        "What is the unit of electrical energy commonly used in domestic billing?",
        "Kilowatt-hour",
        "Volt",
        "Ampere",
        "Ohm",
        "Kilowatt-hour",
    ),

    q(
        "RRB Technician",
        "Which device changes AC voltage from one level to another?",
        "Transformer",
        "Motor",
        "Fuse",
        "Battery",
        "Transformer",
    ),

    q(
        "RRB Technician",
        "Which material is an electrical insulator?",
        "Rubber",
        "Copper",
        "Aluminium",
        "Iron",
        "Rubber",
    ),

    q(
        "RRB Technician",
        "Which tool is commonly used to tighten screws?",
        "Screwdriver",
        "Hammer",
        "Saw",
        "Pliers",
        "Screwdriver",
    ),

    q(
        "RRB Technician",
        "Which tool is used to measure length accurately in workshop work?",
        "Vernier caliper",
        "Compass",
        "Thermometer",
        "Barometer",
        "Vernier caliper",
    ),

    q(
        "RRB Technician",
        "Which process joins metals by heating them?",
        "Welding",
        "Painting",
        "Polishing",
        "Casting only",
        "Welding",
    ),

    q(
        "RRB Technician",
        "What is preventive maintenance?",
        "Maintenance performed to prevent failures",
        "Repair only after breakdown",
        "Replacing all machines daily",
        "Ignoring equipment",
        "Maintenance performed to prevent failures",
    ),

    q(
        "RRB Technician",
        "Which device converts electrical energy into light?",
        "Lamp",
        "Motor",
        "Transformer",
        "Generator",
        "Lamp",
    ),

    q(
        "RRB Technician",
        "What is the purpose of earthing?",
        "Provide a safe path for fault current",
        "Increase voltage",
        "Increase resistance",
        "Store electricity",
        "Provide a safe path for fault current",
    ),

    q(
        "RRB Technician",
        "Which quantity is measured in watts?",
        "Power",
        "Resistance",
        "Current",
        "Voltage",
        "Power",
    ),

    q(
        "RRB Technician",
        "Which quantity is measured in volts?",
        "Voltage",
        "Power",
        "Resistance",
        "Energy",
        "Voltage",
    ),

    q(
        "RRB Technician",
        "Which quantity is measured in amperes?",
        "Current",
        "Voltage",
        "Power",
        "Resistance",
        "Current",
    ),

    q(
        "RRB Technician",
        "Which device can store electrical energy chemically?",
        "Battery",
        "Fuse",
        "Switch",
        "Resistor",
        "Battery",
    ),

    q(
        "RRB Technician",
        "What should be done before working on an electrical circuit?",
        "Disconnect the power supply",
        "Touch bare wires",
        "Increase voltage",
        "Remove insulation",
        "Disconnect the power supply",
    ),
]


# ============================================================
# RRB JE
# ============================================================

RRB_JE_QUESTIONS = [

    q(
        "RRB JE",
        "What is the SI unit of force?",
        "Newton",
        "Joule",
        "Watt",
        "Pascal",
        "Newton",
    ),

    q(
        "RRB JE",
        "Which branch of engineering deals with structures and buildings?",
        "Civil Engineering",
        "Chemical Engineering",
        "Computer Engineering",
        "Aerospace Engineering",
        "Civil Engineering",
    ),

    q(
        "RRB JE",
        "Which instrument is used to measure pressure?",
        "Barometer",
        "Thermometer",
        "Ammeter",
        "Vernier caliper",
        "Barometer",
    ),

    q(
        "RRB JE",
        "What is concrete mainly composed of?",
        "Cement, aggregates and water",
        "Wood and steel only",
        "Glass and plastic",
        "Copper and aluminium",
        "Cement, aggregates and water",
    ),

    q(
        "RRB JE",
        "Which test determines the consistency of fresh concrete?",
        "Slump test",
        "Tensile test",
        "Hardness test",
        "Impact test",
        "Slump test",
    ),

    q(
        "RRB JE",
        "What is the function of reinforcement in reinforced concrete?",
        "Improve tensile strength",
        "Reduce all loads to zero",
        "Increase water content",
        "Replace cement",
        "Improve tensile strength",
    ),

    q(
        "RRB JE",
        "Which material is commonly used as reinforcement in concrete?",
        "Steel",
        "Glass",
        "Paper",
        "Rubber",
        "Steel",
    ),

    q(
        "RRB JE",
        "What is surveying primarily used for?",
        "Measurement and mapping of land",
        "Cooking",
        "Electrical wiring",
        "Banking",
        "Measurement and mapping of land",
    ),

    q(
        "RRB JE",
        "Which instrument measures horizontal and vertical angles in surveying?",
        "Theodolite",
        "Thermometer",
        "Ammeter",
        "Barometer",
        "Theodolite",
    ),

    q(
        "RRB JE",
        "Which branch of engineering deals with machines?",
        "Mechanical Engineering",
        "Civil Engineering",
        "Agricultural Engineering",
        "Textile Engineering",
        "Mechanical Engineering",
    ),

    q(
        "RRB JE",
        "What is torque?",
        "Turning effect of a force",
        "Linear speed only",
        "Electrical resistance",
        "Heat capacity",
        "Turning effect of a force",
    ),

    q(
        "RRB JE",
        "Which unit is used for torque?",
        "Newton-metre",
        "Volt",
        "Ampere",
        "Watt-hour",
        "Newton-metre",
    ),

    q(
        "RRB JE",
        "Which law relates current, voltage and resistance?",
        "Ohm's law",
        "Newton's law",
        "Hooke's law",
        "Boyle's law",
        "Ohm's law",
    ),

    q(
        "RRB JE",
        "Which machine converts mechanical energy into electrical energy?",
        "Generator",
        "Motor",
        "Transformer",
        "Compressor",
        "Generator",
    ),

    q(
        "RRB JE",
        "Which machine converts electrical energy into mechanical energy?",
        "Motor",
        "Generator",
        "Transformer",
        "Battery",
        "Motor",
    ),

    q(
        "RRB JE",
        "What is the purpose of a railway track?",
        "Guide and support railway vehicles",
        "Generate electricity",
        "Store fuel",
        "Sell tickets",
        "Guide and support railway vehicles",
    ),

    q(
        "RRB JE",
        "Which component supports a railway rail and transfers load to the foundation?",
        "Sleeper",
        "Signal",
        "Pantograph",
        "Buffer",
        "Sleeper",
    ),

    q(
        "RRB JE",
        "What is ballast used for in railway tracks?",
        "Support and drainage",
        "Fuel storage",
        "Train signalling only",
        "Ticket checking",
        "Support and drainage",
    ),

    q(
        "RRB JE",
        "What is the main purpose of railway signalling?",
        "Safe train movement",
        "Coach cleaning",
        "Ticket printing",
        "Passenger catering",
        "Safe train movement",
    ),

    q(
        "RRB JE",
        "What is preventive maintenance?",
        "Planned maintenance before failure",
        "Repair after complete destruction",
        "Ignoring defects",
        "Replacing all equipment daily",
        "Planned maintenance before failure",
    ),

]

RAILWAY_CONSTABLE_QUESTIONS = [

    q("RPF", "RPF stands for:",
      "Railway Protection Force", "Railway Police Force",
      "Railway Passenger Force", "Rail Protection Federation",
      "Railway Protection Force"),

    q("RPF", "The Railway Protection Force functions under which ministry?",
      "Ministry of Home Affairs", "Ministry of Railways",
      "Ministry of Defence", "Ministry of Transport",
      "Ministry of Railways"),

    q("RPF", "The primary responsibility of RPF is protection of:",
      "Railway property, passengers and passenger areas",
      "Only railway engines", "Only railway stations", "Only railway tracks",
      "Railway property, passengers and passenger areas"),

    q("RPF", "The Railway Protection Force Act was enacted in:",
      "1957", "1960", "1985", "1990",
      "1957"),

    q("RPF", "RPF personnel are primarily deployed for:",
      "Railway security", "Bank security",
      "Border security", "Airport security",
      "Railway security"),

    q("General Awareness", "The headquarters of Indian Railways is located in:",
      "Mumbai", "New Delhi", "Kolkata", "Chennai",
      "New Delhi"),

    q("General Awareness", "Indian Railways is one of the world's:",
      "Smallest railway networks", "Largest railway networks",
      "Private railway networks", "Underground railway networks",
      "Largest railway networks"),

    q("General Awareness", "The first passenger train in India ran between:",
      "Delhi and Agra", "Mumbai and Thane",
      "Chennai and Bengaluru", "Kolkata and Patna",
      "Mumbai and Thane"),

    q("General Awareness", "The first passenger railway service in India started in:",
      "1853", "1861", "1875", "1885",
      "1853"),

    q("General Awareness", "Which railway zone has its headquarters at Secunderabad?",
      "South Central Railway", "South Western Railway",
      "Central Railway", "East Coast Railway",
      "South Central Railway"),

    q("Indian Polity", "The fundamental rights are included in which part of the Constitution?",
      "Part I", "Part II", "Part III", "Part IV",
      "Part III"),

    q("Indian Polity", "Article 14 guarantees:",
      "Freedom of speech", "Equality before law",
      "Right to education", "Freedom of religion",
      "Equality before law"),

    q("Indian Polity", "The President of India is elected by:",
      "Direct vote of citizens",
      "Electoral College",
      "Prime Minister",
      "Supreme Court",
      "Electoral College"),

    q("Indian Polity", "The normal term of the Lok Sabha is:",
      "3 years", "4 years", "5 years", "6 years",
      "5 years"),

    q("Indian Polity", "The Supreme Court of India is located in:",
      "Mumbai", "New Delhi", "Hyderabad", "Kolkata",
      "New Delhi"),

    q("Indian Polity", "Who is the constitutional head of a state?",
      "Chief Minister", "Governor", "Chief Secretary", "Speaker",
      "Governor"),

    q("Indian Polity", "Who appoints the Governor of a state?",
      "Prime Minister", "President", "Chief Minister", "Chief Justice",
      "President"),

    q("General Science", "The SI unit of force is:",
      "Watt", "Newton", "Joule", "Pascal",
      "Newton"),

    q("General Science", "Which organ pumps blood throughout the human body?",
      "Lungs", "Heart", "Kidney", "Liver",
      "Heart"),

    q("General Science", "Which gas is essential for respiration?",
      "Nitrogen", "Oxygen", "Hydrogen", "Carbon dioxide",
      "Oxygen"),

    q("General Science", "Which blood cells fight infections?",
      "RBC", "WBC", "Platelets", "Plasma",
      "WBC"),

    q("General Science", "Vitamin C deficiency causes:",
      "Rickets", "Scurvy", "Beriberi", "Night blindness",
      "Scurvy"),

    q("General Science", "The chemical formula of water is:",
      "CO2", "H2O", "O2", "NaCl",
      "H2O"),

    q("General Science", "Which planet is known as the Red Planet?",
      "Venus", "Mars", "Jupiter", "Mercury",
      "Mars"),

    q("General Science", "The largest planet in the Solar System is:",
      "Earth", "Saturn", "Jupiter", "Neptune",
      "Jupiter"),

    q("Reasoning", "Complete the series: 5, 10, 15, 20, ?",
      "22", "25", "30", "35",
      "25"),

    q("Reasoning", "Complete the series: 2, 4, 8, 16, ?",
      "24", "28", "32", "36",
      "32"),

    q("Reasoning", "Find the odd one out:",
      "Train", "Bus", "Car", "Mango",
      "Mango"),

    q("Reasoning", "If CAT is coded as DBU, DOG will be coded as:",
      "EPH", "EOG", "FOH", "DPG",
      "EPH"),

    q("Reasoning", "A is taller than B. B is taller than C. Who is shortest?",
      "A", "B", "C", "Cannot determine",
      "C"),

    q("Reasoning", "If NORTH is coded as OPSUI, SOUTH is coded as:",
      "TPVUI", "TPVTH", "TPTUI", "SPVUI",
      "TPVUI"),

    q("Reasoning", "Complete: AZ, BY, CX, DW, ?",
      "EV", "EU", "FV", "EW",
      "EV"),

    q("Reasoning", "Find the odd one out:",
      "Square", "Triangle", "Circle", "Railway",
      "Railway"),

    q("Reasoning", "If 1 = 2, 2 = 4, 3 = 6, then 8 = ?",
      "12", "14", "16", "18",
      "16"),

    q("Reasoning", "A person walks north and then turns right. Which direction is he facing?",
      "West", "East", "South", "North",
      "East"),

    q("Mathematics", "25% of 400 is:",
      "50", "75", "100", "125",
      "100"),

    q("Mathematics", "The HCF of 18 and 24 is:",
      "3", "6", "9", "12",
      "6"),

    q("Mathematics", "The LCM of 12 and 15 is:",
      "30", "45", "60", "75",
      "60"),

    q("Mathematics", "A train travels 180 km in 3 hours. Its speed is:",
      "40 km/h", "50 km/h", "60 km/h", "70 km/h",
      "60 km/h"),

    q("Mathematics", "If CP is ₹500 and SP is ₹600, profit is:",
      "₹50", "₹75", "₹100", "₹150",
      "₹100"),

    q("Mathematics", "The average of 10, 20 and 30 is:",
      "15", "20", "25", "30",
      "20"),

    q("Mathematics", "What is 15 × 12?",
      "160", "170", "180", "190",
      "180"),

    q("Mathematics", "The square of 20 is:",
      "200", "300", "400", "500",
      "400"),

    q("General Awareness", "The national animal of India is:",
      "Lion", "Tiger", "Elephant", "Leopard",
      "Tiger"),

    q("General Awareness", "The national flower of India is:",
      "Rose", "Lotus", "Lily", "Jasmine",
      "Lotus"),

    q("General Awareness", "The national sport officially recognised by India is:",
      "Hockey", "Cricket", "Football", "No official national sport",
      "No official national sport"),

    q("RPF", "RPF personnel may assist in maintaining security at:",
      "Railway stations", "Banks only", "Schools only", "Hospitals only",
      "Railway stations"),

    q("RPF", "Which force primarily handles law and order within railway premises in coordination with RPF?",
      "State Government Railway Police", "Air Force",
      "Army", "Coast Guard",
      "State Government Railway Police"),

    q("RPF", "RPF is primarily concerned with the protection of:",
      "Railway property", "Agricultural land", "Sea ports", "Air bases",
      "Railway property"),

    q("Current Affairs", "The railway network in India is operated primarily by:",
      "Indian Railways", "Private banks", "State police",
      "Ministry of Defence",
      "Indian Railways"),
]

RAILWAY_SI_QUESTIONS = [

    q("RPF", "RPF stands for:",
      "Railway Protection Force", "Railway Police Force",
      "Railway Passenger Force", "Rail Protection Federation",
      "Railway Protection Force"),

    q("RPF", "The Railway Protection Force works under:",
      "Ministry of Railways", "Ministry of Defence",
      "Ministry of Home Affairs", "Ministry of Law",
      "Ministry of Railways"),

    q("RPF", "The main duty of RPF is protection of:",
      "Railway property and passengers", "Only railway employees",
      "Only railway bridges", "Only railway engines",
      "Railway property and passengers"),

    q("Law", "The Indian Penal Code has been replaced by:",
      "BNS", "BNSS", "BSA", "RTI Act",
      "BNS"),

    q("Law", "BNSS primarily deals with:",
      "Criminal procedure", "Evidence only", "Contracts",
      "Civil procedure",
      "Criminal procedure"),

    q("Law", "BSA primarily deals with:",
      "Evidence", "Criminal procedure", "Taxation", "Contracts",
      "Evidence"),

    q("Law", "The Supreme Court of India is the highest:",
      "Legislative body", "Judicial body", "Executive body",
      "Election body",
      "Judicial body"),

    q("Law", "The Constitution of India guarantees equality before law under:",
      "Article 12", "Article 14", "Article 19", "Article 21",
      "Article 14"),

    q("Law", "Article 21 protects:",
      "Life and personal liberty", "Freedom of religion",
      "Right to property", "Right to vote",
      "Life and personal liberty"),

    q("Law", "The right to constitutional remedies is associated with:",
      "Article 32", "Article 40", "Article 44", "Article 51",
      "Article 32"),

    q("Indian Polity", "The President of India is:",
      "Head of State", "Head of Government", "Chief Justice",
      "Speaker",
      "Head of State"),

    q("Indian Polity", "The Council of Ministers is headed by:",
      "President", "Prime Minister", "Vice-President", "Speaker",
      "Prime Minister"),

    q("Indian Polity", "The normal term of Lok Sabha is:",
      "4 years", "5 years", "6 years", "7 years",
      "5 years"),

    q("Indian Polity", "The Supreme Court is located in:",
      "New Delhi", "Mumbai", "Chennai", "Hyderabad",
      "New Delhi"),

    q("Indian Polity", "The Governor of a state is appointed by:",
      "President", "Prime Minister", "Chief Minister", "Chief Justice",
      "President"),

    q("Railway Security", "RPF is responsible for protecting:",
      "Railway property", "National highways",
      "Airports", "Sea ports",
      "Railway property"),

    q("Railway Security", "Railway security requires coordination between RPF and:",
      "Government Railway Police", "Forest Department",
      "Income Tax Department", "Postal Department",
      "Government Railway Police"),

    q("Railway Security", "RPF personnel may assist passengers during:",
      "Security emergencies", "Bank audits", "School examinations",
      "Tax collection",
      "Security emergencies"),

    q("Railway Security", "An unattended suspicious object at a station should be:",
      "Reported immediately", "Opened immediately",
      "Moved personally", "Ignored",
      "Reported immediately"),

    q("Railway Security", "Crowd management is important at:",
      "Busy railway stations", "Only offices",
      "Only courts", "Only banks",
      "Busy railway stations"),

    q("Reasoning", "Complete: 3, 6, 12, 24, ?",
      "36", "42", "48", "54",
      "48"),

    q("Reasoning", "Complete: 10, 20, 30, 40, ?",
      "45", "50", "55", "60",
      "50"),

    q("Reasoning", "Find the odd one:",
      "Police", "Army", "Navy", "Banana",
      "Banana"),

    q("Reasoning", "If DOG is coded as EPH, CAT is coded as:",
      "DBU", "DCT", "CBU", "EBU",
      "DBU"),

    q("Reasoning", "A is older than B and B is older than C. Who is youngest?",
      "A", "B", "C", "Cannot say",
      "C"),

    q("Reasoning", "If EAST is opposite to WEST, NORTH is opposite to:",
      "South", "East", "West", "North-East",
      "South"),

    q("Reasoning", "Find the odd one:",
      "Circle", "Square", "Triangle", "Train",
      "Train"),

    q("Mathematics", "20% of 500 is:",
      "50", "75", "100", "125",
      "100"),

    q("Mathematics", "The HCF of 36 and 48 is:",
      "6", "12", "18", "24",
      "12"),

    q("Mathematics", "The LCM of 8 and 12 is:",
      "16", "20", "24", "32",
      "24"),

    q("Mathematics", "A vehicle travels 240 km in 4 hours. Speed is:",
      "40 km/h", "50 km/h", "60 km/h", "80 km/h",
      "60 km/h"),

    q("Mathematics", "The average of 15, 25 and 35 is:",
      "20", "25", "30", "35",
      "25"),

    q("Mathematics", "If CP = ₹800 and SP = ₹1,000, profit is:",
      "₹100", "₹150", "₹200", "₹250",
      "₹200"),

    q("General Science", "The SI unit of force is:",
      "Newton", "Joule", "Watt", "Volt",
      "Newton"),

    q("General Science", "Which organ pumps blood?",
      "Heart", "Liver", "Kidney", "Lungs",
      "Heart"),

    q("General Science", "Which gas is essential for breathing?",
      "Oxygen", "Nitrogen", "Hydrogen", "Helium",
      "Oxygen"),

    q("General Science", "Which blood cells fight infection?",
      "RBC", "WBC", "Platelets", "Plasma",
      "WBC"),

    q("General Awareness", "The headquarters of Indian Railways is:",
      "New Delhi", "Mumbai", "Kolkata", "Chennai",
      "New Delhi"),

    q("General Awareness", "The first passenger train in India ran between:",
      "Mumbai and Thane", "Delhi and Agra",
      "Chennai and Bengaluru", "Kolkata and Delhi",
      "Mumbai and Thane"),

    q("General Awareness", "South Central Railway headquarters is located at:",
      "Secunderabad", "Hyderabad", "Vijayawada", "Warangal",
      "Secunderabad"),

    q("English", "Choose the synonym of ALERT:",
      "Careless", "Vigilant", "Lazy", "Weak",
      "Vigilant"),

    q("English", "Choose the antonym of GUILTY:",
      "Criminal", "Innocent", "Accused", "Convicted",
      "Innocent"),

    q("English", "Choose the correctly spelt word:",
      "Surveillance", "Surveliance", "Surveilance", "Survillance",
      "Surveillance"),

    q("English", "Choose the correct sentence:",
      "He go to the station.",
      "He goes to the station.",
      "He going station.",
      "He gone station.",
      "He goes to the station."),

    q("General Awareness", "The national animal of India is:",
      "Tiger", "Lion", "Elephant", "Leopard",
      "Tiger"),

    q("General Awareness", "The Indian Constitution came into effect on:",
      "15 August 1947", "26 November 1949",
      "26 January 1950", "2 October 1950",
      "26 January 1950"),

    q("RPF", "RPF stands for:",
      "Railway Protection Force", "Railway Police Force",
      "Rail Passenger Force", "Railway Patrol Force",
      "Railway Protection Force"),

    q("RPF", "The primary role of RPF is:",
      "Railway security", "Border security",
      "Air security", "Forest protection",
      "Railway security"),

    q("Law", "A person is presumed innocent until:",
      "Arrested", "Proved guilty according to law",
      "Questioned", "Charged",
      "Proved guilty according to law"),

    q("Law", "The rule of law means:",
      "Everyone is subject to law",
      "Only police follow law",
      "Only courts follow law",
      "Only citizens follow law",
      "Everyone is subject to law"),
]

# ============================================================
# FOREST RANGE OFFICER - 50 QUESTIONS
# ============================================================

FOREST_RANGE_OFFICER_QUESTIONS = [

    q(
        "Forestry",
        "Which branch of science deals with the management of forests?",
        "Forestry",
        "Agronomy",
        "Geology",
        "Hydrology",
        "Forestry",
    ),

    q(
        "Forestry",
        "The scientific management of forests for sustained production is called:",
        "Silviculture",
        "Horticulture",
        "Pisciculture",
        "Sericulture",
        "Silviculture",
    ),

    q(
        "Forestry",
        "Silviculture primarily deals with:",
        "Cultivation and management of forest trees",
        "Study of rocks",
        "Study of insects",
        "Water management",
        "Cultivation and management of forest trees",
    ),

    q(
        "Forestry",
        "The process of planting trees on land that was previously not forested is called:",
        "Afforestation",
        "Deforestation",
        "Desertification",
        "Urbanisation",
        "Afforestation",
    ),

    q(
        "Forestry",
        "Reforestation means:",
        "Replanting trees in areas where forests were removed",
        "Removing forests",
        "Converting forests into farms",
        "Cutting mature trees",
        "Replanting trees in areas where forests were removed",
    ),

    q(
        "Forestry",
        "The uppermost layer formed by tree crowns in a forest is called:",
        "Canopy",
        "Litter",
        "Humus",
        "Understorey",
        "Canopy",
    ),

    q(
        "Forestry",
        "The layer of dead leaves and organic material on the forest floor is called:",
        "Litter",
        "Canopy",
        "Bark",
        "Sapwood",
        "Litter",
    ),

    q(
        "Forestry",
        "Which tissue transports water from roots to leaves?",
        "Phloem",
        "Xylem",
        "Cambium",
        "Epidermis",
        "Xylem",
    ),

    q(
        "Forestry",
        "Which tissue transports prepared food in plants?",
        "Xylem",
        "Phloem",
        "Cork",
        "Cambium",
        "Phloem",
    ),

    q(
        "Forestry",
        "The process by which green plants prepare food is:",
        "Respiration",
        "Photosynthesis",
        "Transpiration",
        "Germination",
        "Photosynthesis",
    ),

    q(
        "Forestry",
        "The pigment responsible for the green colour of leaves is:",
        "Chlorophyll",
        "Carotene",
        "Melanin",
        "Haemoglobin",
        "Chlorophyll",
    ),

    q(
        "Forestry",
        "Which gas is absorbed by plants during photosynthesis?",
        "Oxygen",
        "Carbon dioxide",
        "Nitrogen",
        "Hydrogen",
        "Carbon dioxide",
    ),

    q(
        "Forestry",
        "The loss of water vapour from plant leaves is called:",
        "Respiration",
        "Transpiration",
        "Photosynthesis",
        "Absorption",
        "Transpiration",
    ),

    q(
        "Forestry",
        "The age of a tree can often be estimated by counting:",
        "Branches",
        "Annual rings",
        "Leaves",
        "Roots",
        "Annual rings",
    ),

    q(
        "Forestry",
        "The central woody part of a mature tree is commonly called:",
        "Heartwood",
        "Sapwood",
        "Cambium",
        "Bark",
        "Heartwood",
    ),

    q(
        "Forestry",
        "The actively conducting outer wood of a tree is called:",
        "Heartwood",
        "Sapwood",
        "Pith",
        "Bark",
        "Sapwood",
    ),

    q(
        "Forestry",
        "Which part of a tree protects the inner tissues from external damage?",
        "Bark",
        "Root",
        "Pith",
        "Flower",
        "Bark",
    ),

    q(
        "Forestry",
        "Which of the following is a major forest product?",
        "Timber",
        "Plastic",
        "Petroleum",
        "Cement",
        "Timber",
    ),

    q(
        "Forestry",
        "Bamboo belongs to which plant family?",
        "Poaceae",
        "Fabaceae",
        "Solanaceae",
        "Rosaceae",
        "Poaceae",
    ),

    q(
        "Forestry",
        "Teak is scientifically known as:",
        "Tectona grandis",
        "Azadirachta indica",
        "Ficus religiosa",
        "Mangifera indica",
        "Tectona grandis",
    ),

    q(
        "Forestry",
        "Neem is scientifically known as:",
        "Azadirachta indica",
        "Tectona grandis",
        "Dalbergia sissoo",
        "Shorea robusta",
        "Azadirachta indica",
    ),

    q(
        "Forestry",
        "Sandalwood is mainly valued for its:",
        "Fragrant heartwood",
        "Edible leaves",
        "Fruit juice",
        "Bark fibre",
        "Fragrant heartwood",
    ),

    q(
        "Wildlife",
        "The scientific study of animals is called:",
        "Botany",
        "Zoology",
        "Geology",
        "Ecology",
        "Zoology",
    ),

    q(
        "Wildlife",
        "The scientific study of the relationships between organisms and their environment is:",
        "Ecology",
        "Genetics",
        "Taxonomy",
        "Anatomy",
        "Ecology",
    ),

    q(
        "Wildlife",
        "A group of organisms of the same species living in an area is called:",
        "Population",
        "Community",
        "Ecosystem",
        "Biome",
        "Population",
    ),

    q(
        "Wildlife",
        "A community of organisms together with their physical environment forms:",
        "Ecosystem",
        "Population",
        "Species",
        "Habitat",
        "Ecosystem",
    ),

    q(
        "Wildlife",
        "The natural home of an organism is called its:",
        "Habitat",
        "Niche",
        "Population",
        "Biome",
        "Habitat",
    ),

    q(
        "Wildlife",
        "Animals that eat only plants are called:",
        "Carnivores",
        "Herbivores",
        "Omnivores",
        "Decomposers",
        "Herbivores",
    ),

    q(
        "Wildlife",
        "Animals that primarily eat other animals are called:",
        "Herbivores",
        "Carnivores",
        "Producers",
        "Decomposers",
        "Carnivores",
    ),

    q(
        "Wildlife",
        "Animals that eat both plants and animals are called:",
        "Herbivores",
        "Carnivores",
        "Omnivores",
        "Parasites",
        "Omnivores",
    ),

    q(
        "Wildlife",
        "Which of the following is a primary producer in a forest ecosystem?",
        "Green plant",
        "Tiger",
        "Deer",
        "Fungus",
        "Green plant",
    ),

    q(
        "Wildlife",
        "Which organisms are major decomposers in forest ecosystems?",
        "Fungi and bacteria",
        "Tigers and lions",
        "Deer and elephants",
        "Birds and reptiles",
        "Fungi and bacteria",
    ),

    q(
        "Wildlife",
        "The variety of living organisms in an area is called:",
        "Biodiversity",
        "Biomass",
        "Biogeography",
        "Population density",
        "Biodiversity",
    ),

    q(
        "Wildlife",
        "A species found naturally only in a particular geographical region is called:",
        "Endemic species",
        "Migratory species",
        "Domestic species",
        "Invasive species",
        "Endemic species",
    ),

    q(
        "Wildlife",
        "A species facing a very high risk of extinction is classified as:",
        "Least Concern",
        "Endangered",
        "Common",
        "Domestic",
        "Endangered",
    ),

    q(
        "Environment",
        "The gradual increase in Earth's average temperature is called:",
        "Global warming",
        "Acid rain",
        "Ozone formation",
        "Eutrophication",
        "Global warming",
    ),

    q(
        "Environment",
        "The major greenhouse gas released by burning fossil fuels is:",
        "Carbon dioxide",
        "Oxygen",
        "Nitrogen",
        "Helium",
        "Carbon dioxide",
    ),

    q(
        "Environment",
        "The ozone layer protects Earth from harmful:",
        "Ultraviolet radiation",
        "Radio waves",
        "Sound waves",
        "Infrared radiation",
        "Ultraviolet radiation",
    ),

    q(
        "Environment",
        "Acid rain is mainly caused by emissions of:",
        "Sulphur dioxide and nitrogen oxides",
        "Oxygen and hydrogen",
        "Carbon and helium",
        "Nitrogen and oxygen only",
        "Sulphur dioxide and nitrogen oxides",
    ),

    q(
        "Environment",
        "The conversion of forest land into non-forest land is called:",
        "Deforestation",
        "Afforestation",
        "Reforestation",
        "Conservation",
        "Deforestation",
    ),

    q(
        "Environment",
        "Soil erosion can be reduced effectively by:",
        "Planting vegetation",
        "Removing trees",
        "Overgrazing",
        "Burning forests",
        "Planting vegetation",
    ),

    q(
        "Environment",
        "Which practice helps conserve soil in forest areas?",
        "Maintaining vegetation cover",
        "Excessive grazing",
        "Clear cutting",
        "Burning vegetation",
        "Maintaining vegetation cover",
    ),

    q(
        "Wildlife Conservation",
        "Project Tiger was launched in India in:",
        "1973",
        "1980",
        "1985",
        "1990",
        "1973",
    ),

    q(
        "Wildlife Conservation",
        "The main objective of Project Tiger is:",
        "Conservation of tigers and their habitat",
        "Increasing timber production",
        "Promoting hunting",
        "Urban development",
        "Conservation of tigers and their habitat",
    ),

    q(
        "Wildlife Conservation",
        "A protected area primarily established for wildlife conservation is:",
        "Wildlife sanctuary",
        "Industrial zone",
        "Mining zone",
        "Residential zone",
        "Wildlife sanctuary",
    ),

    q(
        "Wildlife Conservation",
        "National parks are established mainly for:",
        "Conservation of wildlife and ecosystems",
        "Commercial mining",
        "Industrial production",
        "Urban expansion",
        "Conservation of wildlife and ecosystems",
    ),

    q(
        "Wildlife Conservation",
        "The Wildlife Protection Act of India was enacted in:",
        "1972",
        "1962",
        "1982",
        "1992",
        "1972",
    ),

    q(
        "Environment",
        "The Ramsar Convention is associated with conservation of:",
        "Wetlands",
        "Deserts",
        "Mountains",
        "Grasslands only",
        "Wetlands",
    ),

    q(
        "Environment",
        "Mangrove forests are commonly found in:",
        "Coastal and tidal areas",
        "Desert regions",
        "High mountains",
        "Dry grasslands",
        "Coastal and tidal areas",
    ),

    q(
        "Environment",
        "Mangrove forests are important because they:",
        "Protect coastal areas from erosion",
        "Increase desertification",
        "Reduce biodiversity",
        "Prevent rainfall",
        "Protect coastal areas from erosion",
    ),

    q(
        "Forestry",
        "Social forestry primarily aims to:",
        "Meet local needs for fuelwood, fodder and small timber",
        "Increase mining",
        "Promote urban construction",
        "Remove village vegetation",
        "Meet local needs for fuelwood, fodder and small timber",
    ),

    q(
        "Forestry",
        "Agroforestry refers to:",
        "Combining trees with crops and/or livestock",
        "Growing only forest trees",
        "Removing trees from farmland",
        "Growing crops only",
        "Combining trees with crops and/or livestock",
    ),

]

# ============================================================
# UPSC - 50 EXAM-SPECIFIC QUESTIONS
# ============================================================

UPSC_QUESTIONS = [

    # ---------------- POLITY ----------------

    q(
        "Indian Polity",
        "Which part of the Indian Constitution deals with Fundamental Rights?",
        "Part II",
        "Part III",
        "Part IV",
        "Part V",
        "Part III",
        "Medium",
    ),

    q(
        "Indian Polity",
        "Which Article guarantees equality before the law and equal protection of laws?",
        "Article 12",
        "Article 14",
        "Article 19",
        "Article 21",
        "Article 14",
        "Medium",
    ),

    q(
        "Indian Polity",
        "The Directive Principles of State Policy are contained in which part of the Constitution?",
        "Part II",
        "Part III",
        "Part IV",
        "Part VI",
        "Part IV",
        "Medium",
    ),

    q(
        "Indian Polity",
        "Who is the constitutional head of the Union Executive in India?",
        "Prime Minister",
        "President",
        "Vice-President",
        "Home Minister",
        "President",
        "Easy",
    ),

    q(
        "Indian Polity",
        "Which constitutional amendment reduced the voting age in India from 21 to 18 years?",
        "42nd Amendment",
        "44th Amendment",
        "61st Amendment",
        "73rd Amendment",
        "61st Amendment",
        "Medium",
    ),

    q(
        "Indian Polity",
        "The power of judicial review in India is exercised by which institutions?",
        "Only Parliament",
        "Only President",
        "Supreme Court and High Courts",
        "Election Commission",
        "Supreme Court and High Courts",
        "Medium",
    ),

    q(
        "Indian Polity",
        "Which body conducts elections to Parliament and State Legislatures?",
        "Union Public Service Commission",
        "Election Commission of India",
        "Finance Commission",
        "Law Commission",
        "Election Commission of India",
        "Easy",
    ),

    q(
        "Indian Polity",
        "Which Article provides for the establishment of the Finance Commission?",
        "Article 280",
        "Article 324",
        "Article 356",
        "Article 368",
        "Article 280",
        "Medium",
    ),

    # ---------------- HISTORY ----------------

    q(
        "Indian History",
        "Which ancient civilization is associated with planned cities such as Harappa and Mohenjo-daro?",
        "Vedic Civilization",
        "Indus Valley Civilization",
        "Mauryan Civilization",
        "Gupta Civilization",
        "Indus Valley Civilization",
        "Easy",
    ),

    q(
        "Indian History",
        "Who founded the Mauryan Empire?",
        "Ashoka",
        "Chandragupta Maurya",
        "Bindusara",
        "Samudragupta",
        "Chandragupta Maurya",
        "Easy",
    ),

    q(
        "Indian History",
        "Who wrote the Arthashastra?",
        "Kalidasa",
        "Kautilya",
        "Banabhatta",
        "Megasthenes",
        "Kautilya",
        "Medium",
    ),

    q(
        "Indian History",
        "The Battle of Plassey was fought in which year?",
        "1757",
        "1761",
        "1764",
        "1772",
        "1757",
        "Easy",
    ),

    q(
        "Indian History",
        "Who introduced the Permanent Settlement in Bengal?",
        "Lord Wellesley",
        "Lord Cornwallis",
        "Lord Dalhousie",
        "Lord Curzon",
        "Lord Cornwallis",
        "Medium",
    ),

    q(
        "Indian History",
        "The Revolt of 1857 first broke out at which place?",
        "Delhi",
        "Kanpur",
        "Meerut",
        "Lucknow",
        "Meerut",
        "Easy",
    ),

    q(
        "Indian History",
        "Who founded the Indian National Congress in 1885 along with other early leaders?",
        "A. O. Hume",
        "Lord Curzon",
        "Dadabhai Naoroji",
        "Surendranath Banerjee",
        "A. O. Hume",
        "Medium",
    ),

    q(
        "Indian History",
        "The Non-Cooperation Movement was launched by Mahatma Gandhi in which year?",
        "1917",
        "1919",
        "1920",
        "1922",
        "1920",
        "Easy",
    ),

    # ---------------- GEOGRAPHY ----------------

    q(
        "Indian Geography",
        "Which is the largest state in India by geographical area?",
        "Madhya Pradesh",
        "Maharashtra",
        "Rajasthan",
        "Uttar Pradesh",
        "Rajasthan",
        "Easy",
    ),

    q(
        "Indian Geography",
        "Which river is known as the Dakshin Ganga?",
        "Krishna",
        "Godavari",
        "Kaveri",
        "Narmada",
        "Godavari",
        "Easy",
    ),

    q(
        "Indian Geography",
        "The Western Ghats and Eastern Ghats meet at which hills?",
        "Aravalli Hills",
        "Nilgiri Hills",
        "Vindhya Hills",
        "Satpura Hills",
        "Nilgiri Hills",
        "Medium",
    ),

    q(
        "Indian Geography",
        "Which soil is particularly suitable for cotton cultivation?",
        "Alluvial soil",
        "Black soil",
        "Laterite soil",
        "Red soil",
        "Black soil",
        "Easy",
    ),

    q(
        "Indian Geography",
        "Which Indian river flows through a rift valley?",
        "Ganga",
        "Yamuna",
        "Narmada",
        "Brahmaputra",
        "Narmada",
        "Medium",
    ),

    q(
        "Indian Geography",
        "Which state has the longest coastline in India?",
        "Tamil Nadu",
        "Andhra Pradesh",
        "Gujarat",
        "Maharashtra",
        "Gujarat",
        "Easy",
    ),

    q(
        "World Geography",
        "Which is the largest ocean on Earth?",
        "Atlantic Ocean",
        "Indian Ocean",
        "Pacific Ocean",
        "Arctic Ocean",
        "Pacific Ocean",
        "Easy",
    ),

    q(
        "World Geography",
        "The Tropic of Cancer passes through how many Indian states?",
        "6",
        "7",
        "8",
        "9",
        "8",
        "Medium",
    ),

    # ---------------- ECONOMY ----------------

    q(
        "Indian Economy",
        "Which institution is responsible for monetary policy in India?",
        "SEBI",
        "RBI",
        "NITI Aayog",
        "Finance Commission",
        "RBI",
        "Easy",
    ),

    q(
        "Indian Economy",
        "What does GDP stand for?",
        "Gross Domestic Product",
        "General Domestic Production",
        "Gross Development Product",
        "Government Domestic Product",
        "Gross Domestic Product",
        "Easy",
    ),

    q(
        "Indian Economy",
        "Which organization replaced the Planning Commission?",
        "Finance Commission",
        "NITI Aayog",
        "RBI",
        "Economic Advisory Council",
        "NITI Aayog",
        "Easy",
    ),

    q(
        "Indian Economy",
        "Which tax is imposed on the supply of goods and services under the GST system?",
        "Direct tax",
        "Indirect tax",
        "Wealth tax",
        "Corporate tax only",
        "Indirect tax",
        "Medium",
    ),

    q(
        "Indian Economy",
        "Inflation refers to:",
        "Fall in general price level",
        "Rise in general price level",
        "Fall in money supply",
        "Rise in unemployment only",
        "Rise in general price level",
        "Easy",
    ),

    q(
        "Indian Economy",
        "Which institution regulates the securities market in India?",
        "RBI",
        "SEBI",
        "IRDAI",
        "PFRDA",
        "SEBI",
        "Easy",
    ),

    q(
        "Indian Economy",
        "Which sector includes agriculture, forestry and fishing?",
        "Primary sector",
        "Secondary sector",
        "Tertiary sector",
        "Quaternary sector",
        "Primary sector",
        "Easy",
    ),

    q(
        "Indian Economy",
        "What is fiscal deficit broadly associated with?",
        "Government expenditure exceeding revenue excluding borrowings",
        "Increase in exports",
        "Decrease in imports",
        "Increase in foreign exchange reserves",
        "Government expenditure exceeding revenue excluding borrowings",
        "Medium",
    ),

    # ---------------- ENVIRONMENT ----------------

    q(
        "Environment",
        "Which gas is the major contributor to the enhanced greenhouse effect among the following?",
        "Carbon dioxide",
        "Oxygen",
        "Nitrogen",
        "Argon",
        "Carbon dioxide",
        "Easy",
    ),

    q(
        "Environment",
        "The Ramsar Convention is primarily associated with:",
        "Forests",
        "Wetlands",
        "Mountains",
        "Deserts",
        "Wetlands",
        "Easy",
    ),

    q(
        "Environment",
        "Which organization publishes the Red List of Threatened Species?",
        "UNESCO",
        "IUCN",
        "UNEP",
        "FAO",
        "IUCN",
        "Medium",
    ),

    q(
        "Environment",
        "Project Tiger was launched in India in which year?",
        "1969",
        "1973",
        "1980",
        "1986",
        "1973",
        "Medium",
    ),

    q(
        "Environment",
        "Which ecosystem has the highest biodiversity among the following?",
        "Tundra",
        "Tropical rainforest",
        "Desert",
        "Polar region",
        "Tropical rainforest",
        "Easy",
    ),

    q(
        "Environment",
        "The ozone layer is mainly found in which atmospheric layer?",
        "Troposphere",
        "Stratosphere",
        "Mesosphere",
        "Thermosphere",
        "Stratosphere",
        "Easy",
    ),

    q(
        "Environment",
        "Which of the following is a renewable source of energy?",
        "Coal",
        "Petroleum",
        "Solar energy",
        "Natural gas",
        "Solar energy",
        "Easy",
    ),

    q(
        "Environment",
        "The Paris Agreement primarily deals with:",
        "International trade",
        "Climate change",
        "Nuclear weapons",
        "Ocean boundaries",
        "Climate change",
        "Easy",
    ),

    # ---------------- GOVERNANCE ----------------

    q(
        "Governance",
        "Which constitutional body audits the accounts of the Union and State governments?",
        "Election Commission",
        "Comptroller and Auditor General",
        "Finance Commission",
        "UPSC",
        "Comptroller and Auditor General",
        "Medium",
    ),

    q(
        "Governance",
        "The Right to Information Act in India was enacted in:",
        "2001",
        "2003",
        "2005",
        "2007",
        "2005",
        "Easy",
    ),

    q(
        "Governance",
        "Which body is responsible for conducting the Civil Services Examination?",
        "SSC",
        "UPSC",
        "IBPS",
        "NTA",
        "UPSC",
        "Easy",
    ),

    q(
        "Governance",
        "The concept of Panchayati Raj received constitutional status through which amendment?",
        "42nd Amendment",
        "61st Amendment",
        "73rd Amendment",
        "86th Amendment",
        "73rd Amendment",
        "Medium",
    ),

    q(
        "Governance",
        "Municipalities received constitutional recognition through which amendment?",
        "72nd Amendment",
        "73rd Amendment",
        "74th Amendment",
        "86th Amendment",
        "74th Amendment",
        "Medium",
    ),

    q(
        "Governance",
        "Which schedule of the Constitution contains provisions related to Panchayats?",
        "Ninth Schedule",
        "Tenth Schedule",
        "Eleventh Schedule",
        "Twelfth Schedule",
        "Eleventh Schedule",
        "Medium",
    ),

    # ---------------- SCIENCE & TECHNOLOGY ----------------

    q(
        "Science and Technology",
        "Which Indian space organization is responsible for the country's space programme?",
        "DRDO",
        "ISRO",
        "BARC",
        "CSIR",
        "ISRO",
        "Easy",
    ),

    q(
        "Science and Technology",
        "What is the primary purpose of a satellite navigation system?",
        "Weather creation",
        "Position and navigation",
        "Electricity generation",
        "Water purification",
        "Position and navigation",
        "Easy",
    ),

    q(
        "Science and Technology",
        "Which technology uses the splitting of atoms to release energy?",
        "Solar technology",
        "Nuclear fission",
        "Wind technology",
        "Hydroelectric technology",
        "Nuclear fission",
        "Medium",
    ),

    q(
        "Science and Technology",
        "Which branch of science deals with heredity and variation?",
        "Ecology",
        "Genetics",
        "Geology",
        "Astronomy",
        "Genetics",
        "Easy",
    ),

    q(
        "Science and Technology",
        "What does AI stand for?",
        "Automated Internet",
        "Artificial Intelligence",
        "Advanced Information",
        "Applied Intelligence",
        "Artificial Intelligence",
        "Easy",
    ),

    q(
        "Science and Technology",
        "Which material is commonly used as a semiconductor in electronic devices?",
        "Silicon",
        "Wood",
        "Rubber",
        "Glass",
        "Silicon",
        "Easy",
    ),

    # ---------------- INTERNATIONAL RELATIONS ----------------

    q(
        "International Relations",
        "Where is the headquarters of the World Health Organization located?",
        "New York",
        "Geneva",
        "Paris",
        "Vienna",
        "Geneva",
        "Easy",
    ),

    q(
        "International Relations",
        "The United Nations Security Council has how many permanent members?",
        "3",
        "4",
        "5",
        "6",
        "5",
        "Easy",
    ),

    q(
        "International Relations",
        "Which organization is primarily concerned with international monetary cooperation?",
        "IMF",
        "WHO",
        "UNESCO",
        "ILO",
        "IMF",
        "Medium",
    ),

    q(
        "International Relations",
        "The headquarters of UNESCO is located in:",
        "London",
        "Paris",
        "Geneva",
        "Rome",
        "Paris",
        "Easy",
    ),

    q(
        "International Relations",
        "Which group consists of Brazil, Russia, India, China and South Africa?",
        "SAARC",
        "BRICS",
        "ASEAN",
        "NATO",
        "BRICS",
        "Easy",
    ),
]

# ============================================================
# TELANGANA POLICE CONSTABLE - 50 QUESTIONS
# ============================================================

TELANGANA_POLICE_CONSTABLE_QUESTIONS = [

    # ---------------- TELANGANA HISTORY ----------------

    q(
        "Telangana History",
        "The Telangana Armed Struggle was mainly associated with opposition to which system?",
        "Zamindari system",
        "Nizam's feudal system",
        "Ryotwari system",
        "Mahalwari system",
        "Nizam's feudal system",
        "Medium",
    ),

    q(
        "Telangana History",
        "Who was the last Nizam of Hyderabad?",
        "Mir Osman Ali Khan",
        "Mir Mahboob Ali Khan",
        "Nasir-ud-Daulah",
        "Sikandar Jah",
        "Mir Osman Ali Khan",
        "Easy",
    ),

    q(
        "Telangana History",
        "Hyderabad State was integrated into the Indian Union in which year?",
        "1947",
        "1948",
        "1950",
        "1956",
        "1948",
        "Easy",
    ),

    q(
        "Telangana History",
        "Operation Polo was associated with the integration of:",
        "Mysore State",
        "Hyderabad State",
        "Madras State",
        "Bombay State",
        "Hyderabad State",
        "Medium",
    ),

    q(
        "Telangana History",
        "The Telangana region was part of which state before the formation of Telangana?",
        "Karnataka",
        "Andhra Pradesh",
        "Maharashtra",
        "Madhya Pradesh",
        "Andhra Pradesh",
        "Easy",
    ),

    q(
        "Telangana History",
        "Telangana became a separate state on:",
        "1 May 1960",
        "1 November 1956",
        "2 June 2014",
        "15 August 2014",
        "2 June 2014",
        "Easy",
    ),

    q(
        "Telangana History",
        "The States Reorganisation Act came into effect in:",
        "1948",
        "1950",
        "1956",
        "1962",
        "1956",
        "Medium",
    ),

    q(
        "Telangana History",
        "The movement for a separate Telangana state was strongly associated with the demand for:",
        "Linguistic uniformity",
        "Regional development and safeguards",
        "Merger with Karnataka",
        "Merger with Maharashtra",
        "Regional development and safeguards",
        "Medium",
    ),

    # ---------------- TELANGANA GEOGRAPHY ----------------

    q(
        "Telangana Geography",
        "Which river is one of the major rivers flowing through Telangana?",
        "Godavari",
        "Yamuna",
        "Sutlej",
        "Ravi",
        "Godavari",
        "Easy",
    ),

    q(
        "Telangana Geography",
        "Which river forms part of the southern boundary region of Telangana?",
        "Krishna",
        "Ganga",
        "Brahmaputra",
        "Mahanadi",
        "Krishna",
        "Medium",
    ),

    q(
        "Telangana Geography",
        "Which is the capital city of Telangana?",
        "Warangal",
        "Nizamabad",
        "Hyderabad",
        "Karimnagar",
        "Hyderabad",
        "Easy",
    ),

    q(
        "Telangana Geography",
        "Which district is known for the Ramappa Temple?",
        "Mulugu",
        "Medak",
        "Nalgonda",
        "Adilabad",
        "Mulugu",
        "Medium",
    ),

    q(
        "Telangana Geography",
        "The Kaleshwaram Lift Irrigation Project is associated mainly with which river?",
        "Godavari",
        "Krishna",
        "Tungabhadra",
        "Musi",
        "Godavari",
        "Medium",
    ),

    q(
        "Telangana Geography",
        "The Musi River flows through which major Telangana city?",
        "Warangal",
        "Hyderabad",
        "Nizamabad",
        "Khammam",
        "Hyderabad",
        "Easy",
    ),

    q(
        "Telangana Geography",
        "Which type of forest is widely found in parts of Telangana?",
        "Tropical dry deciduous",
        "Alpine",
        "Tundra",
        "Mangrove",
        "Tropical dry deciduous",
        "Medium",
    ),

    q(
        "Telangana Geography",
        "Which lake is located in Hyderabad and is a major urban water body?",
        "Hussain Sagar",
        "Dal Lake",
        "Chilika Lake",
        "Wular Lake",
        "Hussain Sagar",
        "Easy",
    ),

    # ---------------- TELANGANA CULTURE ----------------

    q(
        "Telangana Culture",
        "Bathukamma is a major festival associated with:",
        "Telangana",
        "Punjab",
        "Kerala",
        "Gujarat",
        "Telangana",
        "Easy",
    ),

    q(
        "Telangana Culture",
        "Bonalu is traditionally associated with worship of:",
        "Village and mother goddesses",
        "Sun god only",
        "Sea god",
        "Mountain gods only",
        "Village and mother goddesses",
        "Medium",
    ),

    q(
        "Telangana Culture",
        "Perini Shivatandavam is traditionally associated with which region?",
        "Telangana",
        "Punjab",
        "Bihar",
        "Goa",
        "Telangana",
        "Easy",
    ),

    q(
        "Telangana Culture",
        "The Ramappa Temple is also known as:",
        "Rudreshwara Temple",
        "Venkateswara Temple",
        "Brihadeeswara Temple",
        "Meenakshi Temple",
        "Rudreshwara Temple",
        "Medium",
    ),

    q(
        "Telangana Culture",
        "Which fort is located in Warangal?",
        "Warangal Fort",
        "Agra Fort",
        "Red Fort",
        "Golconda Fort",
        "Warangal Fort",
        "Easy",
    ),

    q(
        "Telangana Culture",
        "Golconda Fort is located in:",
        "Hyderabad",
        "Warangal",
        "Nalgonda",
        "Karimnagar",
        "Hyderabad",
        "Easy",
    ),

    # ---------------- POLICE / LAW ----------------

    q(
        "Police and Law",
        "The primary responsibility of the police is to:",
        "Maintain law and order",
        "Prepare the Union Budget",
        "Conduct school examinations",
        "Issue passports",
        "Maintain law and order",
        "Easy",
    ),

    q(
        "Police and Law",
        "FIR stands for:",
        "First Information Report",
        "Final Investigation Record",
        "First Investigation Rule",
        "Federal Information Report",
        "First Information Report",
        "Easy",
    ),

    q(
        "Police and Law",
        "An FIR is generally registered at a:",
        "Police station",
        "Revenue office",
        "Municipal office",
        "Post office",
        "Police station",
        "Easy",
    ),

    q(
        "Police and Law",
        "Which institution has the primary responsibility for maintaining public order at the state level?",
        "State police",
        "Election Commission",
        "Finance Commission",
        "UPSC",
        "State police",
        "Medium",
    ),

    q(
        "Police and Law",
        "The Indian Penal Code was traditionally the principal criminal law dealing with:",
        "Criminal offences",
        "Land records",
        "Tax collection",
        "Company registration",
        "Criminal offences",
        "Easy",
    ),

    q(
        "Police and Law",
        "Which branch of government interprets laws and adjudicates disputes?",
        "Executive",
        "Judiciary",
        "Legislature",
        "Election Commission",
        "Judiciary",
        "Easy",
    ),

    q(
        "Police and Law",
        "A person arrested by police has the right to be informed of:",
        "Grounds of arrest",
        "Only the police station address",
        "The officer's salary",
        "The district budget",
        "Grounds of arrest",
        "Medium",
    ),

    q(
        "Police and Law",
        "Which constitutional right protects life and personal liberty?",
        "Article 14",
        "Article 19",
        "Article 21",
        "Article 32",
        "Article 21",
        "Easy",
    ),

    # ---------------- INDIAN POLITY ----------------

    q(
        "Indian Polity",
        "Who is the constitutional head of a state?",
        "Chief Minister",
        "Governor",
        "Chief Secretary",
        "Speaker",
        "Governor",
        "Easy",
    ),

    q(
        "Indian Polity",
        "The Council of Ministers in a state is headed by the:",
        "Governor",
        "Chief Minister",
        "Speaker",
        "Chief Justice",
        "Chief Minister",
        "Easy",
    ),

    q(
        "Indian Polity",
        "Fundamental Duties were added to the Constitution by which amendment?",
        "42nd Amendment",
        "44th Amendment",
        "52nd Amendment",
        "73rd Amendment",
        "42nd Amendment",
        "Medium",
    ),

    q(
        "Indian Polity",
        "Which Article guarantees freedom of speech and expression subject to constitutional restrictions?",
        "Article 14",
        "Article 19",
        "Article 21",
        "Article 25",
        "Article 19",
        "Medium",
    ),

    q(
        "Indian Polity",
        "Which body is the highest court in India?",
        "High Court",
        "Supreme Court",
        "District Court",
        "Sessions Court",
        "Supreme Court",
        "Easy",
    ),

    q(
        "Indian Polity",
        "The Governor of a state is appointed by the:",
        "Prime Minister",
        "President",
        "Chief Minister",
        "State Legislature",
        "President",
        "Easy",
    ),

    # ---------------- GENERAL SCIENCE ----------------

    q(
        "General Science",
        "Which blood group is commonly called the universal donor for red blood cells?",
        "AB positive",
        "O negative",
        "A positive",
        "B negative",
        "O negative",
        "Medium",
    ),

    q(
        "General Science",
        "Which vitamin is important for blood clotting?",
        "Vitamin A",
        "Vitamin C",
        "Vitamin K",
        "Vitamin D",
        "Vitamin K",
        "Medium",
    ),

    q(
        "General Science",
        "Which part of the human brain controls balance and coordination?",
        "Cerebrum",
        "Cerebellum",
        "Medulla",
        "Hypothalamus",
        "Cerebellum",
        "Medium",
    ),

    q(
        "General Science",
        "Which gas is required for normal human respiration?",
        "Nitrogen",
        "Oxygen",
        "Carbon dioxide",
        "Hydrogen",
        "Oxygen",
        "Easy",
    ),

    q(
        "General Science",
        "What is the SI unit of force?",
        "Joule",
        "Newton",
        "Pascal",
        "Watt",
        "Newton",
        "Easy",
    ),

    q(
        "General Science",
        "Which instrument is used to measure atmospheric pressure?",
        "Thermometer",
        "Barometer",
        "Hygrometer",
        "Ammeter",
        "Barometer",
        "Easy",
    ),

    # ---------------- REASONING ----------------

    q(
        "Reasoning",
        "Find the next number: 2, 6, 12, 20, 30, ?",
        "36",
        "40",
        "42",
        "44",
        "42",
        "Medium",
    ),

    q(
        "Reasoning",
        "If POLICE is coded as QPMJDF by shifting each letter one position forward, how is LAW coded?",
        "MBX",
        "LBX",
        "MBW",
        "KZW",
        "MBX",
        "Medium",
    ),

    q(
        "Reasoning",
        "A person walks 5 km north and then 5 km east. In which direction is the person from the starting point?",
        "North-west",
        "North-east",
        "South-east",
        "South-west",
        "North-east",
        "Easy",
    ),

    q(
        "Reasoning",
        "Find the odd one out.",
        "Police",
        "Army",
        "Navy",
        "Hospital",
        "Hospital",
        "Easy",
    ),

    # ---------------- BASIC ARITHMETIC ----------------

    q(
        "Arithmetic",
        "A police vehicle travels 180 km in 3 hours. What is its average speed?",
        "40 km/h",
        "50 km/h",
        "60 km/h",
        "70 km/h",
        "60 km/h",
        "Easy",
    ),

    q(
        "Arithmetic",
        "What is 20% of 750?",
        "100",
        "125",
        "150",
        "175",
        "150",
        "Easy",
    ),

    q(
        "Arithmetic",
        "A number is increased from 200 to 250. What is the percentage increase?",
        "20%",
        "25%",
        "30%",
        "35%",
        "25%",
        "Medium",
    ),

    q(
        "Arithmetic",
        "If a constable saves ₹2,000 per month, how much will be saved in 12 months?",
        "₹20,000",
        "₹22,000",
        "₹24,000",
        "₹26,000",
        "₹24,000",
        "Easy",
    ),
]

# ============================================================
# UPSC CSE - 50 UNIQUE QUESTIONS
# ============================================================

UPSC_CSE_QUESTIONS = [

    # ---------------- INDIAN POLITY ----------------

    q(
        "Indian Polity",
        "Which part of the Constitution contains the Directive Principles of State Policy?",
        "Part II",
        "Part III",
        "Part IV",
        "Part V",
        "Part IV",
        "Easy",
    ),

    q(
        "Indian Polity",
        "The concept of judicial review in India is primarily borrowed from which country?",
        "United Kingdom",
        "United States",
        "Canada",
        "Australia",
        "United States",
        "Medium",
    ),

    q(
        "Indian Polity",
        "Who decides whether a Bill is a Money Bill in the Lok Sabha?",
        "President",
        "Prime Minister",
        "Speaker of Lok Sabha",
        "Finance Minister",
        "Speaker of Lok Sabha",
        "Medium",
    ),

    q(
        "Indian Polity",
        "Which constitutional amendment introduced Panchayati Raj institutions?",
        "42nd Amendment",
        "61st Amendment",
        "73rd Amendment",
        "86th Amendment",
        "73rd Amendment",
        "Easy",
    ),

    q(
        "Indian Polity",
        "The Rajya Sabha is a permanent House because:",
        "It cannot be dissolved",
        "Its members have lifetime tenure",
        "It has no elections",
        "Its members are appointed by the President only",
        "It cannot be dissolved",
        "Easy",
    ),

    q(
        "Indian Polity",
        "Which authority audits the accounts of the Union and State governments?",
        "Finance Commission",
        "Comptroller and Auditor General",
        "Election Commission",
        "NITI Aayog",
        "Comptroller and Auditor General",
        "Easy",
    ),

    q(
        "Indian Polity",
        "The power of the President to promulgate an Ordinance is provided under:",
        "Article 72",
        "Article 123",
        "Article 143",
        "Article 356",
        "Article 123",
        "Medium",
    ),

    q(
        "Indian Polity",
        "Which schedule of the Constitution deals with allocation of seats in the Rajya Sabha?",
        "Fourth Schedule",
        "Fifth Schedule",
        "Sixth Schedule",
        "Seventh Schedule",
        "Fourth Schedule",
        "Medium",
    ),

    # ---------------- MODERN HISTORY ----------------

    q(
        "Modern History",
        "The Permanent Settlement was introduced by:",
        "Lord Cornwallis",
        "Lord Wellesley",
        "Lord Dalhousie",
        "Lord Curzon",
        "Lord Cornwallis",
        "Easy",
    ),

    q(
        "Modern History",
        "The Doctrine of Lapse was most closely associated with:",
        "Lord Ripon",
        "Lord Dalhousie",
        "Lord Canning",
        "Lord Curzon",
        "Lord Dalhousie",
        "Easy",
    ),

    q(
        "Modern History",
        "The Swadeshi Movement began primarily as a response to:",
        "Rowlatt Act",
        "Partition of Bengal",
        "Simon Commission",
        "Government of India Act",
        "Partition of Bengal",
        "Easy",
    ),

    q(
        "Modern History",
        "The Home Rule Movement in India was associated with Annie Besant and:",
        "Bal Gangadhar Tilak",
        "Dadabhai Naoroji",
        "Gopal Krishna Gokhale",
        "Lala Lajpat Rai",
        "Bal Gangadhar Tilak",
        "Medium",
    ),

    q(
        "Modern History",
        "The Champaran Satyagraha was mainly related to:",
        "Cotton cultivation",
        "Indigo cultivation",
        "Tea cultivation",
        "Wheat cultivation",
        "Indigo cultivation",
        "Easy",
    ),

    q(
        "Modern History",
        "The Cabinet Mission came to India in:",
        "1942",
        "1945",
        "1946",
        "1947",
        "1946",
        "Easy",
    ),

    q(
        "Modern History",
        "The Indian National Congress was founded in:",
        "1885",
        "1890",
        "1905",
        "1911",
        "1885",
        "Easy",
    ),

    q(
        "Modern History",
        "Who founded the Servants of India Society?",
        "Gopal Krishna Gokhale",
        "Bal Gangadhar Tilak",
        "Madan Mohan Malaviya",
        "Surendranath Banerjee",
        "Gopal Krishna Gokhale",
        "Medium",
    ),

    # ---------------- ANCIENT & MEDIEVAL HISTORY ----------------

    q(
        "Ancient History",
        "Which Harappan site is located in present-day Gujarat?",
        "Lothal",
        "Taxila",
        "Sanchi",
        "Nalanda",
        "Lothal",
        "Easy",
    ),

    q(
        "Ancient History",
        "The Sangam literature is mainly associated with which language?",
        "Sanskrit",
        "Tamil",
        "Pali",
        "Prakrit",
        "Tamil",
        "Easy",
    ),

    q(
        "Ancient History",
        "Ashoka belonged to which dynasty?",
        "Gupta",
        "Maurya",
        "Kushan",
        "Satavahana",
        "Maurya",
        "Easy",
    ),

    q(
        "Medieval History",
        "The Vijayanagara Empire was founded by:",
        "Harihara and Bukka",
        "Krishnadevaraya and Bukka",
        "Alauddin Khilji and Malik Kafur",
        "Rana Sanga and Prithviraj",
        "Harihara and Bukka",
        "Medium",
    ),

    q(
        "Medieval History",
        "Who wrote the Akbarnama?",
        "Abul Fazl",
        "Badauni",
        "Amir Khusrau",
        "Al-Biruni",
        "Abul Fazl",
        "Easy",
    ),

    q(
        "Medieval History",
        "The Bhakti movement emphasized:",
        "Military expansion",
        "Devotion to God",
        "Trade regulation",
        "Land revenue collection",
        "Devotion to God",
        "Easy",
    ),

    # ---------------- INDIAN GEOGRAPHY ----------------

    q(
        "Geography",
        "The Western Ghats are also known as:",
        "Sahyadri",
        "Aravalli",
        "Shivalik",
        "Nilgiri",
        "Sahyadri",
        "Easy",
    ),

    q(
        "Geography",
        "Which river is known as the 'Sorrow of Bihar'?",
        "Kosi",
        "Son",
        "Gandak",
        "Ghaghara",
        "Kosi",
        "Easy",
    ),

    q(
        "Geography",
        "Black soil is particularly suitable for growing:",
        "Rice",
        "Cotton",
        "Tea",
        "Jute",
        "Cotton",
        "Easy",
    ),

    q(
        "Geography",
        "The Coriolis force is caused by:",
        "Revolution of Earth",
        "Rotation of Earth",
        "Gravity of Moon",
        "Solar radiation",
        "Rotation of Earth",
        "Medium",
    ),

    q(
        "Geography",
        "Which Indian state has the longest coastline?",
        "Tamil Nadu",
        "Gujarat",
        "Andhra Pradesh",
        "Maharashtra",
        "Gujarat",
        "Easy",
    ),

    q(
        "Geography",
        "The Tropic of Cancer passes through how many Indian states?",
        "6",
        "7",
        "8",
        "9",
        "8",
        "Medium",
    ),

    # ---------------- ECONOMY ----------------

    q(
        "Indian Economy",
        "GDP measures the monetary value of:",
        "Only agricultural output",
        "Final goods and services produced within an economy",
        "Only exports",
        "Government expenditure only",
        "Final goods and services produced within an economy",
        "Medium",
    ),

    q(
        "Indian Economy",
        "Inflation refers to:",
        "A fall in general price levels",
        "A sustained rise in general price levels",
        "A rise in exports only",
        "A fall in money supply only",
        "A sustained rise in general price levels",
        "Easy",
    ),

    q(
        "Indian Economy",
        "Which institution is responsible for monetary policy in India?",
        "SEBI",
        "RBI",
        "NITI Aayog",
        "Finance Commission",
        "RBI",
        "Easy",
    ),

    q(
        "Indian Economy",
        "Fiscal policy primarily deals with:",
        "Money supply and interest rates",
        "Government revenue and expenditure",
        "Foreign exchange only",
        "Bank licensing",
        "Government revenue and expenditure",
        "Medium",
    ),

    q(
        "Indian Economy",
        "What does GST stand for?",
        "General Sales Tax",
        "Goods and Services Tax",
        "Government Service Tax",
        "Goods Supply Tariff",
        "Goods and Services Tax",
        "Easy",
    ),

    q(
        "Indian Economy",
        "Which institution replaced the Planning Commission?",
        "Finance Commission",
        "NITI Aayog",
        "RBI",
        "SEBI",
        "NITI Aayog",
        "Easy",
    ),

    # ---------------- ENVIRONMENT ----------------

    q(
        "Environment",
        "The Ramsar Convention is associated with conservation of:",
        "Mountains",
        "Wetlands",
        "Deserts",
        "Grasslands",
        "Wetlands",
        "Easy",
    ),

    q(
        "Environment",
        "Which gas is a major contributor to the enhanced greenhouse effect?",
        "Oxygen",
        "Carbon dioxide",
        "Nitrogen",
        "Argon",
        "Carbon dioxide",
        "Easy",
    ),

    q(
        "Environment",
        "The term biodiversity refers to:",
        "Only plant species",
        "Only animal species",
        "Variety of life at different levels",
        "Only microorganisms",
        "Variety of life at different levels",
        "Medium",
    ),

    q(
        "Environment",
        "A species found naturally only in a particular geographical area is called:",
        "Migratory",
        "Endemic",
        "Invasive",
        "Cosmopolitan",
        "Endemic",
        "Easy",
    ),

    q(
        "Environment",
        "Project Tiger was launched in India in:",
        "1965",
        "1973",
        "1980",
        "1986",
        "1973",
        "Easy",
    ),

    q(
        "Environment",
        "The ozone layer is mainly present in the:",
        "Troposphere",
        "Stratosphere",
        "Mesosphere",
        "Thermosphere",
        "Stratosphere",
        "Medium",
    ),

    # ---------------- SCIENCE & TECHNOLOGY ----------------

    q(
        "Science and Technology",
        "DNA is primarily responsible for:",
        "Energy production only",
        "Storage of genetic information",
        "Blood circulation",
        "Digestion",
        "Storage of genetic information",
        "Easy",
    ),

    q(
        "Science and Technology",
        "CRISPR technology is primarily associated with:",
        "Gene editing",
        "Satellite navigation",
        "Weather forecasting",
        "Nuclear fusion",
        "Gene editing",
        "Medium",
    ),

    q(
        "Science and Technology",
        "A geostationary satellite appears stationary because it:",
        "Does not rotate",
        "Has an orbital period equal to Earth's rotation",
        "Orbits the Moon",
        "Has no gravitational force",
        "Has an orbital period equal to Earth's rotation",
        "Medium",
    ),

    q(
        "Science and Technology",
        "Which Indian organisation is responsible for the country's space programme?",
        "DRDO",
        "ISRO",
        "CSIR",
        "BARC",
        "ISRO",
        "Easy",
    ),

    q(
        "Science and Technology",
        "Artificial intelligence primarily involves machines performing tasks that normally require:",
        "Only physical strength",
        "Human-like cognitive abilities",
        "Only mechanical work",
        "Only mathematical calculations",
        "Human-like cognitive abilities",
        "Medium",
    ),

    # ---------------- GOVERNANCE ----------------

    q(
        "Governance",
        "Social auditing is primarily intended to promote:",
        "Military preparedness",
        "Transparency and accountability",
        "Foreign trade",
        "Monetary stability",
        "Transparency and accountability",
        "Medium",
    ),

    q(
        "Governance",
        "The Right to Information Act primarily promotes:",
        "Government secrecy",
        "Transparency in public administration",
        "Military recruitment",
        "Judicial appointments",
        "Transparency in public administration",
        "Easy",
    ),

    q(
        "Governance",
        "E-governance refers to the use of information technology in:",
        "Government services and administration",
        "Agricultural production only",
        "Military operations only",
        "Private banking only",
        "Government services and administration",
        "Easy",
    ),

    q(
        "Governance",
        "The principle of decentralisation means:",
        "Concentration of power at the centre",
        "Transfer of powers to lower levels of government",
        "Abolition of local government",
        "Privatisation of government",
        "Transfer of powers to lower levels of government",
        "Medium",
    ),

    q(
        "Governance",
        "Which institution is primarily responsible for conducting elections to Parliament and state legislatures?",
        "Union Public Service Commission",
        "Election Commission of India",
        "Finance Commission",
        "Comptroller and Auditor General",
        "Election Commission of India",
        "Easy",
    ),

    # ---------------- INTERNATIONAL RELATIONS ----------------

    q(
        "International Relations",
        "The United Nations Security Council has how many permanent members?",
        "3",
        "4",
        "5",
        "6",
        "5",
        "Easy",
    ),

    q(
        "International Relations",
        "Which organisation is primarily concerned with international public health?",
        "WHO",
        "WTO",
        "ILO",
        "UNESCO",
        "WHO",
        "Easy",
    ),

    q(
        "International Relations",
        "The headquarters of the World Trade Organization is in:",
        "New York",
        "Geneva",
        "Paris",
        "London",
        "Geneva",
        "Easy",
    ),

    q(
        "International Relations",
        "ASEAN is a regional organisation of countries in:",
        "South America",
        "Southeast Asia",
        "West Asia",
        "Eastern Europe",
        "Southeast Asia",
        "Easy",
    ),

    # ---------------- ETHICS / APTITUDE ----------------

    q(
        "Ethics",
        "Integrity in public administration primarily means:",
        "Avoiding all decisions",
        "Consistency between ethical principles and actions",
        "Following orders without question",
        "Keeping information secret",
        "Consistency between ethical principles and actions",
        "Medium",
    ),

    q(
        "Ethics",
        "A conflict of interest occurs when:",
        "A person has no responsibilities",
        "Personal interests may improperly influence official duties",
        "An officer changes departments",
        "A citizen files an application",
        "Personal interests may improperly influence official duties",
        "Medium",
    ),

    q(
        "Ethics",
        "Empathy means:",
        "Ignoring others' feelings",
        "Understanding another person's feelings and perspective",
        "Always agreeing with others",
        "Avoiding communication",
        "Understanding another person's feelings and perspective",
        "Easy",
    ),
]

TELANGANA_POLICE_SI_QUESTIONS = [

    q(
        "Telangana Police SI - Polity",
        "Which Article of the Indian Constitution guarantees equality before law?",
        "Article 12",
        "Article 14",
        "Article 16",
        "Article 19",
        "Article 14",
    ),

    q(
        "Telangana Police SI - Polity",
        "The Fundamental Duties were added to the Indian Constitution by which Amendment?",
        "42nd Amendment",
        "44th Amendment",
        "52nd Amendment",
        "73rd Amendment",
        "42nd Amendment",
    ),

    q(
        "Telangana Police SI - Polity",
        "Who is the constitutional head of a state?",
        "Chief Minister",
        "Governor",
        "Chief Secretary",
        "Speaker",
        "Governor",
    ),

    q(
        "Telangana Police SI - Polity",
        "Who appoints the Governor of an Indian state?",
        "Chief Minister",
        "President of India",
        "Prime Minister",
        "State Legislature",
        "President of India",
    ),

    q(
        "Telangana Police SI - Polity",
        "Which Article deals with the Right to Constitutional Remedies?",
        "Article 19",
        "Article 21",
        "Article 32",
        "Article 44",
        "Article 32",
    ),

    q(
        "Telangana Police SI - Polity",
        "Who is the Supreme Commander of the Armed Forces of India?",
        "Prime Minister",
        "Defence Minister",
        "President",
        "Chief of Defence Staff",
        "President",
    ),

    q(
        "Telangana Police SI - Polity",
        "Which body conducts elections to the Parliament and State Legislatures?",
        "UPSC",
        "Election Commission of India",
        "Finance Commission",
        "NITI Aayog",
        "Election Commission of India",
    ),

    q(
        "Telangana Police SI - Polity",
        "The minimum age required to become a member of the Lok Sabha is:",
        "18 years",
        "21 years",
        "25 years",
        "30 years",
        "25 years",
    ),

    q(
        "Telangana Police SI - Polity",
        "Which institution is known as the guardian of the Constitution?",
        "Parliament",
        "Supreme Court",
        "President",
        "Election Commission",
        "Supreme Court",
    ),

    q(
        "Telangana Police SI - Polity",
        "Who presides over the Rajya Sabha?",
        "President",
        "Prime Minister",
        "Vice-President",
        "Speaker of Lok Sabha",
        "Vice-President",
    ),

    q(
        "Telangana Police SI - Telangana",
        "Telangana became a separate state on:",
        "1 January 2014",
        "2 June 2014",
        "15 August 2014",
        "1 November 2014",
        "2 June 2014",
    ),

    q(
        "Telangana Police SI - Telangana",
        "What is the capital of Telangana?",
        "Warangal",
        "Karimnagar",
        "Hyderabad",
        "Nizamabad",
        "Hyderabad",
    ),

    q(
        "Telangana Police SI - Telangana",
        "Which river flows through Hyderabad?",
        "Godavari",
        "Krishna",
        "Musi",
        "Manjira",
        "Musi",
    ),

    q(
        "Telangana Police SI - Telangana",
        "Which is the major river associated with northern Telangana?",
        "Godavari",
        "Musi",
        "Tungabhadra",
        "Pennar",
        "Godavari",
    ),

    q(
        "Telangana Police SI - Telangana",
        "Bathukamma is a famous festival of:",
        "Andhra Pradesh",
        "Telangana",
        "Karnataka",
        "Odisha",
        "Telangana",
    ),

    q(
        "Telangana Police SI - Telangana",
        "The Ramappa Temple is located in which district of Telangana?",
        "Mulugu",
        "Adilabad",
        "Nalgonda",
        "Medak",
        "Mulugu",
    ),

    q(
        "Telangana Police SI - Telangana",
        "Which city is known as the City of Pearls?",
        "Warangal",
        "Hyderabad",
        "Khammam",
        "Nizamabad",
        "Hyderabad",
    ),

    q(
        "Telangana Police SI - Telangana",
        "The Kaleshwaram project is mainly associated with which river?",
        "Krishna",
        "Godavari",
        "Musi",
        "Tungabhadra",
        "Godavari",
    ),

    q(
        "Telangana Police SI - Telangana",
        "Which movement played an important role in the formation of Telangana?",
        "Telangana Statehood Movement",
        "Swadeshi Movement",
        "Quit India Movement",
        "Chipko Movement",
        "Telangana Statehood Movement",
    ),

    q(
        "Telangana Police SI - Telangana",
        "Which traditional dance form is strongly associated with Telangana?",
        "Perini Shivatandavam",
        "Kathakali",
        "Bharatanatyam",
        "Mohiniyattam",
        "Perini Shivatandavam",
    ),

    q(
        "Telangana Police SI - Law",
        "Which principle means that a person is considered innocent until proven guilty?",
        "Rule of majority",
        "Presumption of innocence",
        "Natural justice",
        "Double jeopardy",
        "Presumption of innocence",
    ),

    q(
        "Telangana Police SI - Law",
        "What is the main purpose of criminal law?",
        "To regulate contracts",
        "To punish offences and protect society",
        "To regulate marriages",
        "To collect taxes",
        "To punish offences and protect society",
    ),

    q(
        "Telangana Police SI - Law",
        "Which authority generally registers an FIR for a cognizable offence?",
        "Police station",
        "Civil court",
        "Revenue office",
        "Municipal office",
        "Police station",
    ),

    q(
        "Telangana Police SI - Law",
        "FIR stands for:",
        "First Investigation Report",
        "First Information Report",
        "Final Information Record",
        "First Incident Record",
        "First Information Report",
    ),

    q(
        "Telangana Police SI - Law",
        "A cognizable offence generally permits police to:",
        "Arrest without warrant under law",
        "Never investigate",
        "Only issue a fine",
        "Only file a civil suit",
        "Arrest without warrant under law",
    ),

    q(
        "Telangana Police SI - Law",
        "Which principle protects a person from being tried twice for the same offence?",
        "Natural justice",
        "Double jeopardy",
        "Rule of law",
        "Judicial review",
        "Double jeopardy",
    ),

    q(
        "Telangana Police SI - Law",
        "What is bail?",
        "Permanent release from all charges",
        "Temporary release of an accused subject to conditions",
        "Acquittal by police",
        "Cancellation of an FIR",
        "Temporary release of an accused subject to conditions",
    ),

    q(
        "Telangana Police SI - Law",
        "Which branch of government interprets laws?",
        "Executive",
        "Legislature",
        "Judiciary",
        "Election Commission",
        "Judiciary",
    ),

    q(
        "Telangana Police SI - Law",
        "Natural justice primarily aims to ensure:",
        "Fairness in decision-making",
        "Higher taxation",
        "Political campaigning",
        "Administrative secrecy",
        "Fairness in decision-making",
    ),

    q(
        "Telangana Police SI - Law",
        "Which writ is commonly used to produce a person who is unlawfully detained?",
        "Mandamus",
        "Habeas Corpus",
        "Certiorari",
        "Quo Warranto",
        "Habeas Corpus",
    ),

    q(
        "Telangana Police SI - Reasoning",
        "Find the next number: 4, 8, 16, 32, ?",
        "48",
        "56",
        "64",
        "72",
        "64",
    ),

    q(
        "Telangana Police SI - Reasoning",
        "Find the odd one out.",
        "Police",
        "Army",
        "Navy",
        "Mango",
        "Mango",
    ),

    q(
        "Telangana Police SI - Reasoning",
        "If POLICE is coded as QPMJDF, then each letter is shifted by:",
        "One position forward",
        "Two positions forward",
        "One position backward",
        "Three positions forward",
        "One position forward",
    ),

    q(
        "Telangana Police SI - Reasoning",
        "A person walks 5 km north and then 5 km east. In which direction is he from the starting point?",
        "North-west",
        "North-east",
        "South-east",
        "South-west",
        "North-east",
    ),

    q(
        "Telangana Police SI - Reasoning",
        "If all policemen are disciplined and Ravi is a policeman, then Ravi is:",
        "Undisciplined",
        "Disciplined",
        "A civilian",
        "A judge",
        "Disciplined",
    ),

    q(
        "Telangana Police SI - Reasoning",
        "Complete the series: 7, 14, 21, 28, ?",
        "32",
        "35",
        "36",
        "42",
        "35",
    ),

    q(
        "Telangana Police SI - Reasoning",
        "If SOUTH is written as HTUOS, the word is:",
        "Encrypted",
        "Written in reverse order",
        "Written alphabetically",
        "Translated",
        "Written in reverse order",
    ),

    q(
        "Telangana Police SI - Reasoning",
        "A is the brother of B. B is the sister of C. How is A related to C?",
        "Father",
        "Brother",
        "Uncle",
        "Cousin",
        "Brother",
    ),

    q(
        "Telangana Police SI - Reasoning",
        "Which number does not belong to the group?",
        "9",
        "16",
        "25",
        "30",
        "30",
    ),

    q(
        "Telangana Police SI - Reasoning",
        "Complete the analogy: Police : Law :: Doctor : ?",
        "Court",
        "Medicine",
        "School",
        "Agriculture",
        "Medicine",
    ),

    q(
        "Telangana Police SI - General Science",
        "Which part of the human brain controls balance and coordination?",
        "Cerebrum",
        "Cerebellum",
        "Medulla",
        "Hypothalamus",
        "Cerebellum",
    ),

    q(
        "Telangana Police SI - General Science",
        "Which blood group is known as the universal donor for red blood cells?",
        "AB positive",
        "A positive",
        "O negative",
        "B negative",
        "O negative",
    ),

    q(
        "Telangana Police SI - General Science",
        "Which vitamin is important for blood clotting?",
        "Vitamin A",
        "Vitamin C",
        "Vitamin D",
        "Vitamin K",
        "Vitamin K",
    ),

    q(
        "Telangana Police SI - General Science",
        "Which gas is essential for human respiration?",
        "Nitrogen",
        "Oxygen",
        "Carbon dioxide",
        "Hydrogen",
        "Oxygen",
    ),

    q(
        "Telangana Police SI - General Science",
        "Which instrument is used to measure blood pressure?",
        "Thermometer",
        "Barometer",
        "Sphygmomanometer",
        "Hygrometer",
        "Sphygmomanometer",
    ),

    q(
        "Telangana Police SI - General Science",
        "What is the normal approximate human body temperature?",
        "35°C",
        "37°C",
        "39°C",
        "42°C",
        "37°C",
    ),

    q(
        "Telangana Police SI - General Science",
        "Which disease is caused by deficiency of Vitamin C?",
        "Rickets",
        "Scurvy",
        "Beriberi",
        "Night blindness",
        "Scurvy",
    ),

    q(
        "Telangana Police SI - General Science",
        "Which organ removes waste products from the blood?",
        "Heart",
        "Kidney",
        "Lungs",
        "Stomach",
        "Kidney",
    ),

    q(
        "Telangana Police SI - General Science",
        "Which microorganism is used in the production of curd?",
        "Virus",
        "Lactobacillus",
        "Protozoa",
        "Algae",
        "Lactobacillus",
    ),

    q(
        "Telangana Police SI - General Science",
        "Which type of energy is stored in food?",
        "Chemical energy",
        "Sound energy",
        "Light energy",
        "Nuclear energy",
        "Chemical energy",
    ),

    q(
        "Telangana Police SI - Current Affairs",
        "Which institution is responsible for maintaining monetary stability in India?",
        "SEBI",
        "RBI",
        "NITI Aayog",
        "UPSC",
        "RBI",
    ),

    q(
        "Telangana Police SI - General Awareness",
        "Which organisation is responsible for investigating major cases of corruption and certain economic offences in India?",
        "CBI",
        "ISRO",
        "DRDO",
        "UGC",
        "CBI",
    ),
]

TELANGANA_AE_QUESTIONS = [

    q(
        "Civil Engineering",
        "Which property of cement is primarily responsible for its ability to bind aggregates together?",
        "Fineness",
        "Cementing property",
        "Soundness",
        "Colour",
        "Cementing property",
    ),

    q(
        "Civil Engineering",
        "The initial setting time of ordinary Portland cement should not be less than:",
        "10 minutes",
        "30 minutes",
        "60 minutes",
        "120 minutes",
        "30 minutes",
    ),

    q(
        "Civil Engineering",
        "Which test is commonly used to determine the workability of fresh concrete?",
        "Slump test",
        "Los Angeles test",
        "Proctor test",
        "CBR test",
        "Slump test",
    ),

    q(
        "Civil Engineering",
        "The characteristic compressive strength of concrete is generally measured after:",
        "3 days",
        "7 days",
        "14 days",
        "28 days",
        "28 days",
    ),

    q(
        "Civil Engineering",
        "Which aggregate property is most important for resisting wear in road construction?",
        "Abrasion resistance",
        "Colour",
        "Shape only",
        "Moisture content",
        "Abrasion resistance",
    ),

    q(
        "Civil Engineering",
        "The main purpose of providing reinforcement in reinforced concrete beams is to resist:",
        "Tension",
        "Temperature only",
        "Dead load only",
        "Shrinkage only",
        "Tension",
    ),

    q(
        "Civil Engineering",
        "A simply supported beam primarily develops which reactions at its supports?",
        "Axial reactions only",
        "Vertical and horizontal reactions depending on loading",
        "Torsional reactions only",
        "No reactions",
        "Vertical and horizontal reactions depending on loading",
    ),

    q(
        "Civil Engineering",
        "The unit of Young's modulus is:",
        "N",
        "N/m",
        "N/m²",
        "m/N",
        "N/m²",
    ),

    q(
        "Civil Engineering",
        "Which soil has the highest permeability among the following?",
        "Clay",
        "Silt",
        "Sand",
        "Organic soil",
        "Sand",
    ),

    q(
        "Civil Engineering",
        "The water content at which a soil changes from plastic state to liquid state is called:",
        "Shrinkage limit",
        "Plastic limit",
        "Liquid limit",
        "Optimum moisture content",
        "Liquid limit",
    ),

    q(
        "Civil Engineering",
        "The Standard Proctor test is used to determine:",
        "Soil permeability",
        "Soil compaction characteristics",
        "Bearing capacity directly",
        "Shear strength only",
        "Soil compaction characteristics",
    ),

    q(
        "Civil Engineering",
        "CBR test is mainly associated with the design of:",
        "Concrete buildings",
        "Flexible pavements",
        "Steel bridges",
        "Water tanks",
        "Flexible pavements",
    ),

    q(
        "Civil Engineering",
        "Which instrument is commonly used for measuring horizontal and vertical angles in surveying?",
        "Theodolite",
        "Planimeter",
        "Rain gauge",
        "Barometer",
        "Theodolite",
    ),

    q(
        "Civil Engineering",
        "A contour line joins points having the same:",
        "Temperature",
        "Elevation",
        "Pressure",
        "Distance",
        "Elevation",
    ),

    q(
        "Civil Engineering",
        "The process of determining the difference in elevation between points is called:",
        "Levelling",
        "Chaining",
        "Traversing",
        "Triangulation",
        "Levelling",
    ),

    q(
        "Civil Engineering",
        "Which type of foundation is generally suitable when the soil bearing capacity near the surface is low?",
        "Deep foundation",
        "Isolated footing only",
        "Strip footing only",
        "Wall footing only",
        "Deep foundation",
    ),

    q(
        "Civil Engineering",
        "Which structural member primarily carries axial compressive load?",
        "Column",
        "Slab",
        "Lintel",
        "Floor finish",
        "Column",
    ),

    q(
        "Civil Engineering",
        "The ratio of lateral strain to longitudinal strain is known as:",
        "Young's modulus",
        "Poisson's ratio",
        "Bulk modulus",
        "Shear modulus",
        "Poisson's ratio",
    ),

    q(
        "Civil Engineering",
        "Which test is used to determine the impact strength of road aggregates?",
        "Aggregate impact test",
        "Slump test",
        "Vee-Bee test",
        "Proctor test",
        "Aggregate impact test",
    ),

    q(
        "Civil Engineering",
        "Bitumen is primarily used in flexible pavement as a:",
        "Binder",
        "Filler",
        "Coarse aggregate",
        "Subgrade soil",
        "Binder",
    ),

    q(
        "Electrical Engineering",
        "According to Ohm's law, voltage is equal to:",
        "IR",
        "I/R",
        "R/I",
        "I + R",
        "IR",
    ),

    q(
        "Electrical Engineering",
        "The SI unit of electrical resistance is:",
        "Volt",
        "Ampere",
        "Ohm",
        "Watt",
        "Ohm",
    ),

    q(
        "Electrical Engineering",
        "An electrical transformer operates on the principle of:",
        "Electromagnetic induction",
        "Electrolysis",
        "Static friction",
        "Thermal expansion",
        "Electromagnetic induction",
    ),

    q(
        "Electrical Engineering",
        "A transformer generally cannot operate on:",
        "AC supply",
        "DC supply",
        "Alternating voltage",
        "Sinusoidal AC",
        "DC supply",
    ),

    q(
        "Electrical Engineering",
        "The power factor of a purely resistive AC circuit is:",
        "0",
        "0.5",
        "1",
        "2",
        "1",
    ),

    q(
        "Electrical Engineering",
        "Which instrument is used to measure electric current?",
        "Voltmeter",
        "Ammeter",
        "Wattmeter",
        "Ohmmeter",
        "Ammeter",
    ),

    q(
        "Electrical Engineering",
        "Which instrument measures electrical power?",
        "Ammeter",
        "Voltmeter",
        "Wattmeter",
        "Galvanometer",
        "Wattmeter",
    ),

    q(
        "Electrical Engineering",
        "The unit of electrical power is:",
        "Joule",
        "Watt",
        "Ohm",
        "Coulomb",
        "Watt",
    ),

    q(
        "Electrical Engineering",
        "In a three-phase balanced system, the phase difference between two phases is:",
        "60°",
        "90°",
        "120°",
        "180°",
        "120°",
    ),

    q(
        "Electrical Engineering",
        "Which device protects an electrical circuit from excessive current?",
        "Fuse",
        "Transformer",
        "Capacitor",
        "Resistor",
        "Fuse",
    ),

    q(
        "Electrical Engineering",
        "The speed of a DC motor can be controlled by varying:",
        "Armature voltage",
        "Colour of winding",
        "Frequency of sunlight",
        "Mechanical weight only",
        "Armature voltage",
    ),

    q(
        "Electrical Engineering",
        "Which material is commonly used as a conductor in electrical wiring?",
        "Copper",
        "Rubber",
        "Glass",
        "Wood",
        "Copper",
    ),

    q(
        "Electrical Engineering",
        "A capacitor stores electrical energy in the form of:",
        "Magnetic field",
        "Electric field",
        "Heat only",
        "Sound",
        "Electric field",
    ),

    q(
        "Electrical Engineering",
        "The unit of capacitance is:",
        "Henry",
        "Farad",
        "Tesla",
        "Weber",
        "Farad",
    ),

    q(
        "Electrical Engineering",
        "The unit of inductance is:",
        "Farad",
        "Henry",
        "Ohm",
        "Volt",
        "Henry",
    ),

    q(
        "Engineering Mathematics",
        "What is the derivative of x² with respect to x?",
        "x",
        "2x",
        "x²",
        "2",
        "2x",
    ),

    q(
        "Engineering Mathematics",
        "What is the integral of 1 with respect to x?",
        "1",
        "x",
        "x²",
        "0",
        "x",
    ),

    q(
        "Engineering Mathematics",
        "The value of sin 90° is:",
        "0",
        "1/2",
        "1",
        "√3/2",
        "1",
    ),

    q(
        "Engineering Mathematics",
        "The value of cos 0° is:",
        "0",
        "1",
        "-1",
        "1/2",
        "1",
    ),

    q(
        "Engineering Mathematics",
        "If A = 2 and B = 3, then A² + B² is:",
        "10",
        "11",
        "12",
        "13",
        "13",
    ),

    q(
        "Engineering Mathematics",
        "What is the determinant of the matrix [[1, 2], [3, 4]]?",
        "-2",
        "2",
        "4",
        "10",
        "-2",
    ),

    q(
        "Engineering Mathematics",
        "The sum of the angles of a triangle is:",
        "90°",
        "180°",
        "270°",
        "360°",
        "180°",
    ),

    q(
        "General Engineering",
        "Which law states that energy cannot be created or destroyed?",
        "Newton's first law",
        "Law of conservation of energy",
        "Ohm's law",
        "Boyle's law",
        "Law of conservation of energy",
    ),

    q(
        "General Engineering",
        "The SI unit of force is:",
        "Joule",
        "Newton",
        "Pascal",
        "Watt",
        "Newton",
    ),

    q(
        "General Engineering",
        "The SI unit of pressure is:",
        "Pascal",
        "Newton",
        "Joule",
        "Watt",
        "Pascal",
    ),

    q(
        "General Engineering",
        "Which machine element is commonly used to transmit rotary motion between shafts?",
        "Gear",
        "Beam",
        "Column",
        "Slab",
        "Gear",
    ),

    q(
        "Telangana GK",
        "Telangana was officially formed as a separate state on:",
        "1 January 2014",
        "2 June 2014",
        "15 August 2014",
        "26 January 2014",
        "2 June 2014",
    ),

    q(
        "Telangana GK",
        "What is the capital of Telangana?",
        "Warangal",
        "Hyderabad",
        "Nizamabad",
        "Karimnagar",
        "Hyderabad",
    ),

    q(
        "Telangana GK",
        "Which river is one of the major rivers flowing through Telangana?",
        "Godavari",
        "Yamuna",
        "Sutlej",
        "Ravi",
        "Godavari",
    ),

    q(
        "Telangana GK",
        "Which city is historically associated with the Kakatiya dynasty?",
        "Warangal",
        "Mumbai",
        "Jaipur",
        "Patna",
        "Warangal",
    ),

    q(
        "General Awareness",
        "Which organization publishes Indian national standards for many engineering products and practices?",
        "Bureau of Indian Standards",
        "Election Commission",
        "RBI",
        "UPSC",
        "Bureau of Indian Standards",
    ),

]


TELANGANA_AEE_QUESTIONS = [

    # ============================================================
    # CIVIL ENGINEERING
    # ============================================================

    q(
        "Civil Engineering",
        "Which test is commonly used to determine the consistency of cement?",
        "Slump test",
        "Vicat test",
        "Compaction test",
        "Impact test",
        "Vicat test",
    ),

    q(
        "Civil Engineering",
        "The initial setting time of ordinary Portland cement should not be less than:",
        "10 minutes",
        "30 minutes",
        "60 minutes",
        "90 minutes",
        "30 minutes",
    ),

    q(
        "Civil Engineering",
        "Which instrument is commonly used for measuring horizontal angles in surveying?",
        "Level",
        "Theodolite",
        "Planimeter",
        "Prismatic compass",
        "Theodolite",
    ),

    q(
        "Civil Engineering",
        "The process of determining the relative elevations of points is called:",
        "Traversing",
        "Levelling",
        "Chaining",
        "Triangulation",
        "Levelling",
    ),

    q(
        "Civil Engineering",
        "Which type of foundation is generally suitable for heavy loads when soil bearing capacity is low?",
        "Isolated footing",
        "Strip footing",
        "Raft foundation",
        "Stepped footing",
        "Raft foundation",
    ),

    q(
        "Civil Engineering",
        "The characteristic strength of concrete is normally specified at an age of:",
        "3 days",
        "7 days",
        "14 days",
        "28 days",
        "28 days",
    ),

    q(
        "Civil Engineering",
        "Which test is used to measure the workability of fresh concrete?",
        "Slump test",
        "Tensile test",
        "Compression test",
        "Abrasion test",
        "Slump test",
    ),

    q(
        "Civil Engineering",
        "In a simply supported beam, the bending moment at a simple support is:",
        "Maximum",
        "Minimum but non-zero",
        "Zero",
        "Infinite",
        "Zero",
    ),

    q(
        "Civil Engineering",
        "Which soil has the highest permeability among the following?",
        "Clay",
        "Silt",
        "Sand",
        "Peat",
        "Sand",
    ),

    q(
        "Civil Engineering",
        "The unit weight of water is approximately:",
        "0.981 kN/m³",
        "9.81 kN/m³",
        "98.1 kN/m³",
        "981 kN/m³",
        "9.81 kN/m³",
    ),

    # ============================================================
    # ADVANCED CIVIL ENGINEERING
    # ============================================================

    q(
        "Civil Engineering",
        "Which method is commonly used for determining the bearing capacity of shallow foundations?",
        "Rankine method",
        "Terzaghi method",
        "Darcy method",
        "Bernoulli method",
        "Terzaghi method",
    ),

    q(
        "Civil Engineering",
        "According to Darcy's law, discharge through soil is proportional to:",
        "Hydraulic gradient",
        "Soil density only",
        "Porosity only",
        "Water temperature only",
        "Hydraulic gradient",
    ),

    q(
        "Civil Engineering",
        "Which property of concrete mainly improves resistance to weathering and chemical attack?",
        "Workability",
        "Durability",
        "Bleeding",
        "Segregation",
        "Durability",
    ),

    q(
        "Civil Engineering",
        "In reinforced concrete, steel reinforcement is mainly provided to resist:",
        "Compression only",
        "Tension",
        "Shrinkage only",
        "Temperature only",
        "Tension",
    ),

    q(
        "Civil Engineering",
        "The ratio of lateral strain to longitudinal strain is known as:",
        "Young's modulus",
        "Bulk modulus",
        "Poisson's ratio",
        "Shear modulus",
        "Poisson's ratio",
    ),

    q(
        "Civil Engineering",
        "Which survey is particularly suitable for preparing contour maps?",
        "Chain survey",
        "Plane table survey",
        "Topographical survey",
        "Cadastral survey",
        "Topographical survey",
    ),

    q(
        "Civil Engineering",
        "Which hydraulic structure is used to measure the flow of water in an open channel?",
        "Weir",
        "Dam",
        "Reservoir",
        "Aqueduct",
        "Weir",
    ),

    q(
        "Civil Engineering",
        "The Manning equation is mainly used in:",
        "Structural design",
        "Open channel flow",
        "Soil classification",
        "Traffic analysis",
        "Open channel flow",
    ),

    # ============================================================
    # ELECTRICAL ENGINEERING
    # ============================================================

    q(
        "Electrical Engineering",
        "Ohm's law states that, at constant temperature, current is proportional to:",
        "Resistance",
        "Voltage",
        "Power",
        "Frequency",
        "Voltage",
    ),

    q(
        "Electrical Engineering",
        "The SI unit of electrical resistance is:",
        "Volt",
        "Ampere",
        "Ohm",
        "Watt",
        "Ohm",
    ),

    q(
        "Electrical Engineering",
        "Which device converts electrical energy into mechanical energy?",
        "Transformer",
        "Generator",
        "Motor",
        "Rectifier",
        "Motor",
    ),

    q(
        "Electrical Engineering",
        "A transformer operates on the principle of:",
        "Electrolysis",
        "Mutual induction",
        "Thermal expansion",
        "Photoelectric effect",
        "Mutual induction",
    ),

    q(
        "Electrical Engineering",
        "Which instrument is used to measure electric current?",
        "Voltmeter",
        "Ammeter",
        "Wattmeter",
        "Ohmmeter",
        "Ammeter",
    ),

    q(
        "Electrical Engineering",
        "Which instrument measures electrical power?",
        "Ammeter",
        "Voltmeter",
        "Wattmeter",
        "Galvanometer",
        "Wattmeter",
    ),

    q(
        "Electrical Engineering",
        "In a purely resistive AC circuit, voltage and current are:",
        "90° out of phase",
        "180° out of phase",
        "In phase",
        "45° out of phase",
        "In phase",
    ),

    q(
        "Electrical Engineering",
        "Which protection device is commonly used against excessive current?",
        "Fuse",
        "Capacitor",
        "Transformer",
        "Inductor",
        "Fuse",
    ),

    # ============================================================
    # ADVANCED ELECTRICAL
    # ============================================================

    q(
        "Electrical Engineering",
        "The power factor of a purely resistive circuit is:",
        "0",
        "0.5",
        "1",
        "-1",
        "1",
    ),

    q(
        "Electrical Engineering",
        "Which machine is commonly used for generating three-phase electrical power?",
        "Synchronous generator",
        "DC motor",
        "Induction motor",
        "Transformer",
        "Synchronous generator",
    ),

    q(
        "Electrical Engineering",
        "In a three-phase balanced system, the phase difference between two phases is:",
        "30°",
        "60°",
        "90°",
        "120°",
        "120°",
    ),

    q(
        "Electrical Engineering",
        "Which device is used to improve the power factor of an inductive load?",
        "Resistor",
        "Capacitor",
        "Fuse",
        "Diode",
        "Capacitor",
    ),

    q(
        "Electrical Engineering",
        "The synchronous speed of an AC motor depends on frequency and:",
        "Resistance",
        "Number of poles",
        "Voltage only",
        "Current only",
        "Number of poles",
    ),

    q(
        "Electrical Engineering",
        "Which semiconductor device allows current to flow mainly in one direction?",
        "Transistor",
        "Diode",
        "Capacitor",
        "Inductor",
        "Diode",
    ),

    # ============================================================
    # MECHANICAL ENGINEERING
    # ============================================================

    q(
        "Mechanical Engineering",
        "The SI unit of force is:",
        "Joule",
        "Newton",
        "Watt",
        "Pascal",
        "Newton",
    ),

    q(
        "Mechanical Engineering",
        "Which law states that every action has an equal and opposite reaction?",
        "Newton's First Law",
        "Newton's Second Law",
        "Newton's Third Law",
        "Law of gravitation",
        "Newton's Third Law",
    ),

    q(
        "Mechanical Engineering",
        "The efficiency of a machine is the ratio of:",
        "Input to output",
        "Output to input",
        "Load to effort",
        "Effort to load",
        "Output to input",
    ),

    q(
        "Mechanical Engineering",
        "Which process is used to remove material using a rotating multi-point cutting tool?",
        "Turning",
        "Milling",
        "Forging",
        "Casting",
        "Milling",
    ),

    q(
        "Mechanical Engineering",
        "Which device converts heat energy into mechanical work?",
        "Pump",
        "Heat engine",
        "Compressor",
        "Transformer",
        "Heat engine",
    ),

    q(
        "Mechanical Engineering",
        "The SI unit of pressure is:",
        "Newton",
        "Pascal",
        "Joule",
        "Watt",
        "Pascal",
    ),

    q(
        "Mechanical Engineering",
        "Which thermodynamic law deals with conservation of energy?",
        "Zeroth law",
        "First law",
        "Second law",
        "Third law",
        "First law",
    ),

    q(
        "Mechanical Engineering",
        "Which device is used to increase the pressure of a gas?",
        "Turbine",
        "Compressor",
        "Condenser",
        "Boiler",
        "Compressor",
    ),

    # ============================================================
    # GENERAL / ENGINEERING
    # ============================================================

    q(
        "Engineering Mathematics",
        "The derivative of x² with respect to x is:",
        "x",
        "2x",
        "x²",
        "2",
        "2x",
    ),

    q(
        "Engineering Mathematics",
        "The integral of 1 with respect to x is:",
        "1",
        "x",
        "x²",
        "0",
        "x",
    ),

    q(
        "Engineering Mathematics",
        "If A = 2 and B = 3, then AB is:",
        "5",
        "6",
        "8",
        "9",
        "6",
    ),

    q(
        "General Engineering",
        "Which material generally has high electrical conductivity?",
        "Rubber",
        "Glass",
        "Copper",
        "Wood",
        "Copper",
    ),

    q(
        "General Engineering",
        "Which instrument is used to measure temperature?",
        "Barometer",
        "Thermometer",
        "Hygrometer",
        "Ammeter",
        "Thermometer",
    ),

    q(
        "General Engineering",
        "Which renewable energy source uses sunlight to generate electricity?",
        "Wind energy",
        "Solar energy",
        "Tidal energy",
        "Geothermal energy",
        "Solar energy",
    ),

    # ============================================================
    # TELANGANA / PUBLIC WORKS
    # ============================================================

    q(
        "Telangana Engineering",
        "Which major river flows through Telangana and is associated with the Kaleshwaram project?",
        "Ganga",
        "Godavari",
        "Yamuna",
        "Narmada",
        "Godavari",
    ),

    q(
        "Telangana Engineering",
        "The Kaleshwaram Lift Irrigation Project is primarily associated with:",
        "Irrigation",
        "Railways",
        "Air transport",
        "Mining",
        "Irrigation",
    ),

    q(
        "Telangana Engineering",
        "Which river is associated with the Nagarjuna Sagar project?",
        "Krishna",
        "Godavari",
        "Tungabhadra",
        "Musi",
        "Krishna",
    ),

    q(
        "Telangana Engineering",
        "The main objective of an irrigation project is to:",
        "Increase rainfall",
        "Provide water for agriculture",
        "Reduce soil fertility",
        "Increase air pollution",
        "Provide water for agriculture",
    ),

    q(
        "Telangana Engineering",
        "Which department is primarily responsible for construction and maintenance of many government buildings and roads?",
        "Public Works Department",
        "Forest Department",
        "Tourism Department",
        "Postal Department",
        "Public Works Department",
    ),

    q(
        "Telangana Engineering",
        "Which factor is especially important when designing a hydraulic structure?",
        "Water pressure",
        "Colour of concrete",
        "Paint thickness",
        "Room temperature only",
        "Water pressure",
    ),
]

DSC_QUESTIONS = [

    q(
        "Child Development & Pedagogy",
        "According to Piaget, children in the concrete operational stage can:",
        "Think only through reflexes",
        "Think logically about concrete objects",
        "Think only about imaginary situations",
        "Understand all abstract concepts",
        "Think logically about concrete objects",
    ),

    q(
        "Child Development & Pedagogy",
        "Which stage of Piaget's theory generally occurs from birth to about 2 years?",
        "Pre-operational stage",
        "Concrete operational stage",
        "Sensorimotor stage",
        "Formal operational stage",
        "Sensorimotor stage",
    ),

    q(
        "Child Development & Pedagogy",
        "The concept of the Zone of Proximal Development was proposed by:",
        "Jean Piaget",
        "Lev Vygotsky",
        "B. F. Skinner",
        "Ivan Pavlov",
        "Lev Vygotsky",
    ),

    q(
        "Child Development & Pedagogy",
        "Scaffolding in education means:",
        "Punishing students for mistakes",
        "Providing temporary support during learning",
        "Giving only written examinations",
        "Avoiding difficult tasks",
        "Providing temporary support during learning",
    ),

    q(
        "Child Development & Pedagogy",
        "According to Vygotsky, learning is strongly influenced by:",
        "Social interaction",
        "Physical height",
        "Memory alone",
        "Genetic inheritance alone",
        "Social interaction",
    ),

    q(
        "Child Development & Pedagogy",
        "Which approach considers individual differences among learners?",
        "Child-centred approach",
        "Teacher-only approach",
        "Rote-only approach",
        "Lecture-only approach",
        "Child-centred approach",
    ),

    q(
        "Child Development & Pedagogy",
        "A teacher who allows students to discover concepts independently is using:",
        "Discovery learning",
        "Punitive learning",
        "Mechanical learning",
        "Passive learning",
        "Discovery learning",
    ),

    q(
        "Child Development & Pedagogy",
        "Which of the following is an example of intrinsic motivation?",
        "Studying because of curiosity",
        "Studying only for a prize",
        "Studying because of punishment",
        "Studying because of parental pressure",
        "Studying because of curiosity",
    ),

    q(
        "Child Development & Pedagogy",
        "A child's development is best described as:",
        "Completely uniform",
        "A continuous process",
        "Limited to physical growth",
        "Completed before school",
        "A continuous process",
    ),

    q(
        "Child Development & Pedagogy",
        "Which factor can significantly influence child development?",
        "Heredity and environment",
        "Only school uniforms",
        "Only examination marks",
        "Only classroom furniture",
        "Heredity and environment",
    ),

    q(
        "Educational Psychology",
        "Which type of assessment is conducted during the teaching-learning process?",
        "Formative assessment",
        "Final assessment",
        "Entrance assessment",
        "Selection assessment",
        "Formative assessment",
    ),

    q(
        "Educational Psychology",
        "Summative assessment is generally conducted:",
        "Only before teaching",
        "During every five minutes",
        "At the end of a course or instructional period",
        "Before admission",
        "At the end of a course or instructional period",
    ),

    q(
        "Educational Psychology",
        "The main purpose of formative assessment is to:",
        "Improve ongoing learning",
        "Rank students permanently",
        "Remove weak students",
        "Replace teaching",
        "Improve ongoing learning",
    ),

    q(
        "Educational Psychology",
        "A diagnostic test is mainly used to identify:",
        "Learning difficulties",
        "School holidays",
        "Teacher attendance",
        "Classroom furniture",
        "Learning difficulties",
    ),

    q(
        "Educational Psychology",
        "Remedial teaching is designed mainly for students who:",
        "Need additional help in learning",
        "Always obtain full marks",
        "Do not attend examinations",
        "Have completed all learning objectives",
        "Need additional help in learning",
    ),

    q(
        "Educational Psychology",
        "Which classroom practice promotes active learning?",
        "Group discussion",
        "Continuous dictation",
        "Silent copying",
        "Memorising without understanding",
        "Group discussion",
    ),

    q(
        "Educational Psychology",
        "A portfolio is useful for:",
        "Showing a learner's progress over time",
        "Replacing every classroom activity",
        "Measuring school buildings",
        "Recording only attendance",
        "Showing a learner's progress over time",
    ),

    q(
        "Educational Psychology",
        "A rubric is mainly used to:",
        "Provide criteria for evaluating student work",
        "Record school holidays",
        "Calculate teacher salary",
        "Prepare school transport",
        "Provide criteria for evaluating student work",
    ),

    q(
        "Educational Psychology",
        "Which is most important in effective classroom communication?",
        "Clarity",
        "Confusion",
        "Fear",
        "Silence",
        "Clarity",
    ),

    q(
        "Educational Psychology",
        "Feedback given immediately after a student's performance can help:",
        "Improve learning",
        "Prevent learning",
        "Eliminate practice",
        "Replace assessment completely",
        "Improve learning",
    ),

    q(
        "Teaching Methods",
        "The project method of teaching is associated with:",
        "Learning through purposeful activities",
        "Only memorisation",
        "Only dictation",
        "Only lectures",
        "Learning through purposeful activities",
    ),

    q(
        "Teaching Methods",
        "The demonstration method is particularly useful when the teacher wants to:",
        "Show a process or procedure",
        "Avoid student observation",
        "Prevent questions",
        "Eliminate practical learning",
        "Show a process or procedure",
    ),

    q(
        "Teaching Methods",
        "The discussion method encourages students to:",
        "Express and exchange ideas",
        "Remain completely silent",
        "Avoid interaction",
        "Memorise every sentence",
        "Express and exchange ideas",
    ),

    q(
        "Teaching Methods",
        "The inductive method proceeds generally from:",
        "Specific examples to a general rule",
        "General rule to specific examples",
        "Theory to punishment",
        "Assessment to admission",
        "Specific examples to a general rule",
    ),

    q(
        "Teaching Methods",
        "The deductive method generally proceeds from:",
        "General principle to specific examples",
        "Specific examples to a general principle",
        "Observation to guessing",
        "Activity to examination",
        "General principle to specific examples",
    ),

    q(
        "Teaching Methods",
        "Brainstorming is mainly used to:",
        "Generate ideas",
        "Conduct physical training",
        "Record attendance",
        "Punish students",
        "Generate ideas",
    ),

    q(
        "Teaching Methods",
        "Which method is most suitable for developing practical skills?",
        "Learning by doing",
        "Only reading",
        "Only memorisation",
        "Only dictation",
        "Learning by doing",
    ),

    q(
        "Teaching Methods",
        "A lesson plan helps a teacher to:",
        "Organise the teaching process",
        "Avoid preparation",
        "Eliminate assessment",
        "Reduce student participation",
        "Organise the teaching process",
    ),

    q(
        "Teaching Methods",
        "Teaching aids are mainly used to:",
        "Make learning clearer and more effective",
        "Increase classroom noise",
        "Replace the teacher completely",
        "Avoid explanation",
        "Make learning clearer and more effective",
    ),

    q(
        "Teaching Methods",
        "Which activity best promotes cooperative learning?",
        "Small-group problem solving",
        "Individual punishment",
        "Silent copying",
        "Teacher monologue",
        "Small-group problem solving",
    ),

    q(
        "Inclusive Education",
        "Inclusive education means:",
        "Educating learners together while addressing diverse needs",
        "Teaching only high achievers",
        "Separating every learner",
        "Avoiding students with disabilities",
        "Educating learners together while addressing diverse needs",
    ),

    q(
        "Inclusive Education",
        "A teacher should respond to a learner with a disability by:",
        "Providing appropriate support and accommodations",
        "Ignoring the learner",
        "Removing the learner from all activities",
        "Giving no classroom support",
        "Providing appropriate support and accommodations",
    ),

    q(
        "Inclusive Education",
        "Which classroom practice supports inclusive education?",
        "Using different teaching strategies",
        "Using one method for every learner",
        "Ignoring individual needs",
        "Avoiding group activities",
        "Using different teaching strategies",
    ),

    q(
        "Inclusive Education",
        "Universal Design for Learning encourages teachers to provide:",
        "Multiple ways of engaging with learning",
        "Only one examination method",
        "Only textbook-based learning",
        "Only oral instruction",
        "Multiple ways of engaging with learning",
    ),

    q(
        "Inclusive Education",
        "Peer tutoring can help learners by:",
        "Encouraging cooperation and support",
        "Preventing communication",
        "Reducing participation",
        "Eliminating classroom interaction",
        "Encouraging cooperation and support",
    ),

    q(
        "Inclusive Education",
        "A barrier-free school environment is important because it:",
        "Improves accessibility for all learners",
        "Limits participation",
        "Prevents movement",
        "Reduces inclusion",
        "Improves accessibility for all learners",
    ),

    q(
        "Inclusive Education",
        "Which approach is appropriate for a learner with different learning needs?",
        "Differentiated instruction",
        "Identical instruction in every situation",
        "No instruction",
        "Punishment-based instruction",
        "Differentiated instruction",
    ),

    q(
        "Inclusive Education",
        "Assistive technology can help learners by:",
        "Supporting access to learning",
        "Replacing all teachers",
        "Preventing communication",
        "Removing classroom activities",
        "Supporting access to learning",
    ),

    q(
        "Inclusive Education",
        "An inclusive classroom should encourage:",
        "Respect and participation",
        "Discrimination",
        "Isolation",
        "Fear",
        "Respect and participation",
    ),

    q(
        "Inclusive Education",
        "The primary aim of inclusive education is to:",
        "Provide equitable learning opportunities",
        "Separate learners permanently",
        "Reduce participation",
        "Focus only on examination scores",
        "Provide equitable learning opportunities",
    ),

    q(
        "Telangana Education",
        "The capital city of Telangana is:",
        "Warangal",
        "Hyderabad",
        "Nizamabad",
        "Karimnagar",
        "Hyderabad",
    ),

    q(
        "Telangana Education",
        "Telangana was formed as a separate state on:",
        "1 June 2014",
        "2 June 2014",
        "1 July 2014",
        "15 August 2014",
        "2 June 2014",
    ),

    q(
        "Telangana Education",
        "Which language is widely used as a medium of instruction in schools in Telangana?",
        "Telugu",
        "French",
        "German",
        "Russian",
        "Telugu",
    ),

    q(
        "Telangana Education",
        "The official language of Telangana includes:",
        "Telugu",
        "Spanish",
        "French",
        "German",
        "Telugu",
    ),

    q(
        "General Knowledge",
        "The Right to Education Act primarily relates to education of children in the age group:",
        "3–5 years",
        "6–14 years",
        "15–18 years",
        "18–21 years",
        "6–14 years",
    ),

    q(
        "General Knowledge",
        "Which fundamental right is related to freedom of speech and expression?",
        "Article 14",
        "Article 19",
        "Article 21",
        "Article 32",
        "Article 19",
    ),

    q(
        "General Knowledge",
        "The Constitution of India came into force on:",
        "15 August 1947",
        "26 January 1950",
        "26 November 1949",
        "2 October 1950",
        "26 January 1950",
    ),

    q(
        "General Knowledge",
        "Who was the first Education Minister of independent India?",
        "Maulana Abul Kalam Azad",
        "Sardar Patel",
        "Rajendra Prasad",
        "C. Rajagopalachari",
        "Maulana Abul Kalam Azad",
    ),

    q(
        "General Knowledge",
        "The National Education Policy 2020 introduced which school structure?",
        "5+3+3+4",
        "10+2+3",
        "8+4+2",
        "6+6+4",
        "5+3+3+4",
    ),

]

HIGH_COURT_QUESTIONS = [

    q(
        "Indian Constitution",
        "Which Part of the Constitution contains provisions relating to High Courts?",
        "Part III",
        "Part IV",
        "Part VI",
        "Part V",
        "Part VI",
    ),

    q(
        "Indian Constitution",
        "Which Articles of the Constitution primarily deal with High Courts?",
        "Articles 124–147",
        "Articles 214–231",
        "Articles 245–263",
        "Articles 280–300",
        "Articles 214–231",
    ),

    q(
        "Indian Constitution",
        "Which Article provides for a High Court for each State?",
        "Article 214",
        "Article 215",
        "Article 216",
        "Article 217",
        "Article 214",
    ),

    q(
        "Indian Constitution",
        "Under which Article is every High Court declared to be a Court of Record?",
        "Article 214",
        "Article 215",
        "Article 226",
        "Article 227",
        "Article 215",
    ),

    q(
        "Indian Constitution",
        "What is one important power of a High Court as a Court of Record?",
        "Power to make laws",
        "Power to punish for its own contempt",
        "Power to appoint Governors",
        "Power to amend the Constitution",
        "Power to punish for its own contempt",
    ),

    q(
        "Indian Constitution",
        "Which Article deals with the constitution of High Courts?",
        "Article 215",
        "Article 216",
        "Article 217",
        "Article 218",
        "Article 216",
    ),

    q(
        "Indian Constitution",
        "Who formally appoints a Judge of a High Court?",
        "Prime Minister",
        "Governor",
        "President of India",
        "Chief Justice of India",
        "President of India",
    ),

    q(
        "Indian Constitution",
        "Which Article deals with the appointment and conditions of office of a High Court Judge?",
        "Article 216",
        "Article 217",
        "Article 218",
        "Article 220",
        "Article 217",
    ),

    q(
        "Indian Constitution",
        "What is the retirement age of a High Court Judge?",
        "60 years",
        "62 years",
        "65 years",
        "68 years",
        "62 years",
    ),

    q(
        "Indian Constitution",
        "A High Court Judge may resign by addressing the resignation to whom?",
        "Governor",
        "Chief Justice of India",
        "President of India",
        "Prime Minister",
        "President of India",
    ),

    q(
        "Indian Constitution",
        "Which authority transfers a High Court Judge from one High Court to another?",
        "Governor",
        "President of India",
        "Chief Minister",
        "Parliament",
        "President of India",
    ),

    q(
        "Indian Constitution",
        "Which Article deals with the application of certain provisions relating to Supreme Court Judges to High Court Judges?",
        "Article 217",
        "Article 218",
        "Article 219",
        "Article 220",
        "Article 218",
    ),

    q(
        "Indian Constitution",
        "Before entering office, a High Court Judge takes an oath or affirmation before whom?",
        "President of India",
        "Chief Justice of India",
        "Governor of the State",
        "Chief Minister",
        "Governor of the State",
    ),

    q(
        "Indian Constitution",
        "Which Article deals with the oath or affirmation by High Court Judges?",
        "Article 218",
        "Article 219",
        "Article 220",
        "Article 221",
        "Article 219",
    ),

    q(
        "Indian Constitution",
        "Which Article places restrictions on practice after a person has been a permanent Judge of a High Court?",
        "Article 219",
        "Article 220",
        "Article 221",
        "Article 222",
        "Article 220",
    ),

    q(
        "Indian Constitution",
        "Which Article deals with the salaries of High Court Judges?",
        "Article 220",
        "Article 221",
        "Article 222",
        "Article 223",
        "Article 221",
    ),

    q(
        "Indian Constitution",
        "Which Article deals with the transfer of a Judge from one High Court to another?",
        "Article 221",
        "Article 222",
        "Article 223",
        "Article 224",
        "Article 222",
    ),

    q(
        "Indian Constitution",
        "Who appoints an Acting Chief Justice of a High Court when necessary?",
        "Governor",
        "President of India",
        "Chief Minister",
        "Parliament",
        "President of India",
    ),

    q(
        "Indian Constitution",
        "Which Article deals with the appointment of Acting Chief Justice?",
        "Article 222",
        "Article 223",
        "Article 224",
        "Article 225",
        "Article 223",
    ),

    q(
        "Indian Constitution",
        "Which Article deals with additional and acting Judges of High Courts?",
        "Article 223",
        "Article 224",
        "Article 225",
        "Article 226",
        "Article 224",
    ),

    q(
        "Indian Constitution",
        "Under which Article can retired High Court Judges be requested to sit and act as Judges of a High Court?",
        "Article 224",
        "Article 224A",
        "Article 225",
        "Article 226",
        "Article 224A",
    ),

    q(
        "Indian Constitution",
        "Which Article deals with the jurisdiction of existing High Courts?",
        "Article 224",
        "Article 225",
        "Article 226",
        "Article 227",
        "Article 225",
    ),

    q(
        "Writ Jurisdiction",
        "Which Article gives High Courts the power to issue writs?",
        "Article 32",
        "Article 136",
        "Article 226",
        "Article 227",
        "Article 226",
    ),

    q(
        "Writ Jurisdiction",
        "The writ jurisdiction of High Courts under Article 226 can be used for enforcement of Fundamental Rights and what else?",
        "Only criminal laws",
        "Other legal rights",
        "Only Directive Principles",
        "Only constitutional amendments",
        "Other legal rights",
    ),

    q(
        "Writ Jurisdiction",
        "Which writ literally means 'produce the body'?",
        "Mandamus",
        "Habeas Corpus",
        "Certiorari",
        "Quo Warranto",
        "Habeas Corpus",
    ),

    q(
        "Writ Jurisdiction",
        "Which writ is generally issued to command a public authority to perform a legal duty?",
        "Mandamus",
        "Habeas Corpus",
        "Prohibition",
        "Certiorari",
        "Mandamus",
    ),

    q(
        "Writ Jurisdiction",
        "Which writ is used to challenge a person's unlawful occupation of a public office?",
        "Habeas Corpus",
        "Mandamus",
        "Quo Warranto",
        "Prohibition",
        "Quo Warranto",
    ),

    q(
        "Writ Jurisdiction",
        "Which writ is generally issued to prevent a lower court or tribunal from exceeding its jurisdiction?",
        "Prohibition",
        "Mandamus",
        "Habeas Corpus",
        "Quo Warranto",
        "Prohibition",
    ),

    q(
        "Writ Jurisdiction",
        "Which writ is generally used to quash an order already passed by a lower court or tribunal?",
        "Mandamus",
        "Certiorari",
        "Habeas Corpus",
        "Quo Warranto",
        "Certiorari",
    ),

    q(
        "Writ Jurisdiction",
        "Which constitutional Article provides the Supreme Court's writ jurisdiction for Fundamental Rights?",
        "Article 14",
        "Article 19",
        "Article 32",
        "Article 226",
        "Article 32",
    ),

    q(
        "Writ Jurisdiction",
        "Compared with Article 32, the writ jurisdiction of High Courts under Article 226 is generally:",
        "Narrower",
        "Broader",
        "Identical in every respect",
        "Limited only to criminal matters",
        "Broader",
    ),

    q(
        "Judicial Powers",
        "Which Article gives a High Court power of superintendence over courts and tribunals within its jurisdiction?",
        "Article 226",
        "Article 227",
        "Article 228",
        "Article 229",
        "Article 227",
    ),

    q(
        "Judicial Powers",
        "The power of superintendence under Article 227 is primarily exercised over:",
        "Parliament",
        "State Legislature",
        "Courts and tribunals within the High Court's territorial jurisdiction",
        "Election Commission",
        "Courts and tribunals within the High Court's territorial jurisdiction",
    ),

    q(
        "Judicial Powers",
        "Which Article permits a High Court to withdraw certain cases involving substantial questions of constitutional interpretation?",
        "Article 226",
        "Article 227",
        "Article 228",
        "Article 229",
        "Article 228",
    ),

    q(
        "Judicial Powers",
        "Who has the power to make rules concerning officers and servants of a High Court, subject to law?",
        "Governor",
        "Chief Justice of the High Court",
        "Chief Minister",
        "President",
        "Chief Justice of the High Court",
    ),

    q(
        "Judicial Powers",
        "Which Article deals with officers and servants of High Courts?",
        "Article 228",
        "Article 229",
        "Article 230",
        "Article 231",
        "Article 229",
    ),

    q(
        "Judicial Powers",
        "Which Article deals with extension of jurisdiction of a High Court to Union Territories?",
        "Article 229",
        "Article 230",
        "Article 231",
        "Article 232",
        "Article 230",
    ),

    q(
        "Judicial Powers",
        "Which Article allows Parliament to establish a common High Court for two or more States or for States and a Union Territory?",
        "Article 229",
        "Article 230",
        "Article 231",
        "Article 232",
        "Article 231",
    ),

    q(
        "Judiciary",
        "At the State level, the High Court is generally the highest judicial authority in the State's judicial hierarchy.",
        "Supreme Court",
        "High Court",
        "District Court",
        "Taluk Court",
        "High Court",
    ),

    q(
        "Judiciary",
        "Which court is generally above the High Court in India's integrated judicial system?",
        "District Court",
        "Sessions Court",
        "Supreme Court",
        "Magistrate Court",
        "Supreme Court",
    ),

    q(
        "Judiciary",
        "Which of the following is NOT a writ issued by High Courts?",
        "Habeas Corpus",
        "Mandamus",
        "Certiorari",
        "Injunction",
        "Injunction",
    ),

    q(
        "Judiciary",
        "Which type of jurisdiction allows a High Court to hear appeals from subordinate courts?",
        "Appellate jurisdiction",
        "Advisory jurisdiction",
        "Electoral jurisdiction",
        "Legislative jurisdiction",
        "Appellate jurisdiction",
    ),

    q(
        "Judiciary",
        "High Courts exercise judicial review primarily to examine whether laws and executive actions conform to:",
        "Political party rules",
        "The Constitution",
        "Government advertisements",
        "Private agreements only",
        "The Constitution",
    ),

    q(
        "Judiciary",
        "Which principle is closely associated with the independence of the judiciary?",
        "Judicial control by political parties",
        "Security of tenure",
        "Executive appointment without safeguards",
        "Removal by ordinary executive order",
        "Security of tenure",
    ),

    q(
        "Judiciary",
        "A High Court can exercise contempt jurisdiction because it is constitutionally recognized as:",
        "A court of record",
        "An election tribunal",
        "A legislative body",
        "An executive authority",
        "A court of record",
    ),

    q(
        "Legal Awareness",
        "Which body is generally responsible for administering justice at the district level under the supervision of the High Court?",
        "District judiciary",
        "Parliament",
        "Election Commission",
        "Finance Commission",
        "District judiciary",
    ),

    q(
        "Legal Awareness",
        "Which constitutional principle allows courts to invalidate laws that violate constitutional provisions?",
        "Judicial review",
        "Collective responsibility",
        "Cabinet secrecy",
        "Universal adult franchise",
        "Judicial review",
    ),

    q(
        "Legal Awareness",
        "Which Fundamental Right is most directly associated with protection against unlawful detention through Habeas Corpus?",
        "Right to Equality",
        "Right to Freedom",
        "Right against Exploitation",
        "Cultural and Educational Rights",
        "Right to Freedom",
    ),

    q(
        "Legal Awareness",
        "Which court normally exercises superintendence over subordinate courts within its territorial jurisdiction?",
        "Supreme Court only",
        "High Court",
        "District Court",
        "Lok Sabha",
        "High Court",
    ),

    q(
        "Legal Awareness",
        "Which of the following best describes the role of a High Court in a State?",
        "Only an administrative office",
        "Highest court at the State judicial level",
        "Only a criminal court",
        "Only an election body",
        "Highest court at the State judicial level",
    ),

    q(
        "Legal Awareness",
        "Which of the following is an important function of High Courts?",
        "Issuing writs",
        "Conducting national elections",
        "Making the Union Budget",
        "Appointing Union Ministers",
        "Issuing writs",
    ),

    q(
        "Legal Awareness",
        "Which constitutional provision enables a High Court to supervise subordinate courts and tribunals?",
        "Article 214",
        "Article 219",
        "Article 226",
        "Article 227",
        "Article 227",
    ),

    q(
        "Legal Awareness",
        "Which statement about Article 226 is correct?",
        "It applies only to criminal cases",
        "It gives High Courts writ jurisdiction",
        "It deals with appointment of Governors",
        "It deals with State budgets",
        "It gives High Courts writ jurisdiction",
    ),

    q(
        "Legal Awareness",
        "Which statement correctly distinguishes Article 226 from Article 32?",
        "Only Article 226 concerns courts",
        "Article 226 permits High Courts to issue writs for Fundamental Rights and other legal rights",
        "Article 32 applies only to High Courts",
        "Article 226 deals only with elections",
        "Article 226 permits High Courts to issue writs for Fundamental Rights and other legal rights",
    ),

]

DISTRICT_COURT_QUESTIONS = [

    q(
        "Indian Constitution",
        "Which institution is the highest judicial authority at the State level?",
        "District Court",
        "High Court",
        "Lok Adalat",
        "Tribunal",
        "High Court",
    ),

    q(
        "Indian Constitution",
        "Which Article of the Constitution provides for the establishment of High Courts?",
        "Article 214",
        "Article 124",
        "Article 280",
        "Article 300",
        "Article 214",
    ),

    q(
        "Indian Constitution",
        "Which Article gives High Courts the power of superintendence over subordinate courts?",
        "Article 226",
        "Article 227",
        "Article 229",
        "Article 230",
        "Article 227",
    ),

    q(
        "Judiciary",
        "The District Judiciary primarily functions under the supervision of:",
        "Supreme Court",
        "High Court",
        "Parliament",
        "Governor",
        "High Court",
    ),

    q(
        "Judiciary",
        "Who generally heads the judicial administration at the district level?",
        "District and Sessions Judge",
        "District Collector",
        "Superintendent of Police",
        "Municipal Commissioner",
        "District and Sessions Judge",
    ),

    q(
        "Judiciary",
        "A District and Sessions Judge generally exercises both:",
        "Civil and criminal jurisdiction",
        "Only civil jurisdiction",
        "Only criminal jurisdiction",
        "Only administrative jurisdiction",
        "Civil and criminal jurisdiction",
    ),

    q(
        "Judiciary",
        "The criminal court at the district level dealing with serious offences is commonly known as:",
        "Sessions Court",
        "Revenue Court",
        "Family Court",
        "Consumer Court",
        "Sessions Court",
    ),

    q(
        "Judiciary",
        "The Sessions Court primarily deals with:",
        "Serious criminal cases",
        "Land registration only",
        "Tax collection",
        "Municipal disputes only",
        "Serious criminal cases",
    ),

    q(
        "Judiciary",
        "Which court generally hears appeals from lower courts within the district judicial system?",
        "District Court",
        "Gram Panchayat",
        "Revenue Office",
        "Police Station",
        "District Court",
    ),

    q(
        "Judiciary",
        "A subordinate court is generally subject to the supervisory jurisdiction of:",
        "High Court",
        "Election Commission",
        "Parliament",
        "Finance Commission",
        "High Court",
    ),

    q(
        "Civil Law",
        "Which law primarily governs civil procedure in India?",
        "Code of Civil Procedure",
        "Indian Penal Code",
        "Evidence Act",
        "Police Act",
        "Code of Civil Procedure",
    ),

    q(
        "Civil Law",
        "The Code of Civil Procedure is commonly abbreviated as:",
        "CPC",
        "IPC",
        "CrPC",
        "IEA",
        "CPC",
    ),

    q(
        "Civil Law",
        "A civil suit generally deals with disputes involving:",
        "Civil rights and obligations",
        "Only murder",
        "Only theft",
        "Only traffic violations",
        "Civil rights and obligations",
    ),

    q(
        "Civil Law",
        "Which document normally initiates a civil suit?",
        "Plaint",
        "Charge sheet",
        "FIR",
        "Warrant",
        "Plaint",
    ),

    q(
        "Civil Law",
        "The person who files a civil suit is generally called:",
        "Plaintiff",
        "Defendant",
        "Accused",
        "Witness",
        "Plaintiff",
    ),

    q(
        "Civil Law",
        "The person against whom a civil suit is filed is called:",
        "Plaintiff",
        "Defendant",
        "Petitioner",
        "Witness",
        "Defendant",
    ),

    q(
        "Civil Law",
        "A temporary injunction is primarily intended to:",
        "Preserve the situation until the case is decided",
        "Punish the defendant",
        "Arrest the plaintiff",
        "End every civil case immediately",
        "Preserve the situation until the case is decided",
    ),

    q(
        "Civil Law",
        "A decree is generally associated with:",
        "Formal adjudication of rights in a civil suit",
        "Registration of births",
        "Police investigation",
        "Election results",
        "Formal adjudication of rights in a civil suit",
    ),

    q(
        "Civil Law",
        "An appeal is generally filed against:",
        "A decision or order of a court",
        "A police uniform",
        "A government advertisement",
        "A school timetable",
        "A decision or order of a court",
    ),

    q(
        "Civil Law",
        "Execution proceedings are primarily concerned with:",
        "Enforcing a decree or order",
        "Registering a new case",
        "Conducting elections",
        "Issuing passports",
        "Enforcing a decree or order",
    ),

    q(
        "Criminal Law",
        "A First Information Report is commonly known as:",
        "FIR",
        "PIL",
        "CPC",
        "Writ",
        "FIR",
    ),

    q(
        "Criminal Law",
        "An FIR is generally recorded in connection with:",
        "Information about a cognizable offence",
        "Civil contracts only",
        "Property registration only",
        "School admissions",
        "Information about a cognizable offence",
    ),

    q(
        "Criminal Law",
        "The person against whom a criminal case is brought is generally called:",
        "Accused",
        "Plaintiff",
        "Decree-holder",
        "Arbitrator",
        "Accused",
    ),

    q(
        "Criminal Law",
        "The person who gives evidence before a court is called:",
        "Witness",
        "Plaintiff",
        "Accused",
        "Judge",
        "Witness",
    ),

    q(
        "Criminal Law",
        "A charge sheet is generally submitted after:",
        "Investigation",
        "Judgment",
        "Appeal",
        "Sentencing only",
        "Investigation",
    ),

    q(
        "Criminal Law",
        "Bail generally means:",
        "Temporary release of an accused subject to legal conditions",
        "Permanent acquittal",
        "Cancellation of a case",
        "Conviction",
        "Temporary release of an accused subject to legal conditions",
    ),

    q(
        "Criminal Law",
        "An acquittal means that:",
        "The accused is found not guilty",
        "The accused is arrested",
        "The case automatically becomes civil",
        "The accused is convicted",
        "The accused is found not guilty",
    ),

    q(
        "Criminal Law",
        "A conviction means that:",
        "The accused has been found guilty",
        "The accused has been released without trial",
        "The case has been withdrawn",
        "A civil suit has been filed",
        "The accused has been found guilty",
    ),

    q(
        "Criminal Law",
        "A warrant is generally issued by:",
        "A competent court",
        "A private citizen",
        "A school teacher",
        "A bank manager",
        "A competent court",
    ),

    q(
        "Criminal Law",
        "The main purpose of a criminal trial is to:",
        "Determine whether the accused is guilty according to law",
        "Collect taxes",
        "Register property",
        "Conduct elections",
        "Determine whether the accused is guilty according to law",
    ),

    q(
        "Evidence",
        "Evidence presented before a court is primarily used to:",
        "Establish facts relevant to the case",
        "Prepare school records",
        "Collect taxes",
        "Issue driving licences",
        "Establish facts relevant to the case",
    ),

    q(
        "Evidence",
        "Oral evidence generally refers to:",
        "Statements made by witnesses",
        "Written contracts only",
        "Physical objects only",
        "Court buildings",
        "Statements made by witnesses",
    ),

    q(
        "Evidence",
        "Documentary evidence includes:",
        "Relevant documents produced before the court",
        "Only oral statements",
        "Only police uniforms",
        "Only photographs of judges",
        "Relevant documents produced before the court",
    ),

    q(
        "Evidence",
        "A witness who gives evidence in court may be subjected to:",
        "Cross-examination",
        "Election",
        "Appointment",
        "Promotion",
        "Cross-examination",
    ),

    q(
        "Evidence",
        "Cross-examination is generally conducted by:",
        "The opposing party or their advocate",
        "The court clerk only",
        "The police constable only",
        "The court typist",
        "The opposing party or their advocate",
    ),

    q(
        "Court Procedure",
        "The person who presides over a court proceeding is generally called:",
        "Judge",
        "Clerk",
        "Typist",
        "Bailiff",
        "Judge",
    ),

    q(
        "Court Procedure",
        "An advocate represents:",
        "A party before the court",
        "Only the judge",
        "Only the police",
        "Only the government office",
        "A party before the court",
    ),

    q(
        "Court Procedure",
        "A petition is generally:",
        "A formal written application made to a court",
        "A police uniform",
        "A tax receipt",
        "A school certificate",
        "A formal written application made to a court",
    ),

    q(
        "Court Procedure",
        "A summons is generally used to:",
        "Require a person to appear before a court",
        "Declare someone guilty automatically",
        "Cancel every case",
        "Transfer property",
        "Require a person to appear before a court",
    ),

    q(
        "Court Procedure",
        "A court order is:",
        "A direction issued by a court",
        "A private agreement",
        "A police complaint",
        "A newspaper article",
        "A direction issued by a court",
    ),

    q(
        "Court Procedure",
        "Adjournment means:",
        "Postponement of a court proceeding to another date",
        "Final conviction",
        "Permanent closure of all courts",
        "Transfer of a judge",
        "Postponement of a court proceeding to another date",
    ),

    q(
        "Legal Terminology",
        "What does 'prima facie' generally mean?",
        "At first sight or on the face of it",
        "After final judgment",
        "Without evidence",
        "Against the law",
        "At first sight or on the face of it",
    ),

    q(
        "Legal Terminology",
        "What does 'bona fide' mean?",
        "In good faith",
        "In bad faith",
        "Without authority",
        "After conviction",
        "In good faith",
    ),

    q(
        "Legal Terminology",
        "What does 'ex parte' generally refer to?",
        "A proceeding involving one side in the absence of the other side",
        "A criminal conviction",
        "A police investigation",
        "A final appeal",
        "A proceeding involving one side in the absence of the other side",
    ),

    q(
        "Legal Terminology",
        "What does 'amicus curiae' mean?",
        "Friend of the court",
        "Court clerk",
        "Government prosecutor",
        "Court police",
        "Friend of the court",
    ),

    q(
        "Legal Terminology",
        "What does 'suo motu' mean?",
        "On its own motion",
        "By police order",
        "By private contract",
        "After an election",
        "On its own motion",
    ),

    q(
        "Legal Terminology",
        "What does 'habeas corpus' literally relate to?",
        "Production of a detained person before the court",
        "Transfer of property",
        "Appointment of judges",
        "Civil damages",
        "Production of a detained person before the court",
    ),

    q(
        "Court Administration",
        "Court records are maintained primarily to:",
        "Preserve official information about judicial proceedings",
        "Collect taxes",
        "Conduct elections",
        "Issue passports",
        "Preserve official information about judicial proceedings",
    ),

    q(
        "Court Administration",
        "A court clerk primarily assists in:",
        "Administrative and record-related court work",
        "Passing judicial judgments",
        "Making laws",
        "Conducting elections",
        "Administrative and record-related court work",
    ),

    q(
        "Court Administration",
        "Cause lists generally contain:",
        "Cases listed for hearing",
        "Names of school students",
        "Taxpayer lists",
        "Election candidates only",
        "Cases listed for hearing",
    ),

    q(
        "Court Administration",
        "A certified copy of a court order is:",
        "An officially authenticated copy",
        "A newspaper report",
        "A private handwritten note",
        "An unofficial summary",
        "An officially authenticated copy",
    ),

    q(
        "Court Administration",
        "Digitization of court records mainly helps to:",
        "Improve access, storage and management of records",
        "Eliminate all courts",
        "Replace every judge",
        "Stop appeals",
        "Improve access, storage and management of records",
    ),

    q(
        "Legal Awareness",
        "Lok Adalat is mainly associated with:",
        "Alternative dispute resolution",
        "Criminal investigation",
        "Police recruitment",
        "Tax collection",
        "Alternative dispute resolution",
    ),

    q(
        "Legal Awareness",
        "The main objective of alternative dispute resolution is to:",
        "Resolve disputes through methods outside the traditional trial process",
        "Increase litigation",
        "Prevent settlements",
        "Replace the Constitution",
        "Resolve disputes through methods outside the traditional trial process",
    ),

    q(
        "Legal Awareness",
        "Legal aid is primarily intended to:",
        "Provide legal assistance to eligible persons who cannot afford it",
        "Provide free education to judges",
        "Replace courts",
        "Conduct elections",
        "Provide legal assistance to eligible persons who cannot afford it",
    ),

]

HEALTH_DEPARTMENT_QUESTIONS = [

    q(
        "Human Anatomy",
        "Which organ pumps blood throughout the human body?",
        "Lungs",
        "Heart",
        "Kidney",
        "Liver",
        "Heart",
    ),

    q(
        "Human Anatomy",
        "Which is the largest organ of the human body?",
        "Liver",
        "Skin",
        "Heart",
        "Lungs",
        "Skin",
    ),

    q(
        "Human Anatomy",
        "Which organ is primarily responsible for filtering blood and producing urine?",
        "Liver",
        "Kidney",
        "Heart",
        "Stomach",
        "Kidney",
    ),

    q(
        "Human Anatomy",
        "Which organ is mainly responsible for respiration?",
        "Heart",
        "Lungs",
        "Kidney",
        "Pancreas",
        "Lungs",
    ),

    q(
        "Human Anatomy",
        "Which part of the human brain controls balance and coordination?",
        "Cerebrum",
        "Cerebellum",
        "Medulla",
        "Hypothalamus",
        "Cerebellum",
    ),

    q(
        "Human Anatomy",
        "How many chambers are present in the human heart?",
        "Two",
        "Three",
        "Four",
        "Five",
        "Four",
    ),

    q(
        "Human Anatomy",
        "Which blood vessels carry blood away from the heart?",
        "Veins",
        "Arteries",
        "Capillaries",
        "Nerves",
        "Arteries",
    ),

    q(
        "Human Anatomy",
        "Which blood vessels generally carry blood towards the heart?",
        "Arteries",
        "Veins",
        "Capillaries",
        "Bronchi",
        "Veins",
    ),

    q(
        "Human Anatomy",
        "Which component of blood is mainly responsible for clotting?",
        "Red blood cells",
        "White blood cells",
        "Platelets",
        "Plasma",
        "Platelets",
    ),

    q(
        "Human Anatomy",
        "Which cells are primarily responsible for carrying oxygen?",
        "White blood cells",
        "Red blood cells",
        "Platelets",
        "Plasma cells",
        "Red blood cells",
    ),

    q(
        "Biology",
        "What is the basic structural and functional unit of life?",
        "Tissue",
        "Cell",
        "Organ",
        "Organ system",
        "Cell",
    ),

    q(
        "Biology",
        "Which organelle is known as the powerhouse of the cell?",
        "Nucleus",
        "Mitochondria",
        "Ribosome",
        "Lysosome",
        "Mitochondria",
    ),

    q(
        "Biology",
        "Which molecule carries genetic information in most living organisms?",
        "Protein",
        "DNA",
        "Glucose",
        "Lipid",
        "DNA",
    ),

    q(
        "Biology",
        "Which blood group is commonly known as the universal donor for red blood cells?",
        "AB positive",
        "A positive",
        "O negative",
        "B negative",
        "O negative",
    ),

    q(
        "Biology",
        "Which blood group is commonly known as the universal recipient for red blood cells?",
        "O negative",
        "AB positive",
        "A negative",
        "B positive",
        "AB positive",
    ),

    q(
        "Biology",
        "Which hormone regulates blood glucose levels?",
        "Insulin",
        "Thyroxine",
        "Adrenaline",
        "Estrogen",
        "Insulin",
    ),

    q(
        "Biology",
        "Which gland produces insulin?",
        "Thyroid",
        "Pancreas",
        "Pituitary",
        "Adrenal",
        "Pancreas",
    ),

    q(
        "Biology",
        "Which gland is often called the master gland?",
        "Thyroid gland",
        "Pituitary gland",
        "Adrenal gland",
        "Pancreas",
        "Pituitary gland",
    ),

    q(
        "Biology",
        "Which hormone is primarily associated with the body's fight-or-flight response?",
        "Insulin",
        "Adrenaline",
        "Melatonin",
        "Thyroxine",
        "Adrenaline",
    ),

    q(
        "Biology",
        "Which vitamin is important for normal blood clotting?",
        "Vitamin A",
        "Vitamin C",
        "Vitamin K",
        "Vitamin B12",
        "Vitamin K",
    ),

    q(
        "Nutrition",
        "Which nutrient is the main source of energy for the human body?",
        "Carbohydrates",
        "Vitamins",
        "Minerals",
        "Water",
        "Carbohydrates",
    ),

    q(
        "Nutrition",
        "Which nutrient is essential for growth and repair of body tissues?",
        "Protein",
        "Water",
        "Minerals",
        "Carbohydrate",
        "Protein",
    ),

    q(
        "Nutrition",
        "Which vitamin deficiency causes scurvy?",
        "Vitamin A",
        "Vitamin B12",
        "Vitamin C",
        "Vitamin D",
        "Vitamin C",
    ),

    q(
        "Nutrition",
        "Which vitamin deficiency can cause night blindness?",
        "Vitamin A",
        "Vitamin B",
        "Vitamin C",
        "Vitamin K",
        "Vitamin A",
    ),

    q(
        "Nutrition",
        "Deficiency of vitamin D can lead to:",
        "Scurvy",
        "Rickets",
        "Beriberi",
        "Pellagra",
        "Rickets",
    ),

    q(
        "Nutrition",
        "Which mineral is essential for the formation of haemoglobin?",
        "Calcium",
        "Iron",
        "Sodium",
        "Potassium",
        "Iron",
    ),

    q(
        "Nutrition",
        "Which mineral is especially important for strong bones and teeth?",
        "Calcium",
        "Iron",
        "Sodium",
        "Iodine",
        "Calcium",
    ),

    q(
        "Nutrition",
        "Iodine deficiency may cause:",
        "Goitre",
        "Scurvy",
        "Rickets",
        "Anaemia",
        "Goitre",
    ),

    q(
        "Nutrition",
        "Which nutrient provides the highest energy per gram?",
        "Protein",
        "Carbohydrate",
        "Fat",
        "Vitamin",
        "Fat",
    ),

    q(
        "Nutrition",
        "Which of the following is a good source of dietary fibre?",
        "Whole grains",
        "Refined sugar",
        "Butter",
        "Salt",
        "Whole grains",
    ),

    q(
        "Public Health",
        "Which practice is most effective for preventing many infectious diseases?",
        "Poor sanitation",
        "Hand hygiene",
        "Sharing personal items",
        "Avoiding clean water",
        "Hand hygiene",
    ),

    q(
        "Public Health",
        "Safe drinking water is important mainly for preventing:",
        "Water-borne diseases",
        "Genetic disorders",
        "Bone fractures",
        "Eye colour changes",
        "Water-borne diseases",
    ),

    q(
        "Public Health",
        "Which disease is commonly transmitted through contaminated water?",
        "Cholera",
        "Malaria",
        "Rabies",
        "Tuberculosis",
        "Cholera",
    ),

    q(
        "Public Health",
        "Which disease is caused by the Plasmodium parasite?",
        "Malaria",
        "Typhoid",
        "Cholera",
        "Dengue",
        "Malaria",
    ),

    q(
        "Public Health",
        "Malaria is mainly transmitted by:",
        "Housefly",
        "Female Anopheles mosquito",
        "Tick",
        "Rat",
        "Female Anopheles mosquito",
    ),

    q(
        "Public Health",
        "Dengue is mainly transmitted by:",
        "Aedes mosquito",
        "Anopheles mosquito",
        "Housefly",
        "Flea",
        "Aedes mosquito",
    ),

    q(
        "Public Health",
        "Tuberculosis primarily affects the:",
        "Lungs",
        "Kidneys only",
        "Skin only",
        "Bones only",
        "Lungs",
    ),

    q(
        "Public Health",
        "Which disease is caused by a bacterium called Mycobacterium tuberculosis?",
        "Malaria",
        "Tuberculosis",
        "Dengue",
        "Cholera",
        "Tuberculosis",
    ),

    q(
        "Public Health",
        "Which disease is commonly associated with contaminated food and water and caused by Salmonella Typhi?",
        "Typhoid",
        "Malaria",
        "Dengue",
        "Rabies",
        "Typhoid",
    ),

    q(
        "Public Health",
        "Which disease is caused by a virus and can be transmitted through the bite of an infected animal?",
        "Rabies",
        "Typhoid",
        "Malaria",
        "Cholera",
        "Rabies",
    ),

    q(
        "Disease Prevention",
        "Vaccination primarily helps the body to develop:",
        "Immunity",
        "Dehydration",
        "Anaemia",
        "Fractures",
        "Immunity",
    ),

    q(
        "Disease Prevention",
        "Which type of immunity develops after vaccination?",
        "Acquired active immunity",
        "Inherited immunity",
        "Mechanical immunity",
        "Nutritional immunity",
        "Acquired active immunity",
    ),

    q(
        "Disease Prevention",
        "Which of the following is a communicable disease?",
        "Diabetes",
        "Tuberculosis",
        "Hypertension",
        "Cancer",
        "Tuberculosis",
    ),

    q(
        "Disease Prevention",
        "Which of the following is generally a non-communicable disease?",
        "Malaria",
        "Tuberculosis",
        "Diabetes",
        "Cholera",
        "Diabetes",
    ),

    q(
        "Disease Prevention",
        "Quarantine is primarily used to:",
        "Separate people who may have been exposed to an infectious disease",
        "Treat fractures",
        "Increase blood pressure",
        "Improve eyesight",
        "Separate people who may have been exposed to an infectious disease",
    ),

    q(
        "First Aid",
        "What is the first priority when providing first aid at an accident scene?",
        "Ensure safety of the scene",
        "Give food immediately",
        "Move every injured person immediately",
        "Give medication without assessment",
        "Ensure safety of the scene",
    ),

    q(
        "First Aid",
        "CPR stands for:",
        "Cardiopulmonary Resuscitation",
        "Cardiac Pulse Recovery",
        "Circulatory Pressure Response",
        "Cardiovascular Protection Routine",
        "Cardiopulmonary Resuscitation",
    ),

    q(
        "First Aid",
        "CPR is primarily performed when a person is:",
        "Unresponsive and not breathing normally",
        "Hungry",
        "Sleeping normally",
        "Suffering from a minor cut",
        "Unresponsive and not breathing normally",
    ),

    q(
        "First Aid",
        "For a minor burn, the affected area should generally be:",
        "Cooled with clean running water",
        "Covered with mud",
        "Rubbed vigorously",
        "Covered with toothpaste",
        "Cooled with clean running water",
    ),

    q(
        "First Aid",
        "What is an important immediate measure for severe external bleeding?",
        "Apply direct pressure with a clean dressing",
        "Give solid food",
        "Massage the wound",
        "Apply soil",
        "Apply direct pressure with a clean dressing",
    ),

    q(
        "Health Awareness",
        "Which organ removes many harmful substances from the blood and helps metabolize nutrients?",
        "Liver",
        "Heart",
        "Lungs",
        "Spleen",
        "Liver",
    ),

    q(
        "Health Awareness",
        "Which measurement is commonly used to assess body temperature?",
        "Thermometer",
        "Stethoscope",
        "Sphygmomanometer",
        "Glucometer",
        "Thermometer",
    ),

    q(
        "Health Awareness",
        "Which instrument is commonly used to measure blood pressure?",
        "Thermometer",
        "Sphygmomanometer",
        "Stethoscope only",
        "Pulse oximeter",
        "Sphygmomanometer",
    ),

    q(
        "Health Awareness",
        "Which device is commonly used to measure oxygen saturation in the blood?",
        "Pulse oximeter",
        "Thermometer",
        "Glucometer",
        "Spirometer",
        "Pulse oximeter",
    ),

    q(
        "Health Awareness",
        "Which measurement is commonly used to monitor blood glucose?",
        "Glucometer",
        "Thermometer",
        "Sphygmomanometer",
        "Otoscope",
        "Glucometer",
    ),

]

REVENUE_DEPARTMENT_QUESTIONS = [

    q(
        "Revenue Administration",
        "Which department is primarily responsible for maintaining land and revenue records at the district level?",
        "Revenue Department",
        "Transport Department",
        "Health Department",
        "Education Department",
        "Revenue Department",
    ),

    q(
        "Revenue Administration",
        "Who is generally the head of district administration?",
        "District Collector",
        "District Judge",
        "Superintendent of Police",
        "Municipal Commissioner",
        "District Collector",
    ),

    q(
        "Revenue Administration",
        "The District Collector is primarily responsible for:",
        "District revenue and general administration",
        "Conducting university examinations",
        "Managing railway stations",
        "Issuing passports",
        "District revenue and general administration",
    ),

    q(
        "Revenue Administration",
        "Who generally assists the District Collector in revenue administration at the divisional level?",
        "Revenue Divisional Officer",
        "Station House Officer",
        "District Medical Officer",
        "Municipal Engineer",
        "Revenue Divisional Officer",
    ),

    q(
        "Revenue Administration",
        "RDO commonly stands for:",
        "Revenue Divisional Officer",
        "Regional Development Officer",
        "Rural District Officer",
        "Revenue District Organizer",
        "Revenue Divisional Officer",
    ),

    q(
        "Revenue Administration",
        "A Mandal Revenue Officer is generally associated with:",
        "Mandal-level revenue administration",
        "State-level policing",
        "District-level healthcare",
        "Municipal engineering",
        "Mandal-level revenue administration",
    ),

    q(
        "Revenue Administration",
        "MRO commonly refers to:",
        "Mandal Revenue Officer",
        "Municipal Revenue Officer",
        "Main Revenue Organizer",
        "Mandal Registration Officer",
        "Mandal Revenue Officer",
    ),

    q(
        "Revenue Records",
        "Which records are primarily maintained to document ownership and possession of land?",
        "Land records",
        "Hospital records",
        "School records",
        "Vehicle records",
        "Land records",
    ),

    q(
        "Revenue Records",
        "A survey number is primarily used to:",
        "Identify a parcel of land",
        "Identify a vehicle",
        "Identify a voter",
        "Identify a court case",
        "Identify a parcel of land",
    ),

    q(
        "Revenue Records",
        "A village map is mainly useful for:",
        "Showing land parcels and boundaries",
        "Recording school attendance",
        "Recording births",
        "Recording vehicle ownership",
        "Showing land parcels and boundaries",
    ),

    q(
        "Revenue Records",
        "Mutation of land records generally refers to:",
        "Updating records after a change in ownership or rights",
        "Changing the physical location of land",
        "Changing the district boundary",
        "Constructing a new road",
        "Updating records after a change in ownership or rights",
    ),

    q(
        "Revenue Records",
        "A land title primarily indicates:",
        "Legal ownership or rights over land",
        "The crop grown on land",
        "The rainfall received",
        "The market price of vegetables",
        "Legal ownership or rights over land",
    ),

    q(
        "Revenue Records",
        "A land survey is generally conducted to determine:",
        "Location, area and boundaries of land parcels",
        "Population of a village only",
        "Number of schools",
        "Number of hospitals",
        "Location, area and boundaries of land parcels",
    ),

    q(
        "Revenue Records",
        "The process of measuring and recording land parcels is known as:",
        "Land survey",
        "Land taxation",
        "Land cultivation",
        "Land marketing",
        "Land survey",
    ),

    q(
        "Revenue Records",
        "A cadastral map generally represents:",
        "Individual land parcels and their boundaries",
        "Weather conditions",
        "Railway routes only",
        "Population statistics only",
        "Individual land parcels and their boundaries",
    ),

    q(
        "Land Administration",
        "Land revenue is generally associated with:",
        "Revenue collected in relation to land",
        "Income from railway tickets",
        "Hospital charges",
        "School fees",
        "Revenue collected in relation to land",
    ),

    q(
        "Land Administration",
        "The primary purpose of maintaining accurate land records is to:",
        "Establish and document land rights and transactions",
        "Increase rainfall",
        "Control traffic",
        "Conduct elections",
        "Establish and document land rights and transactions",
    ),

    q(
        "Land Administration",
        "Which document may contain details relating to ownership and land rights?",
        "Record of Rights",
        "Driving licence",
        "Passport",
        "Birth certificate",
        "Record of Rights",
    ),

    q(
        "Land Administration",
        "ROR in land administration commonly refers to:",
        "Record of Rights",
        "Register of Revenue",
        "Report of Registration",
        "Record of Roads",
        "Record of Rights",
    ),

    q(
        "Land Administration",
        "Encroachment generally means:",
        "Unauthorised occupation or use of land",
        "Legal purchase of land",
        "Registration of land",
        "Survey of land",
        "Unauthorised occupation or use of land",
    ),

    q(
        "Land Administration",
        "A boundary dispute generally concerns:",
        "The location or extent of property boundaries",
        "Income tax",
        "Vehicle registration",
        "School admission",
        "The location or extent of property boundaries",
    ),

    q(
        "Land Administration",
        "Which authority generally deals with revenue-related matters at the village or mandal level?",
        "Revenue administration",
        "Railway administration",
        "Postal administration",
        "Airport administration",
        "Revenue administration",
    ),

    q(
        "Land Administration",
        "Land classification is primarily concerned with:",
        "Identifying the nature or category of land",
        "Identifying voters",
        "Identifying vehicles",
        "Identifying hospitals",
        "Identifying the nature or category of land",
    ),

    q(
        "Land Administration",
        "Government land is land that is:",
        "Owned or controlled by the government",
        "Always privately owned",
        "Owned by a bank",
        "Owned by a school",
        "Owned or controlled by the government",
    ),

    q(
        "Land Administration",
        "Assignment of government land generally refers to:",
        "Granting land rights to eligible persons under applicable rules",
        "Selling all government land automatically",
        "Changing district boundaries",
        "Conducting a land survey",
        "Granting land rights to eligible persons under applicable rules",
    ),

    q(
        "Telangana Administration",
        "Telangana is divided into administrative districts for:",
        "Efficient administration and governance",
        "Conducting international trade",
        "Managing railway zones only",
        "Managing airports only",
        "Efficient administration and governance",
    ),

    q(
        "Telangana Administration",
        "The basic rural administrative unit below the district in Telangana is commonly:",
        "Mandal",
        "State",
        "Parliament",
        "Division of a city only",
        "Mandal",
    ),

    q(
        "Telangana Administration",
        "A village is generally administered at the local level through:",
        "Local self-government institutions",
        "High Court",
        "Parliament",
        "Railway Board",
        "Local self-government institutions",
    ),

    q(
        "Telangana Administration",
        "The Gram Panchayat is primarily concerned with:",
        "Local rural administration and development",
        "High Court proceedings",
        "Railway operations",
        "Income tax assessment",
        "Local rural administration and development",
    ),

    q(
        "Telangana Administration",
        "The elected head of a Gram Panchayat is generally known as:",
        "Sarpanch",
        "Collector",
        "Tahsildar",
        "Governor",
        "Sarpanch",
    ),

    q(
        "Disaster Management",
        "The District Collector often plays an important role in:",
        "District-level disaster management",
        "Operating trains",
        "Managing universities",
        "Issuing passports",
        "District-level disaster management",
    ),

    q(
        "Disaster Management",
        "During floods, district administration primarily coordinates:",
        "Relief and rescue operations",
        "Railway ticket sales",
        "School examinations only",
        "Vehicle manufacturing",
        "Relief and rescue operations",
    ),

    q(
        "Disaster Management",
        "Which activity is important during a natural disaster?",
        "Evacuation of people from unsafe areas",
        "Ignoring warnings",
        "Blocking emergency services",
        "Destroying relief material",
        "Evacuation of people from unsafe areas",
    ),

    q(
        "Disaster Management",
        "A district emergency response system is primarily intended to:",
        "Coordinate emergency response and relief",
        "Collect school fees",
        "Register vehicles",
        "Conduct sports events",
        "Coordinate emergency response and relief",
    ),

    q(
        "Revenue Law",
        "A legal dispute regarding ownership of land may ultimately be decided by:",
        "A competent court or authority according to law",
        "A private shopkeeper",
        "A school teacher",
        "A bank cashier",
        "A competent court or authority according to law",
    ),

    q(
        "Revenue Law",
        "Registration of a land transaction primarily provides:",
        "Official recording of the transaction",
        "Automatic construction permission",
        "Automatic agricultural production",
        "Automatic loan approval",
        "Official recording of the transaction",
    ),

    q(
        "Revenue Law",
        "A registered sale deed is primarily evidence of:",
        "A formally recorded property transaction",
        "A school examination result",
        "A medical diagnosis",
        "A police appointment",
        "A formally recorded property transaction",
    ),

    q(
        "Revenue Law",
        "Stamp duty is generally associated with:",
        "Certain legal instruments and property transactions",
        "School examinations",
        "Hospital admissions",
        "Vehicle fuel",
        "Certain legal instruments and property transactions",
    ),

    q(
        "Revenue Law",
        "Property registration is generally carried out through:",
        "The appropriate registration authority",
        "A police station only",
        "A school office",
        "A railway station",
        "The appropriate registration authority",
    ),

    q(
        "Agriculture",
        "Which record is particularly important for identifying agricultural land holdings?",
        "Land record",
        "Passport",
        "Driving licence",
        "Birth certificate",
        "Land record",
    ),

    q(
        "Agriculture",
        "Crop information recorded in revenue records can help administration in:",
        "Agricultural and relief planning",
        "Issuing passports",
        "Conducting court trials",
        "Operating trains",
        "Agricultural and relief planning",
    ),

    q(
        "Agriculture",
        "Crop damage assessment is particularly important after:",
        "Natural calamities",
        "School examinations",
        "Vehicle registration",
        "Passport renewal",
        "Natural calamities",
    ),

    q(
        "Agriculture",
        "Drought primarily refers to:",
        "A prolonged period of insufficient rainfall",
        "Excessive rainfall every day",
        "A rise in sea level only",
        "An increase in forest cover",
        "A prolonged period of insufficient rainfall",
    ),

    q(
        "Agriculture",
        "Flood damage assessment may be used for:",
        "Planning relief and compensation according to applicable rules",
        "Issuing driving licences",
        "Conducting elections only",
        "Managing railway tickets",
        "Planning relief and compensation according to applicable rules",
    ),

    q(
        "Public Administration",
        "The main purpose of e-governance in revenue administration is to:",
        "Provide faster and more transparent public services",
        "Eliminate all government records",
        "Stop citizen services",
        "Prevent record keeping",
        "Provide faster and more transparent public services",
    ),

    q(
        "Public Administration",
        "Digitisation of land records can help reduce:",
        "Record loss and manual errors",
        "Agricultural production",
        "Road construction",
        "Rainfall",
        "Record loss and manual errors",
    ),

    q(
        "Public Administration",
        "A public grievance system allows citizens to:",
        "Submit complaints or requests to government authorities",
        "Issue court judgments",
        "Arrest persons",
        "Make laws directly",
        "Submit complaints or requests to government authorities",
    ),

    q(
        "Public Administration",
        "Transparency in land administration is important because it:",
        "Improves public access to reliable information",
        "Prevents record maintenance",
        "Removes legal procedures",
        "Stops land surveys",
        "Improves public access to reliable information",
    ),

    q(
        "General Awareness",
        "Which constitutional principle requires government authorities to act according to law?",
        "Rule of law",
        "Rule of wealth",
        "Rule of force",
        "Rule of business",
        "Rule of law",
    ),

    q(
        "General Awareness",
        "Which body is primarily responsible for local rural self-government?",
        "Panchayati Raj institutions",
        "Supreme Court",
        "Railway Board",
        "Reserve Bank of India",
        "Panchayati Raj institutions",
    ),

    q(
        "General Awareness",
        "The 73rd Constitutional Amendment is mainly associated with:",
        "Panchayati Raj institutions",
        "Urban municipalities",
        "Supreme Court",
        "Election Commission",
        "Panchayati Raj institutions",
    ),

    q(
        "General Awareness",
        "The 74th Constitutional Amendment is mainly associated with:",
        "Urban local bodies",
        "Panchayati Raj institutions",
        "Supreme Court",
        "District courts",
        "Urban local bodies",
    ),

    q(
        "General Awareness",
        "Good revenue administration primarily requires:",
        "Accurate records, transparency and timely public service",
        "No record keeping",
        "No public access",
        "Manual errors",
        "Accurate records, transparency and timely public service",
    ),
]


# ============================================================
# QUESTION BANK
# ============================================================

QUESTION_BANK = {
    "Air Force": AIR_FORCE,
    "Army": ARMY,
    "Banking": BANKING_QUESTIONS,
    "RRB ALP": RRB_ALP_QUESTIONS,
    "RRB Technician": RRB_TECHNICIAN_QUESTIONS,
    "RRB JE": RRB_JE_QUESTIONS,

    "Railway Constable": RAILWAY_CONSTABLE_QUESTIONS,
    "Railway SI": RAILWAY_SI_QUESTIONS,

    "Forest Range Officer": FOREST_RANGE_OFFICER_QUESTIONS,
    
    "UPSC": UPSC_QUESTIONS,
    "UPSC CSE": UPSC_CSE_QUESTIONS,

    "Telangana Police Constable": TELANGANA_POLICE_CONSTABLE_QUESTIONS,
    "Telangana Police SI": TELANGANA_POLICE_SI_QUESTIONS,

     "Telangana AE": TELANGANA_AE_QUESTIONS,
    "Telangana AEE": TELANGANA_AEE_QUESTIONS,

    "DSC": DSC_QUESTIONS,

    "High Court": HIGH_COURT_QUESTIONS,
    "District Court": DISTRICT_COURT_QUESTIONS,

    "Health Department": HEALTH_DEPARTMENT_QUESTIONS,

    "Revenue Department": REVENUE_DEPARTMENT_QUESTIONS,




}


# ============================================================
# DJANGO COMMAND
# ============================================================

class Command(BaseCommand):

    help = "Import exam-specific mock test questions"

    def handle(self, *args, **options):

        total_added = 0

        for exam_name, questions in QUESTION_BANK.items():

            exam = Exam.objects.filter(
                name__iexact=exam_name
            ).first()

            if not exam:
                self.stdout.write(
                    self.style.WARNING(
                        f"Exam not found: {exam_name}"
                    )
                )
                continue

            added = 0

            for data in questions:

                # Do not insert duplicate question text
                exists = MockTestQuestion.objects.filter(
                    exam=exam,
                    question=data["question"],
                ).exists()

                if exists:
                    continue

                MockTestQuestion.objects.create(
                    exam=exam,
                    exam_name=exam.name,
                    subject=data["subject"],
                    question=data["question"],
                    option1=data["option1"],
                    option2=data["option2"],
                    option3=data["option3"],
                    option4=data["option4"],
                    answer=data["answer"],
                    explanation=f"Correct answer: {data['answer']}",
                    difficulty=data["difficulty"],
                    source="GovtJobs Question Bank",
                    is_active=True,
                )

                added += 1
                total_added += 1

            final_count = MockTestQuestion.objects.filter(
                exam=exam,
                is_active=True
            ).count()

            self.stdout.write(
                self.style.SUCCESS(
                    f"{exam.name}: added {added}, total {final_count}"
                )
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"\nCompleted. Total questions added: {total_added}"
            )
        )