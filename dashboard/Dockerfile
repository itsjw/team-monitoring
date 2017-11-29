FROM node:8

ENV APP_HOME /dashboard/

WORKDIR $APP_HOME
COPY package.json $APP_HOME
COPY package-lock.json $APP_HOME
RUN npm i
COPY . $APP_HOME

EXPOSE 3000

CMD npm run dev
