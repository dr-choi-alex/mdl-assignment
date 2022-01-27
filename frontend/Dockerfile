# FROM node:latest as node

# COPY . .

# RUN npm install

# RUN npm install -g @angular/cli@7.0.2

# RUN ng build

# # RUN npm run build

# RUN npm install http-server -g

# RUN Http-server dist/.

# Stage 0, based on Node.js, to build and compile Angular
# FROM node:12 as node
# # See https://crbug.com/795759
# WORKDIR /app
# COPY package.json .
# RUN npm install
# COPY . .
# # Run unit tests to ensure that the image being built is valid
# # Run end to end tests to ensure that the image being built is valid
# #RUN npm run e2e
# # Build the angular application with production configuration by default
# RUN npm run build 
# # Stage 1, based on Nginx, to have only the compiled app, ready for production with Nginx
# RUN npm install http-server -g
# RUN http-server app/dist/.

# ### STAGE 1: Build ###
# FROM node:12.7-alpine AS build
# WORKDIR /app
# COPY package.json package-lock.json ./
# RUN npm install
# COPY . .
# RUN npm run build
# ### STAGE 2: Run ###
# FROM nginx:alpine
# COPY --from=node /app/dist/mdl /usr/share/ngnix/html

# BUILD
FROM node:12.7-alpine AS build
WORKDIR /app

COPY package.json .
RUN npm install

COPY . .
RUN npm run build

# RUN
FROM nginx:1.17.1-alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY /nginx.conf  /etc/nginx/conf.d/default.conf

EXPOSE 80

