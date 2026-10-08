FROM python:3.14-alpine
WORKDIR /app
COPY app.py review.html /app/
RUN mkdir /data && chown -R 10001:10001 /app /data
USER 10001:10001
EXPOSE 8080
CMD ["python","app.py"]
