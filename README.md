# Medical-Chatbot-using-LangChain-LLM-Pinecone-Flask-AWS

Ques: Why Docker Image created ?

Ans: If someone wants to clone this project and run it locally, instead of downloading all these heavy-lifting dependencies, it can easily call the Docker image where the dependencies are already installed, and it can just call that docker image -> using this cmd -> docker run -p 8080:8080 medical-chatbot

## To build the dockerfile. ( it will take several seconds for the first time to run on vs code terminal)
docker build -t medical-chatbot .

## To run the application in localhost (ui page) run through Docker image 

docker run -p 8080:8080 medical-chatbot
then go to google and write in url -> localhost:8080



Note: We are deploying our project on Render (free)

Ques : Why we use clould platforms to deploy our project ?

Ans : Because these platforms give us a URL and if we give this URL to someone, they can access our medical chatbot application ( no code is needed to give)
And if suppose we dont want to use that application , we can stop the services , so we have noticed it gives sometime "Page not found"