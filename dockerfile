# 基本となるPythonイメージを使用
FROM python:3.9-slim

# 作業ディレクトリを作成
WORKDIR /app

# 必要な依存関係をコピー
COPY requirements.txt requirements.txt

# 必要なPythonパッケージをインストール
RUN pip install -r requirements.txt

# アプリケーションファイルをコピー
COPY . .

# Streamlitを起動
CMD ["streamlit", "run", "app.py", "--server.port", "8501", "--server.enableCORS", "false"]
