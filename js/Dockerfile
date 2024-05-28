FROM node:slim

WORKDIR /app

COPY . .

RUN npm install

EXPOSE 4455

CMD [ "node", "index.js" ]