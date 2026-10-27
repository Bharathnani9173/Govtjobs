import os
import django
from datetime import date

# ---------------------------------------------------------
# Django setup
# ---------------------------------------------------------
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from jobportal.models import CurrentAffair


# ---------------------------------------------------------
# 1950–1960
# EARLY REPUBLIC & NATION BUILDING
# ---------------------------------------------------------

history_data = [

    {
        "title": "1. India Begins Its Republican Journey — 1950",
        "date": date(1950, 1, 26),
        "description": """
On 26 January 1950, the Constitution of India came into force and India became a Republic.

This was one of the most important turning points in modern Indian history. India had become independent in 1947, but during the first years after independence it continued to function under a transitional constitutional arrangement.

The Constitution established India as a democratic Republic and created the basic institutions of the new political system.

The President became the constitutional head of the Union, while the Prime Minister and Council of Ministers became responsible for running the government under the parliamentary system.

Dr. Rajendra Prasad became the first President of India, while Jawaharlal Nehru continued as the first Prime Minister.

However, the Republic still faced enormous challenges.

The country was dealing with the consequences of Partition, refugee rehabilitation, poverty, food shortages, illiteracy, limited industrial development and the task of creating a unified administrative system.

The 1950s therefore became a decade of institution-building and nation-building.
""",
    },

    {
        "title": "2. The First Years of the Republic",
        "date": date(1950, 1, 26),
        "description": """
The early years of the Republic were a period of major political, economic and social transformation.

India inherited an economy in which agriculture employed a large part of the population. Industrial development was still limited, infrastructure was inadequate in many regions and literacy levels were low.

The government therefore had to address several problems simultaneously.

Important priorities included agricultural production, irrigation, electricity, transport, education, healthcare, employment and rural development.

The government also had to establish effective relations between the Union and State governments.

The Constitution provided the legal framework, but the practical institutions of democracy had to be developed through experience.

The first decade of the Republic therefore saw the creation and strengthening of institutions such as Parliament, the Election Commission, the judiciary, planning institutions and democratic local administration.

The decade also witnessed the first general election and major changes to the political map of India.
""",
    },

    {
        "title": "3. Dr. Rajendra Prasad and the Presidency",
        "date": date(1950, 1, 26),
        "description": """
Dr. Rajendra Prasad became the first President of India on 26 January 1950.

Before becoming President, he had played an important role in the national movement and had served as President of the Constituent Assembly.

The Constitution created the office of President as the constitutional head of the Union.

India adopted a parliamentary form of government. Under this system, the President is the constitutional head, while the elected government headed by the Prime Minister is responsible for day-to-day administration.

Rajendra Prasad's presidency coincided with the establishment of the institutions of the new Republic.

During the 1950s, India was developing its parliamentary traditions, strengthening its administrative system and conducting its first nationwide democratic elections.

His presidency therefore belongs to one of the foundational periods of the Indian Republic.
""",
    },

    {
        "title": "4. Election Commission and Universal Adult Franchise",
        "date": date(1950, 1, 25),
        "description": """
The Election Commission of India was established on 25 January 1950.

Its creation was essential for the functioning of India's new democratic system.

One of the most important features of the Constitution was the adoption of universal adult franchise.

This meant that ordinary adult citizens would participate in choosing representatives through elections.

The decision was significant because independent India had a very large population, widespread poverty and comparatively low literacy.

Preparing electoral rolls was therefore a huge administrative undertaking.

Citizens had to be registered, constituencies had to be organised and election procedures had to be established.

The Election Commission became one of the important institutions responsible for conducting elections to Parliament and State legislatures.

The establishment of the Commission demonstrated that democratic government was intended to become a practical reality rather than merely a constitutional principle.
""",
    },

    {
        "title": "5. First General Election — 1951–1952",
        "date": date(1951, 10, 25),
        "description": """
India held its first general election during 1951–52.

The election was an enormous administrative exercise.

The government and Election Commission had to prepare electoral rolls, establish constituencies, arrange polling stations, print ballot papers, provide ballot boxes and train election personnel.

India's relatively low literacy rate also influenced the design of the electoral process.

Election symbols became an important way of identifying political parties and candidates.

Millions of citizens participated in the election.

The election resulted in the formation of India's first elected Parliament under the Constitution.

The first general election demonstrated that the constitutional commitment to representative democracy could be implemented on a very large scale.

It became one of the defining events of the early Republic.
""",
    },

    {
        "title": "6. Parliament and the Development of Parliamentary Democracy",
        "date": date(1952, 4, 17),
        "description": """
The first elected Parliament began functioning after the first general election.

India's parliamentary system was based on the principle that the executive should remain accountable to the elected legislature.

The Lok Sabha represented the directly elected representatives of the people, while the Rajya Sabha represented the States and Union territories within the constitutional framework.

Parliament became an important forum for discussing national policies, legislation, taxation and development programmes.

During the 1950s, parliamentary procedures and conventions were gradually established.

The first decade of the Republic was therefore important not only because elections were conducted, but also because institutions developed the practical traditions required for parliamentary democracy.

The functioning of Parliament became a central part of India's new constitutional system.
""",
    },

    {
        "title": "7. Planning Commission and the First Five-Year Plan",
        "date": date(1950, 3, 15),
        "description": """
Economic development was one of the most important challenges facing independent India.

The Planning Commission was established in March 1950.

Its purpose was to assess national resources and help formulate development plans.

The First Five-Year Plan covered the period from 1951 to 1956.

The plan concentrated strongly on agriculture, irrigation and rural development because food production was an urgent national priority.

It also included programmes involving power, transport, employment, social services and infrastructure.

The planning approach attempted to coordinate national resources and development priorities.

The First Plan represented India's first major attempt to organise economic development through a comprehensive national planning framework.

It laid the foundation for subsequent Five-Year Plans.
""",
    },

    {
        "title": "8. Agriculture, Irrigation and Rural Development",
        "date": date(1951, 4, 1),
        "description": """
Agriculture received major attention during the First Five-Year Plan.

At independence, a large part of India's population depended directly or indirectly on agriculture.

Partition had also created additional food and agricultural problems.

Increasing agricultural production was therefore essential for food security and economic stability.

The government invested in irrigation, agricultural development, rural infrastructure and community development.

Large irrigation and power projects were also taken up.

The objective was to increase agricultural production while improving rural living conditions.

Community development programmes attempted to bring development activities into villages through improvements in agriculture, roads, education, health, sanitation and local facilities.

Agricultural development during the 1950s became an important foundation for later changes in Indian agriculture.
""",
    },

    {
        "title": "9. Community Development and Rural India",
        "date": date(1952, 10, 2),
        "description": """
The development of rural India was considered essential for national development.

A large majority of India's population lived in villages during the early years of the Republic.

The government therefore introduced programmes aimed at improving village life.

Community development focused on areas such as agriculture, education, health, sanitation, roads, drinking water and local economic activity.

The basic idea was that rural communities should participate in their own development.

The programme also attempted to connect government development programmes with local communities.

Although the results varied between regions, the effort represented an important change from colonial administration towards planned social and economic development.

Rural development remained an important objective throughout the subsequent Five-Year Plans.
""",
    },

    {
        "title": "10. Large Dams, Irrigation and Power Projects",
        "date": date(1950, 1, 26),
        "description": """
The 1950s witnessed the construction and expansion of major irrigation and power projects.

Projects such as Bhakra-Nangal, Damodar Valley and Hirakud became associated with India's development strategy.

Large projects were expected to provide several benefits.

These included irrigation for agriculture, generation of electricity, flood control, industrial development and support for economic growth.

The projects represented the belief that modern infrastructure was necessary for transforming India's largely agricultural economy.

Large dams also became symbols of India's development ambitions.

During the First Five-Year Plan, irrigation and power received substantial attention because agricultural production and industrial development both depended on reliable water and electricity.

These projects contributed to the physical infrastructure of the developing Republic.
""",
    },

    {
        "title": "11. Industrial Development in the 1950s",
        "date": date(1952, 1, 1),
        "description": """
Industrial development became an increasingly important part of India's economic strategy during the 1950s.

At independence, India's industrial base was limited and concentrated in selected sectors.

The government believed that India needed to develop its own industrial and technological capacity.

Public-sector enterprises therefore received increasing attention.

Industries associated with steel, machinery, engineering, mining, electricity and transport were considered important for long-term development.

The government also supported small-scale and cottage industries.

The First Five-Year Plan concentrated more heavily on agriculture and immediate development needs, while the Second Five-Year Plan placed much greater emphasis on industrialisation.

This transition marked an important stage in India's attempt to become a more industrialised economy.
""",
    },

    {
        "title": "12. Second Five-Year Plan — 1956–1961",
        "date": date(1956, 4, 1),
        "description": """
The Second Five-Year Plan began in 1956.

Compared with the First Plan, it placed much greater emphasis on industrialisation.

The strategy focused on developing basic and heavy industries that could provide machinery and capital goods needed for future economic growth.

Important areas included steel, heavy engineering, machine-building, mining, power and transport.

Economist P. C. Mahalanobis played an important role in the economic thinking associated with the Second Plan.

The plan aimed to build a stronger industrial base and increase the role of the public sector.

The Second Plan therefore represented an important change in India's development strategy.

While agriculture continued to receive attention, industrialisation became a central feature of national economic planning.
""",
    },

    {
        "title": "13. Foreign Policy and Non-Alignment",
        "date": date(1950, 1, 26),
        "description": """
India's foreign policy during the 1950s developed in the context of the Cold War.

The United States and Soviet Union were the major competing powers in the international system.

India did not formally join the military alliances associated with either bloc.

Jawaharlal Nehru and other Indian leaders emphasised an independent foreign policy.

India supported peaceful coexistence, national independence and opposition to colonialism and racial discrimination.

This approach later became associated with the Non-Aligned Movement.

The formal Non-Aligned Movement was established in 1961, but the ideas and diplomatic relationships associated with non-alignment developed during the 1950s.

India also became active in international diplomacy and supported the use of peaceful methods for resolving international disputes.
""",
    },

    {
        "title": "14. India and China — Panchsheel",
        "date": date(1954, 4, 29),
        "description": """
Relations between India and China were an important part of India's foreign policy during the 1950s.

India initially sought friendly relations with the People's Republic of China.

In 1954, India and China became associated with the Five Principles of Peaceful Coexistence, commonly known as Panchsheel.

The principles were:

1. Mutual respect for territorial integrity and sovereignty.
2. Mutual non-aggression.
3. Mutual non-interference in internal affairs.
4. Equality and mutual benefit.
5. Peaceful coexistence.

These principles became an important part of India's diplomatic approach during the 1950s.

However, relations between India and China later became increasingly difficult because of territorial disputes.

The developments of the 1950s therefore provide important background for understanding the India-China conflict that emerged in the following decade.
""",
    },

    {
        "title": "15. Language Question and Reorganisation of States",
        "date": date(1953, 1, 1),
        "description": """
The organisation of India's States became one of the major political questions of the 1950s.

India was a country of many languages, cultures and regional identities.

After independence, demands emerged for States to be reorganised according to linguistic and regional considerations.

Supporters argued that administration would become easier when people sharing a major language and cultural identity were brought into the same State.

The central government also had to consider economic viability, geographical factors, administrative efficiency and national unity.

The demand for a separate Telugu-speaking State became particularly important.

The creation of Andhra State in 1953 was a major turning point.

It encouraged further demands for linguistic reorganisation across India.

The Government of India subsequently appointed the States Reorganisation Commission.
""",
    },

    {
        "title": "16. Potti Sreeramulu and Creation of Andhra State — 1953",
        "date": date(1952, 12, 15),
        "description": """
The demand for a separate Telugu-speaking State became an important political issue in the early 1950s.

Potti Sreeramulu undertook a prolonged fast demanding a separate State for Telugu-speaking people.

He died in December 1952 after his fast.

His death resulted in intensified public mobilisation and pressure for the creation of a separate Telugu-speaking State.

The Government of India subsequently moved towards establishing Andhra State.

The Andhra State Act, 1953 provided the legal basis for the creation of the State.

Andhra State came into existence on 1 October 1953.

The creation of Andhra State became a major milestone in the reorganisation of India's internal political boundaries.

It also influenced the subsequent movement towards linguistic reorganisation of other States.
""",
    },

    {
        "title": "17. States Reorganisation Commission",
        "date": date(1953, 12, 29),
        "description": """
The creation of Andhra State demonstrated that the question of linguistic States required a broader national solution.

The Government of India therefore appointed the States Reorganisation Commission in 1953.

The Commission examined India's State boundaries and considered several factors.

These included language, culture, administration, economic considerations, geographical factors and national unity.

The Commission submitted its report in 1955.

Its recommendations became an important basis for the reorganisation of India's States.

The process eventually resulted in the States Reorganisation Act of 1956.

The reorganisation represented one of the largest peaceful administrative transformations undertaken by the young Republic.
""",
    },

    {
        "title": "18. States Reorganisation Act — 1956",
        "date": date(1956, 8, 31),
        "description": """
The States Reorganisation Act, 1956 was one of the most important laws of the decade.

The Act was enacted on 31 August 1956.

It provided for major changes to the boundaries and organisation of India's States.

Language was an important consideration, although the reorganisation also involved geographical, administrative and economic factors.

The Act significantly changed India's political map.

The former Hyderabad State was divided as part of the reorganisation.

Its Telugu-speaking areas were transferred to the newly formed Andhra Pradesh, while other areas were associated with neighbouring States.

The reorganisation therefore had major consequences for the political geography of South India.

The Act came into effect along with the wider reorganisation on 1 November 1956.
""",
    },

    {
        "title": "19. Formation of Andhra Pradesh — 1 November 1956",
        "date": date(1956, 11, 1),
        "description": """
The formation of Andhra Pradesh was an important event in the political history of the Telugu-speaking regions.

Andhra State had already been created in 1953.

During the States Reorganisation process, the Telugu-speaking areas of the former Hyderabad State were combined with Andhra State.

The new State of Andhra Pradesh came into existence on 1 November 1956.

Hyderabad became the capital of the new State.

The formation of Andhra Pradesh represented the implementation of linguistic reorganisation in the Telugu-speaking regions.

The event is particularly important for understanding the later political history of Andhra Pradesh and Telangana.

The 1956 reorganisation also demonstrated the flexibility of India's federal system in responding to regional and linguistic demands.
""",
    },

    {
        "title": "20. Education, Science and National Institution Building",
        "date": date(1950, 1, 26),
        "description": """
The 1950s were also a period of institution-building in education, science and technology.

The government recognised that long-term economic development required trained professionals, scientists, engineers, doctors and administrators.

Universities and technical institutions received increasing attention.

Scientific research was considered important for industrial development and national self-reliance.

Engineering and scientific education expanded during the decade.

The government also promoted institutions that could support industrial and technological development.

These efforts created a foundation for India's later scientific and technical growth.

The development of higher education and scientific institutions was therefore closely connected with the wider national development strategy of the 1950s.
""",
    },

    {
        "title": "21. Important Timeline — 1950 to 1960",
        "date": date(1960, 12, 31),
        "description": """
IMPORTANT TIMELINE

25 January 1950
Election Commission of India established.

26 January 1950
Constitution came into force and India became a Republic.

March 1950
Planning Commission established.

1951
First Five-Year Plan began.

1951–1952
First general election held.

1952
First elected Parliament began functioning.

1953
Andhra State was created.

1953
States Reorganisation Commission was appointed.

1954
Panchsheel principles became associated with India-China relations.

1955
States Reorganisation Commission submitted its report.

1956
States Reorganisation Act was enacted.

1 November 1956
Major State reorganisation came into effect.

1 November 1956
Andhra Pradesh came into existence.

1956
Second Five-Year Plan began.

1950s
Major development took place in agriculture, irrigation, power, industry, education and scientific institutions.
""",
    },

    {
        "title": "22. Exam Revision Points — 1950 to 1960",
        "date": date(1960, 12, 31),
        "description": """
IMPORTANT EXAM POINTS

1. India became a Republic on 26 January 1950.

2. Dr. Rajendra Prasad was the first President of India.

3. The Election Commission of India was established on 25 January 1950.

4. The Planning Commission was established in March 1950.

5. India's first general election was held during 1951–52.

6. The First Five-Year Plan covered 1951–1956.

7. Agriculture and irrigation received major attention in the First Five-Year Plan.

8. Community development was an important part of rural development.

9. The Second Five-Year Plan began in 1956.

10. P. C. Mahalanobis is closely associated with the strategy of the Second Five-Year Plan.

11. India followed an independent foreign-policy approach during the Cold War.

12. Panchsheel was associated with India-China relations in 1954.

13. The Andhra State Act was enacted in 1953.

14. Andhra State came into existence on 1 October 1953.

15. The States Reorganisation Commission was appointed in 1953.

16. The States Reorganisation Act was enacted in 1956.

17. Major State reorganisation came into effect on 1 November 1956.

18. Andhra Pradesh came into existence on 1 November 1956.

19. Hyderabad became the capital of Andhra Pradesh in 1956.

20. The 1950s were a major period of democratic, economic, administrative and institutional nation-building.
""",
    },
]


# ---------------------------------------------------------
# IMPORT INTO DATABASE
# ---------------------------------------------------------

created = 0
updated = 0

for item in history_data:

    obj, was_created = CurrentAffair.objects.update_or_create(
        title=item["title"],
        defaults={
            "job": None,
            "period": "1950-1960",
            "category": "History",
            "date": item["date"],
            "description": item["description"].strip(),
            "pdf_link": "",
        },
    )

    if was_created:
        created += 1
    else:
        updated += 1


print("=" * 60)
print("1950–1960 HISTORY IMPORT COMPLETED")
print("=" * 60)
print(f"New records created : {created}")
print(f"Existing records updated : {updated}")
print(f"Total records processed : {len(history_data)}")
print("=" * 60)