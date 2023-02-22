from src.{{cookiecutter.app_slug}} import create_app

app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
