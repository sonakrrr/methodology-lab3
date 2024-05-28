FROM node:22-alpine

WORKDIR /app

COPY . .

RUN npm install

EXPOSE 4455

CMD [ "node", "index.js" ]