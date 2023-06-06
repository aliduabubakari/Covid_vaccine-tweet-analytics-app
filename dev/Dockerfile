# Base Image
FROM python:3.9

# Working Directory
WORKDIR /app

# Copying Dependencies
COPY requirements.txt .

# Installing Requirements
RUN pip install -r requirements.txt

# Copying the Application
COPY . .

# Expose Port
EXPOSE 8501

# Running the Application
CMD ["streamlit", "run", "NLPapp8_best.py"]
