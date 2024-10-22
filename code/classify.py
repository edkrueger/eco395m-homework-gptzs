import pandas as pd
from openai import OpenAI
from prompt_classifier import classify_text_message
from sklearn.metrics import classification_report
from tqdm import tqdm

# this is so we can use progress_apply
tqdm.pandas(desc="progress")


def load_data(path):
    """Loads a CSV, expecting columns "label" and "text".
    Returns a pd.DataFrame with series named "label" and "text".
    """
    # write this


def classify_all(df, client):
    """Takes a DataFrame with series named "label" and "text".
    Returns a pd.DataFrame with series named "label" and "text"
    and also "predicted_label" which is our zero-shot classifier's prediction.
    """

    # in order to be able to use a progress bar with pd.DataFrame
    # tqdm can modify pd.DataFrame's methods to include `progress_apply`
    # which works like apply, but adds a progress bar
    # write this


if __name__ == "__main__":
    import os
    import sys

    import dotenv

    dotenv.load_dotenv()

    OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
    client = OpenAI(api_key=OPENAI_API_KEY, max_retries=0)


    IN_PATH = sys.argv[1]
    OUT_PATH = sys.argv[2]

    out_dir = os.path.dirname(OUT_PATH)
    os.makedirs(out_dir, exist_ok=True)

    in_df = load_data(IN_PATH)

    out_df = classify_all(in_df, client=client)

    out_df.to_csv(OUT_PATH, index=False)

    print(
        classification_report(y_true=out_df["label"], y_pred=out_df["predicted_label"])
    )
