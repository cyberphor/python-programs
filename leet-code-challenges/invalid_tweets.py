from pandas import DataFrame

def create_dataset() -> DataFrame:
    columns = ["tweet_id", "content"]
    rows = [
        [1, "Vote for Biden"],
        [2, "Let us make America great again!"]
    ]
    dataframe = DataFrame(columns = columns, data = rows)
    return dataframe

def solution(dataset: DataFrame) -> DataFrame:
    # apply the "len" function against the "content" column
    # return data where the length is longer than 15 characters
    # locate data with the dataset where this is true
    # return the header and value of this data
    return dataset.loc[dataset["content"].apply(len) > 15][["tweet_id"]]

if __name__ == "__main__":
    dataset = create_dataset()
    answer = solution(dataset)
    print(answer)