To run docker container 

```bash
sudo docker compose up --build 
```

To stop and remove docker container
```bash
sudo docker compose down 
```

To delete volume too (i.e, persistent data is deleted). So, its dangerous
```bash
sudo docker compose down -v
```