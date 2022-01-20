FROM ubuntu:20.04
RUN apt-get update
RUN apt-get install nginx -y
RUN rm /etc/nginx/conf.d/default.conf -f
RUN rm /etc/nginx/nginx.conf -f
ADD ./nginx.conf /etc/nginx/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]


