FROM node:13-alpine

ENV MONGO_DB_USERNAME=admin \
    MONGO_DB_PWD=admin

RUN mkdir -p /home/node-app

COPY . /home/node-app

WORKDIR /home/node-app

CMD ["node", "./app/server.js"]