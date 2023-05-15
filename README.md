# whisper-speech-to-text

使用 OpenAI Whisper Model 進行批次語音辨識，預設語言是繁體中文。

## How to use? 使用說明

1. 下載 Repository
2. (可選擇) 建立 venv: `python3 -m venv venv` 或 `python -m venv venv`
3. 安裝相關 Python 套件: `pip3 install -r requirements.txt` 或 `pip install -r requirements.txt`
4. 將 `.env.example` 檔案重新命名為 `.env`，並貼上 OpenAI Secret Key
5. 把要轉換的檔案放到 **input** 資料夾中
6. 執行 `python3 main.py`
7. 執行結果會放在 **output** 資料夾中
