FROM golang:1.20

# Set destination for COPY
WORKDIR /app

# pre-copy/cache go.mod for pre-downloading dependencies and only redownloading them in subsequent builds if they change
COPY go.mod ./
RUN go mod download && go mod verify


# Copy the source code. Note the slash at the end, as explained in
# https://docs.docker.com/engine/reference/builder/#copy
COPY *.go ./

# Copy input files
COPY input.txt /

# Build
RUN go build -o /day02

# Run
CMD ["/day02", "/input.txt"]