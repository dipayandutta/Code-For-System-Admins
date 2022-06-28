FROM node:14

WORKDIR /app 

COPY package.json .

RUN npm install 

COPY . . 

EXPOSE 80 

# VOLUME [ "/app/node_modules" ] Annoynmous Volume

# CMD [ "node", "server.js" ]

CMD ["npm", "start"]


#docker run -d -p 3900:80 --rm --name bindmount_example -v feedback:/app/feedback -v "/home/dipayan_linux/Work/docker/volumeExample:/app" -v /app/node_modules feedbacknode/volume:v1