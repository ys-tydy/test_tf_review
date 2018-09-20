FROM golang:latest

WORKDIR /go/src/app
RUN go get -u github.com/golang/dep/cmd/dep

ADD . .
RUN dep ensure

CMD ["go", "run", "main.go"]


# docker build ./ -t test_tf_review
# docker run test_tf_review
# docker run -v `pwd`/main.go:/go/src/app/main.go test_tf_review
# docker run -i -t test_tf_review /bin/bash
