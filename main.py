from ckiptagger import WS, data_utils
import csv
# !pip install numpy


# 下載 CkipTagger 的預訓練模型，下載的路徑為"./"，並且生出data資料夾
data_utils.download_data_gdown("./")

# 載入NTUSD情感字典
def load_ntusd_dict(file_path):
    ntusd_dict = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            word, sentiment = row
            ntusd_dict[word] = sentiment
    return ntusd_dict

# 情感分析
def sentiment_analysis(text, ntusd_dict):
    ws = WS("./data")
    tokens = ws([text])[0]
    print (tokens)
    sentiment_score = 0
    for token in tokens:
        if token in ntusd_dict:
            sentiment = ntusd_dict[token]
            if sentiment == 'positive':
                sentiment_score += 1
            elif sentiment == 'negative':
                sentiment_score -= 1
    return sentiment_score

# 主程式
if __name__ == "__main__":
    # 載入NTUSD情感字典
    ntusd_dict = load_ntusd_dict('./ntusd_full.csv')

    # 待分析的文本
    text = "幹你媽的，去死"
    # 進行情感分析
    score = sentiment_analysis(text, ntusd_dict)
    print(score)

    if score > 0:
        print("正面情緒")
    elif score < 0:
        print("負面情緒")
    else:
        print("中性情緒")

