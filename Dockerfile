FROM ubuntu:latest
LABEL authors="granth"

ENTRYPOINT ["top", "-b"]