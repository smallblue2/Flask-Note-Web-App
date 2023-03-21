# import create_app function
from website import create_app

# Create the app
app = create_app()

# Run in debug mode
if __name__ == '__main__':
    app.run(debug=True)
