# Import pandas for creating the DataFrame
import pandas as pd

rollNo = input("Enter your college roll number: ").strip()

last2_digits = rollNo[-2:]

#string to integer
digit1 = int(last2_digits[0])
digit2 = int(last2_digits[1])
categories = ["billing", "account", "general"]

c1 = categories[digit1 % 3]
c2 = categories[digit2 % 3]

faq_data = [
    {
        "category": "billing",
        "question": "How can I check my billing history?",
        "answer": "You can check your billing history by logging into your account and opening the Billing section.",
        "keywords": ["billing", "payment", "history"]
    },
    {
        "category": "account",
        "question": "How do I reset my account password?",
        "answer": "Click on the Forgot Password option on the login page and follow the instructions sent to your registered email address.",
        "keywords": ["password", "reset", "login"]
    },
    {
        "category": "general",
        "question": "How can I contact customer support?",
        "answer": "You can contact customer support through the Help or Contact Us section of the website.",
        "keywords": ["support", "help", "contact"]
    },
    {
        "category": "general",
        "question": "What should I do if I cannot log in?",
        "answer": "Check your username and password first. If the problem continues, use the password reset option or contact customer support.",
        "keywords": ["login", "access", "support"]
    }
]

# Different questions are created depending on the category.
if c1 == "billing":
    faq1 = {
        "category": c1,
        "question": "How can I update my billing information?",
        "answer": "Open the Billing section of your account and update your payment or billing details before saving the changes.",
        "keywords": ["billing", "payment", "details"]
    }

elif c1 == "account":
    faq1 = {
        "category": c1,
        "question": "How do I update my registered mobile number?",
        "answer": "Go to your account settings, select contact information, enter your new mobile number, and verify it using the confirmation code.",
        "keywords": ["mobile", "account", "verification"]
    }

else:
    faq1 = {
        "category": c1,
        "question": "How can I change my notification preferences?",
        "answer": "Open the notification settings in your account and select the types of notifications you want to receive.",
        "keywords": ["notifications", "settings", "preferences"]
    }

if c2 == "billing":
    faq2 = {
        "category": c2,
        "question": "How can I download my payment receipt?",
        "answer": "Go to the Billing section, select the relevant transaction, and choose the option to download the payment receipt.",
        "keywords": ["receipt", "payment", "billing"]
    }

elif c2 == "account":
    faq2 = {
        "category": c2,
        "question": "How can I change my registered email address?",
        "answer": "Open your account settings, edit the registered email address, and complete the verification process.",
        "keywords": ["email", "account", "verification"]
    }

else:
    faq2 = {
        "category": c2,
        "question": "Where can I find information about available services?",
        "answer": "You can find information about available services in the Help or Services section of the website.",
        "keywords": ["services", "information", "help"]
    }

faq_data.append(faq1)
faq_data.append(faq2)

df = pd.DataFrame(faq_data)

print("\nPersonalized Knowledge Base:")
print(df)

print("\nRoll Number:", rollNo)
print("Last two digits:", digit1, digit2)
print("Digit", digit1, "-> Category:", c1)
print("Digit", digit2, "-> Category:", c2)

print("\nNumber of FAQ entries:", len(df))


import pandas as pd

def score(q, df):
    qw = set(q.lower().split())
    r = []

    for i, x in df.iterrows():
        w = set(str(x["question"]).lower().split()) | {
            k.strip().lower() for k in str(x["keywords"]).split(",")
        }
        s = len(qw & w)
        if s:
            r.append((i, s))

    r.sort(key=lambda x: x[1], reverse=True)
    return pd.DataFrame(
        [df.loc[i].assign(confidence=s) for i, s in r]
    )

q = input("Query: ")
print(score(q, df))

def same_category(c, df):
    return df[df["category"].str.lower() == c.lower()]

c = df.iloc[0]["category"]
print(same_category(c, df))

i = 0
print(df.loc[i])
k = input("New keyword: ").strip()

if k:
    old = str(df.loc[i, "keywords"])
    df.loc[i, "keywords"] = k if old == "nan" else old + ", " + k

rn = "YOUR_ROLL_NUMBER"
df.to_csv(rn + "_faq_data.csv", index=False)

print(df.groupby("category").size())

def score2(q, df):
    r = []

    for i, x in df.iterrows():
        w = set(str(x["question"]).lower().split()) | {
            k.strip().lower() for k in str(x["keywords"]).split(",")
        }
        s = len(set(q.lower().split()) & w)
        if s:
            r.append((i, s))

    if not r:
        print("No match")
        return

    m = max(s for i, s in r)
    b = [i for i, s in r if s == m]

    print(df.loc[b].assign(confidence=m))

score2("fee", df)
score2("payment method", df)