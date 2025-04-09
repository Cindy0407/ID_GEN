FROM python:3.8-slim

# 裝一些基本工具（可選）
RUN apt-get update && apt-get install -y \
    curl vim git && \
    rm -rf /var/lib/apt/lists/*

# 設定主目錄名稱
WORKDIR /code

# 複製 requirements 並安裝
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 把 app 資料夾掛進來
COPY . .

# 預設啟動 FastAPI（開發用會被 docker-compose 覆蓋）
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
