from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional

load_dotenv()

model = ChatOpenAI(model="gpt-4-turbo")

# schema


class Review(TypedDict):
    key_themes: Annotated[list[str],
                          "Write all the key themes discussed in the review in a list"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str,
                         "Return sentiment of the review either negative, positive or neutral"]
    pros: Annotated[Optional[list[str]],
                    "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]],
                    "Write down all the cons inside a list"]
    name: Annotated[Optional[str], "Write the name of the reviewer"]


structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""⭐️⭐️⭐️⭐️☆ 4.5/5 — Solid Flagship with Subtle Upgrades

I’ve been using the Samsung Galaxy S24 for about 3 weeks now, and it’s easily one of the most refined Android phones of 2024. While it doesn’t reinvent the wheel, it perfects a lot of what already worked well.

✅ Pros:
Stunning Display: The 6.2" Dynamic AMOLED 2X screen is super crisp, bright, and smooth at 120Hz.

Snappy Performance: The Snapdragon 8 Gen 3 delivers fast multitasking, gaming, and AI features with zero lag.

AI Features: Galaxy AI (like Live Translate and Note Assist) actually feel useful, not gimmicky.

Premium Build: Flat design with Gorilla Glass Armor and aluminum frame feels sleek and sturdy.

Software Support: 7 years of OS + security updates — finally a real longevity promise for Android users.

❌ Cons:
Battery Life is Just Okay: It’ll get you through a day, but heavy users will want to charge before evening.

Minimal Upgrades: If you're coming from an S23, it's not a big leap—feels more like a refinement than a revolution.

No Charger in Box: Still annoying that Samsung doesn’t include a charger with a ₹75K phone.

Overall, the Galaxy S24 is a fantastic flagship that checks all the right boxes. It’s not groundbreaking, but it’s a solid choice for anyone looking for a premium Android experience in 2024. Highly recommend!
review by Chitraksh""")

# print(type(result))
# print(result)
# print(result['summary'])
# print(result['sentiment'])
print(result['name'])
