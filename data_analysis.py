import matplotlib.pyplot as plt
import pandas as pd

def count_words(data):
    """ Count the total number of times each word is used in the dataset for each user. """

    user_word_counts = {}
    
    for entry in data:
        sender = entry["sender"]
        message = entry["message"]

        if sender not in user_word_counts:
            user_word_counts[sender] = {}
        
        words = message.lower().split()

        for word in words:
            user_word_counts[sender][word] = user_word_counts[sender].get(word, 0) + 1

    for sender in user_word_counts:
        user_word_counts[sender] = dict(
            sorted(
                user_word_counts[sender].items(),
                key = lambda item:item[1],
                reverse = True
            )
        )

    return user_word_counts

def messages_over_time(data):
    """ Maps messages sent over time by each user """

    df = pd.DataFrame(data)
    df["timestamp"] = pd.to_datetime(df["timestamp"], utc = True, format="ISO8601")

    counts = (
        df
        .set_index("timestamp")
        .groupby("sender")
        .resample("M")
        .size()
    )

    counts = counts.reset_index()
    counts["month"] = counts["timestamp"].dt.strftime("%Y-%m")
    # continue here
    
    counts.plot(kind = "bar")
    plt.xlabel("Time")
    plt.ylabel("Messages Sent")
    plt.title("Messages Over Time by Sender")
    plt.tight_layout()
    plt.show()
    return 