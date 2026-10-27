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
# 1947–1950 Detailed Indian History
# ---------------------------------------------------------
history_data = [

    {
        "title": "1. The Road to Indian Independence",
        "date": date(1947, 8, 1),
        "description": """
India's independence in 1947 was the result of a long political struggle against British colonial rule. During the late nineteenth and early twentieth centuries, Indian political organisations increasingly demanded greater participation in government and eventually complete independence.

The Indian National Congress became one of the major organisations of the national movement. Leaders such as Mahatma Gandhi, Jawaharlal Nehru, Sardar Vallabhbhai Patel, Maulana Abul Kalam Azad and many others participated in different phases of the freedom movement.

Mahatma Gandhi's leadership gave the national movement a mass character through movements such as the Non-Cooperation Movement, Civil Disobedience Movement and Quit India Movement.

The Second World War greatly weakened Britain's economic and political position. At the same time, the demand for independence had become increasingly strong.

The Cabinet Mission came to India in 1946 to discuss the constitutional future of the country. Although several constitutional proposals were discussed, disagreements between political groups remained.

In 1947, the British government decided to transfer power and end British rule in India.
""",
    },

    {
        "title": "2. Indian Independence Act, 1947",
        "date": date(1947, 7, 18),
        "description": """
The Indian Independence Act, 1947 was passed by the British Parliament to provide the legal framework for the transfer of power.

The Act created two independent Dominions, India and Pakistan.

It ended the authority of the British Parliament to legislate for the new Dominions, subject to the constitutional arrangements of the transition period.

India became independent on 15 August 1947.

During the transitional period, India continued to function as a Dominion. The Government of India Act, 1935, with necessary adaptations, continued to provide an administrative and constitutional framework until the Constitution of India came into force in 1950.

The Indian Independence Act therefore formed an important legal bridge between British rule and independent India.
""",
    },

    {
        "title": "3. 15 August 1947 — India Becomes Independent",
        "date": date(1947, 8, 15),
        "description": """
On 15 August 1947, India became independent after nearly two centuries of British colonial rule.

Jawaharlal Nehru became the first Prime Minister of independent India.

Independence represented the achievement of a long national movement. However, the country immediately faced enormous challenges.

The new government had to deal with Partition, communal violence, refugee rehabilitation, food shortages, economic difficulties, administrative reorganisation and the integration of princely states.

India was initially a Dominion and was not yet a Republic. The constitutional transformation into a Republic would take place on 26 January 1950 when the Constitution came into force.

The year 1947 therefore marked both the end of colonial rule and the beginning of the difficult process of nation-building.
""",
    },

    {
        "title": "4. Partition of India and the Refugee Crisis",
        "date": date(1947, 8, 15),
        "description": """
The transfer of power in 1947 was accompanied by the Partition of British India and the creation of India and Pakistan.

Punjab and Bengal were divided, and the new borders resulted in one of the largest population movements of the twentieth century.

Millions of people crossed the new borders. Hindus and Sikhs moved largely towards India, while many Muslims moved towards Pakistan, although migration patterns were complex and not uniform.

The population movement was accompanied by serious communal violence and loss of property and livelihoods.

The government of independent India had to organise emergency relief, transport, temporary accommodation and long-term rehabilitation for displaced people.

The refugee crisis became one of the earliest major administrative and humanitarian challenges of independent India.

Partition also had a long-term effect on India's foreign relations, internal politics, society and security.
""",
    },

    {
        "title": "5. First Government of Independent India",
        "date": date(1947, 8, 15),
        "description": """
Jawaharlal Nehru became the first Prime Minister of independent India.

The first government inherited an administrative system that had been designed under colonial rule and had to adapt it to the needs of a democratic and independent country.

The immediate priorities included maintaining law and order, rehabilitating refugees, managing food and economic problems, integrating territories and establishing India's international position.

The government also had to continue the constitutional work being carried out by the Constituent Assembly.

India's early leadership therefore had to address both immediate crises and long-term institution building.

The first years of independence laid the administrative and political foundations on which the Republic would later develop.
""",
    },

    {
        "title": "6. Integration of the Princely States",
        "date": date(1947, 8, 15),
        "description": """
At the time of independence, the political map of the subcontinent included British Indian provinces as well as numerous princely states.

With the end of British paramountcy, the future relationship of these states with India and Pakistan became an important issue.

Sardar Vallabhbhai Patel, as Deputy Prime Minister and Home Minister, played a major role in India's integration process. Civil servant V. P. Menon was also closely involved in negotiations and administrative arrangements.

Many princely states joined India through Instruments of Accession and subsequent agreements.

The integration process was not identical everywhere. Different states presented different political and geographical circumstances.

The integration of the princely states was therefore a major part of the creation of a unified Indian Union after independence.

The National Archives preserves records relating to several former princely-state administrations, including Hyderabad and Jammu and Kashmir.
""",
    },

    {
        "title": "7. Junagadh",
        "date": date(1947, 11, 9),
        "description": """
Junagadh was a princely state in the Kathiawar region of present-day Gujarat.

Its ruler decided to accede to Pakistan in 1947. The decision created a political dispute because of the state's geographical position and the composition of its population.

The Indian government became involved in the situation.

Political and administrative developments followed, and the issue was eventually settled through a referendum held in February 1948.

The result supported the integration of Junagadh with India.

The Junagadh episode is an important example of the complex political problems created by the end of British paramountcy and the integration of princely states.
""",
    },

    {
        "title": "8. Jammu and Kashmir in 1947",
        "date": date(1947, 10, 26),
        "description": """
Jammu and Kashmir was a princely state located in a strategically important part of the northern subcontinent.

After independence, the state did not immediately become part of either India or Pakistan.

In October 1947, armed tribal forces entered the state. The political and military situation rapidly deteriorated.

Maharaja Hari Singh subsequently signed the Instrument of Accession to India.

Following the accession, Indian forces were deployed and fighting developed into the first India-Pakistan war after independence.

The conflict became an important part of India's early post-independence history and had continuing consequences for relations between India and Pakistan.

The National Archives holds records relating to Jammu and Kashmir, including historical records covering the period around the transition to independence.
""",
    },

    {
        "title": "9. Hyderabad and Integration into India",
        "date": date(1948, 9, 17),
        "description": """
Hyderabad was one of the largest princely states at the time of Indian independence.

The Nizam of Hyderabad initially sought to maintain Hyderabad's separate position rather than immediately joining the Indian Union.

Negotiations took place between the Government of India and the Hyderabad administration.

Political tensions increased during 1947 and 1948.

In September 1948, the Government of India conducted a military operation known as Operation Polo.

The operation resulted in the surrender of Hyderabad's forces and the integration of Hyderabad into the Indian Union.

The Hyderabad episode became an important part of India's post-independence territorial integration.

The National Archives preserves historical records concerning Hyderabad, including records covering the period before and around integration.
""",
    },

    {
        "title": "10. Mahatma Gandhi and His Assassination in 1948",
        "date": date(1948, 1, 30),
        "description": """
After independence and Partition, Mahatma Gandhi continued to work for communal peace and harmony.

The violence and displacement associated with Partition deeply affected the newly independent country.

Gandhi undertook efforts to promote peace between communities and travelled to areas affected by communal tension.

On 30 January 1948, Mahatma Gandhi was assassinated in New Delhi.

His assassination shocked India and had a profound impact on the country during its first year of independence.

Gandhi's death became one of the defining events of the early Republic period and remains an important event in modern Indian history.
""",
    },

    {
        "title": "11. The Constituent Assembly of India",
        "date": date(1946, 12, 9),
        "description": """
The Constituent Assembly was responsible for preparing the Constitution of India.

The Assembly first met on 9 December 1946, before independence.

After independence, it continued its work as the body responsible for framing the Constitution of the new country.

Members debated the structure of government, fundamental rights, citizenship, relations between the Union and the states, the judiciary, elections and other major constitutional questions.

The Constitution-making process involved numerous committees and extensive debates.

The National Archives preserves the Constituent Assembly Debates covering the period 1947–1950.

These debates provide important primary-source material for understanding the discussions that shaped the Constitution.
""",
    },

    {
        "title": "12. Objectives Resolution",
        "date": date(1946, 12, 13),
        "description": """
On 13 December 1946, Jawaharlal Nehru moved the Objectives Resolution in the Constituent Assembly.

The Resolution outlined broad principles for the future constitutional structure of India.

It emphasised ideas relating to sovereignty, democracy, justice, equality and freedom.

The Resolution was adopted by the Constituent Assembly on 22 January 1947.

Its principles influenced the development of the Constitution and later the Preamble.

The Objectives Resolution is therefore an important step in understanding the intellectual and political foundations of the Indian Constitution.
""",
    },

    {
        "title": "13. Drafting Committee of the Constitution",
        "date": date(1947, 8, 29),
        "description": """
The Drafting Committee of the Constituent Assembly was established on 29 August 1947.

Dr. B. R. Ambedkar served as its Chairman.

The committee played a major role in preparing and refining the draft constitutional text.

However, the Constitution was not the work of the Drafting Committee alone. The Constituent Assembly debated provisions, proposed amendments and ultimately adopted the Constitution.

Various committees of the Constituent Assembly contributed to different aspects of the constitutional framework.

The Drafting Committee therefore formed an important part of a much larger Constitution-making process.
""",
    },

    {
        "title": "14. Making of the Constitution",
        "date": date(1947, 8, 29),
        "description": """
The Constitution of India was developed through extensive discussion in the Constituent Assembly.

Members considered fundamental questions concerning the nature of the Indian state and its system of government.

Important subjects included fundamental rights, citizenship, parliamentary government, federal relations, the judiciary, elections, emergency provisions and safeguards for different groups.

The Assembly considered reports from various committees and debated draft provisions.

The drafting process involved several stages of discussion, amendment and revision.

The Constitution therefore emerged from a lengthy deliberative process rather than being written as a single document at one time.

The National Archives preserves the Constituent Assembly Debates from 1947 to 1950 as an important historical source.
""",
    },

    {
        "title": "15. Adoption of the National Flag",
        "date": date(1947, 7, 22),
        "description": """
The Constituent Assembly adopted the present design of India's national flag on 22 July 1947, shortly before independence.

The flag consists of three horizontal bands of saffron, white and green.

At the centre of the white band is the navy-blue Ashoka Chakra with 24 spokes.

The flag became an important national symbol during the transition from colonial rule to independence.

It was used as the national flag of independent India from 15 August 1947 and continued as the flag of the Republic after the Constitution came into force.

The Government of India's National Portal records 22 July 1947 as the date on which the Constituent Assembly adopted the design.
""",
    },

    {
        "title": "16. Constitution Adopted — 26 November 1949",
        "date": date(1949, 11, 26),
        "description": """
After several years of constitutional discussions, debates and amendments, the Constituent Assembly adopted the Constitution of India on 26 November 1949.

The official Constitution states that the Constituent Assembly adopted, enacted and gave the Constitution to the people of India on 26 November 1949.

Not every provision came into force on that date.

Article 394 specifies that the remaining provisions of the Constitution would come into force on 26 January 1950.

26 November is now observed as Constitution Day in India.

The adoption of the Constitution marked the completion of the principal Constitution-making process and prepared the country for the establishment of the Republic.
""",
    },

    {
        "title": "17. Constitution Signed — 24 January 1950",
        "date": date(1950, 1, 24),
        "description": """
On 24 January 1950, members of the Constituent Assembly signed the Constitution of India.

The signing took place two days before the Constitution came into force.

The event represented the final stage of the constitutional transition.

The Constituent Assembly had spent years discussing and refining the constitutional framework.

With the Constitution signed, India was ready to enter the next stage of its political development as a Republic.

The Constitution came into force on 26 January 1950.
""",
    },

    {
        "title": "18. 26 January 1950 — India Becomes a Republic",
        "date": date(1950, 1, 26),
        "description": """
On 26 January 1950, the Constitution of India came into force.

India became a Republic.

The constitutional system established by the Constitution replaced the earlier Dominion framework.

The office of the President became the constitutional head of the Union.

Dr. Rajendra Prasad became the first President of India.

26 January was selected as the commencement date because 26 January had already been associated with the national movement's declaration of Purna Swaraj in 1930.

The Constitution therefore transformed India from a Dominion into a sovereign constitutional Republic.
""",
    },

    {
        "title": "19. Dr. Rajendra Prasad — First President of India",
        "date": date(1950, 1, 26),
        "description": """
Dr. Rajendra Prasad became the first President of the Republic of India on 26 January 1950.

Before becoming President, he had played an important role in India's national movement and in the Constitution-making process.

He served as President of the Constituent Assembly during the framing of the Constitution.

With the Constitution coming into force, he became the first constitutional President of independent India's Republic.

His tenure began during a period when the institutions of the new Republic were being established and adapted to the constitutional system.
""",
    },

    {
        "title": "20. India at the Beginning of the Republic",
        "date": date(1950, 1, 26),
        "description": """
When India became a Republic in January 1950, the country was still dealing with the consequences of Partition and the challenges of nation-building.

The government faced economic difficulties, refugee rehabilitation, administrative reorganisation and the need to establish democratic institutions.

At the same time, the Constitution created a framework for representative government, fundamental rights, an independent judiciary and relations between the Union and the states.

The beginning of the Republic therefore represented both a constitutional achievement and the start of a long process of institution building.

The years immediately following 1950 would see India's first general election, economic planning, reorganisation of states and further development of democratic institutions.
""",
    },

    {
        "title": "21. Important Timeline — 1947 to 1950",
        "date": date(1950, 1, 26),
        "description": """
IMPORTANT TIMELINE

22 July 1947
The Constituent Assembly adopted the design of India's national flag.

15 August 1947
India became independent.

29 August 1947
The Drafting Committee of the Constituent Assembly was established.

1947
Partition created India and Pakistan and led to large-scale population displacement.

1947–48
The first India-Pakistan war took place in connection with Jammu and Kashmir.

30 January 1948
Mahatma Gandhi was assassinated in New Delhi.

1948
Hyderabad was integrated into the Indian Union following Operation Polo.

26 November 1949
The Constituent Assembly adopted the Constitution of India.

24 January 1950
Members of the Constituent Assembly signed the Constitution.

26 January 1950
The Constitution came into force and India became a Republic.

Dr. Rajendra Prasad became the first President of India.
""",
    },

    {
        "title": "22. Exam Revision Points — 1947 to 1950",
        "date": date(1950, 1, 26),
        "description": """
IMPORTANT EXAM POINTS

1. India became independent on 15 August 1947.

2. The Indian Independence Act was passed in 1947.

3. Jawaharlal Nehru became the first Prime Minister of independent India.

4. The national flag was adopted by the Constituent Assembly on 22 July 1947.

5. The Drafting Committee was established on 29 August 1947.

6. Dr. B. R. Ambedkar was Chairman of the Drafting Committee.

7. Mahatma Gandhi was assassinated on 30 January 1948.

8. Sardar Vallabhbhai Patel played a major role in the integration of princely states.

9. Hyderabad was integrated into the Indian Union in 1948 following Operation Polo.

10. Jawaharlal Nehru moved the Objectives Resolution on 13 December 1946.

11. The Constitution was adopted on 26 November 1949.

12. The Constitution was signed on 24 January 1950.

13. The Constitution came into force on 26 January 1950.

14. India became a Republic on 26 January 1950.

15. Dr. Rajendra Prasad became the first President of India.

16. The Constitution-making process involved the Constituent Assembly, its committees and extensive debates.

17. The National Archives preserves the Constituent Assembly Debates for the period 1947–1950.
""",
    },
]


# ---------------------------------------------------------
# Import into database
# ---------------------------------------------------------

created = 0
updated = 0

for item in history_data:

    obj, was_created = CurrentAffair.objects.update_or_create(
        title=item["title"],
        defaults={
            "job": None,
            "period": "1947-1950",
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
print("1947–1950 HISTORY IMPORT COMPLETED")
print("=" * 60)
print(f"New records created : {created}")
print(f"Existing records updated : {updated}")
print(f"Total records processed : {len(history_data)}")
print("=" * 60)