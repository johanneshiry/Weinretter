FROM node:latest as build-stage
# config build arg may be dev or prod
ARG config=dev

WORKDIR /app
COPY package*.json /app/
RUN npm install
COPY ./ /app/

RUN npm run generate --fail-on-error

FROM nginx:alpine
COPY --from=build-stage /app/dist/ /usr/share/nginx/html
COPY --from=build-stage /app/nginx.conf /etc/nginx/nginx.conf
