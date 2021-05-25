## Spaceflight News Retrieval

### Overview
The goal of this project is to retrieve the latest space flight news from the
[Spaceflight News API](www.spaceflightnewsapi.net) and write it to a 
PostgreSQL database.

### Getting started

To get the environment running on your system, go through the following steps:

1. Clone the repository into the working directory and move into the project 
   directory:
   ```
   git clone https://github.com/bastiaanhoeben/spaceflight-news
   ```
   ```
   cd spaceflight-news
   ```
   
2. Start up the database service and service dependencies:
   ```
   docker-compose up
   ```

3. Create a virtual environment and activate it:
   ```
   python -m venv spaceflight-news
   ```
   ```
   source spaceflight-news/bin/activate
   ```
4. Install the necessary packages from requirements.txt:
   ```
   python -m pip install -r requirements.txt
   ```

5. Run the python script and follow the instructions prompted for:
   ```
   python main.py
   ```
