# Blog API

Welcome to the blog API. You can post, comment and moderate comments using AI.

## Content

- [Tech Details](#tech-details)
- [How to run the project](#how-to-run-the-project)

---

### Tech Details

| Resource                      | Resource Name | Version   | Comment   |
|-------------------------------|---------------|-----------|-----------|
| Back-end programming language | Python        | 3.13      |           |
| Back-end web framework        | FastAPI       | 0.116.1   |           |
| Database                      | PostgreSQL    | 17.6      |           |
| Web server                    | Uvicorn       | 0.35.0    |           |


### How to run the project

I'm using `docker-compose.yml` to build and run the project. Use next commands:

1. To build and run the project in the terminal window:

```bash
docker-compose up --build
```

2. To stop the project use `Ctrl + V`. To down containers (without deleting volumes):

```bash
docker-compose down
```

* To remove volumes use `docker-compose down -v`.

---