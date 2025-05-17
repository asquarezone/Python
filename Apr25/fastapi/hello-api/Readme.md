## Commands 


### Building the image

```bash
docker image build -t fastapi:1 .
```

### Running the container

```bash
docker run -d -P --name app fastapi:1
```