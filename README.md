### Required Links:

Video Presentation:
https://drive.google.com/file/d/1r5XI5qSN7xeYL9xbLvqgcviHp5yvuosZ/view?usp=sharing

UI Repository: 
https://github.com/SaiAshish9/YouTube_Asgmt_UI

Postman Documentation: https://documenter.getpostman.com/view/7520343/2sA2xjyqXe

Solution Document: 
https://drive.google.com/file/d/1JuYbYvOfDN1g_P24UMP3DLRzRkAsXoFv/view?usp=sharing

Assignment Link:
https://fampay.notion.site/Backend-Assignment-FamPay-32aa100dbd8a4479878f174ad8f9d990

### Installation Steps:

Run the following commands inside project's root directory:

1. Using Docker

- python3 -m venv youtube_api
- source youtube_api/bin/activate 
- docker-compose up -d inside root directory
- Go to site: http://localhost:8000/api/u/youtube/videos?limit=10&offset=11

2. Without Using Docker
- python3 -m venv youtube_api
- source youtube_api/bin/activate 
- python -m pip install -r requirements.txt
- Add .env and specify properties YOUTUBE_API_KEY and YOUTUBE_API_KEY_2
- Open 3 other terminal tabs and activate above mentioned virtualenv
- redis-server
- python3 manage.py runserver
- celery -A youtube_backend worker -l info
- celery -A youtube_backend beat -l info
- Start UI server using README specified at the following link:
https://github.com/SaiAshish9/YouTube_Asgmt_UI/edit/master/README.md
- Go to http://localhost:3000/ to see how data is getting changed after every 10s
 
### App Screenshot:

<img width="1440" alt="Youtube Assignment" src="https://github.com/SaiAshish9/YouTube_Asgmt_UI/assets/43849911/698b68bc-768b-40ce-9a4c-dffcb141132f">

### App Functionlity Sample:

https://github.com/SaiAshish9/YouTube_Asgmt_UI/assets/43849911/e29d5c7f-16f9-46bf-be73-4ba6c87c3bf4

### Solutioning:

1. Server should call the YouTube API continuously in background (async) with some interval (say 10 seconds) for fetching the latest videos for a predefined search query and should store the data of videos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs and any other fields you require) in a database with proper indexes.

Note: Used Celery worker, beat and redis server to run required asynchronous tasks in background after every 10s

<img width="836" alt="Screenshot 2024-03-13 at 11 19 04 AM" src="https://github.com/SaiAshish9/YouTube_Asgmt_API/assets/43849911/59e4a640-7427-41a0-beda-ab2001110330">


2. A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.

<img width="829" alt="Screenshot 2024-03-13 at 11 19 49 AM" src="https://github.com/SaiAshish9/YouTube_Asgmt_API/assets/43849911/95513924-0636-4686-9e27-0db2f14f016e">


Note: Refer to the postman documentation


3. A basic search API to search the stored videos using their title and description.

<img width="835" alt="Screenshot 2024-03-13 at 11 20 59 AM" src="https://github.com/SaiAshish9/YouTube_Asgmt_API/assets/43849911/6db7d2d7-3a8a-44fa-b7f2-459b68579eac">


Note: Refer to the postman documentation


4. Dockerize the project.

<img width="830" alt="Screenshot 2024-03-13 at 11 21 31 AM" src="https://github.com/SaiAshish9/YouTube_Asgmt_API/assets/43849911/0d268c60-a2c7-48e2-b389-6ccfb619e3ec">


Note: Follow the above mentioned installation steps using docker


5. It should be scalable and optimised.

- Utilizing standard Django utilities and React components ensures that our application container is scalable and can be optimized using various cloud services. 
- We can enhance extensibility in the React code by implementing various design patterns.
- Integrating ElasticSearch can significantly improve search optimization. 
- Optimizing Celery configuration can prevent burnouts and enhance performance. 
- Additionally, integrating Kubernetes can effectively manage Docker containers for smoother operations.


6. Add support for supplying multiple API keys so that if quota is exhausted on one, it automatically uses the next available key.

<img width="829" alt="Screenshot 2024-03-13 at 11 23 20 AM" src="https://github.com/SaiAshish9/YouTube_Asgmt_API/assets/43849911/d5db776a-fe38-422c-a7d6-af7626faa038">


7. Make a dashboard to view the stored videos with filters and sorting options (optional)

<img width="1440" alt="Youtube Assignment" src="https://github.com/SaiAshish9/YouTube_Asgmt_API/assets/43849911/58f1d3ca-24a6-44a1-a5dc-d4605adc7157">


Note: For now, I've implemented LimitOffsetPagination and search functionality. Next, I plan to integrate the filters modal, enabling specific actions similar to those on youtube.com


8. Optimise search api, so that it's able to search videos containing partial match for the search query in either video title or description.
Ex 1: A video with title How to make tea? should match for the search query tea how

<img width="828" alt="Screenshot 2024-03-13 at 11 24 33 AM" src="https://github.com/SaiAshish9/YouTube_Asgmt_API/assets/43849911/8bbfb8dd-3a6d-46e0-a9d6-77d4486b9a1d">


Note: For now, I've optimized it using Django REST Framework search filters. In the future, we can explore ElasticSearch as a potentially more effective alternative
