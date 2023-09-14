# Lekhan - A Django Blogging Application

Lekhan is a versatile Django-based blogging application that enables users to create, manage, and share their blog posts, comment on others' posts, like and unlike posts, edit their profiles, and more. It provides a robust platform for bloggers to interact and engage with their audience. This README.md file provides detailed instructions on setting up and using the Lekhan application.

## Features

- User authentication (registration, login, logout).
- Blog post creation, editing, and deletion.
- Commenting on blog posts.
- Liking and unliking blog posts.
- User profile creation and editing.
- Categorization of blog posts.
- Authorization control for blog post editing and deletion.

## Installation

To run Lekhan locally, you need to have Python, pip, and Django installed on your system. Follow these steps to get started:

1. Clone the repository:

   ```bash
   git clone https://github.com/auscode/Blogging.git
   ```

2. Change your working directory to the project folder:

   ```bash
   cd Blogging
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - **On Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **On macOS and Linux:**

     ```bash
     source venv/bin/activate
     ```

5. Install the project dependencies from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

6. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

7. Create a superuser (admin) account:

   ```bash
   python manage.py createsuperuser
   ```

8. Start the development server:

   ```bash
   python manage.py runserver
   ```

9. Access the Lekhan application in your browser at `http://localhost:8000/`.

## Usage

1. Log in with your superuser account to access the admin panel at `http://localhost:8000/admin/`. Here, you can manage users, blog posts, categories, and other site settings.

2. To create a new blog post, navigate to the homepage and click on the "Create Post" button.

3. Users can register and log in to start interacting with the application, including creating their own profile, commenting on blog posts, liking/unliking posts, and more.


## Contributing

If you would like to contribute to Lekhan, please follow these steps:

1. Fork the repository on GitHub.

2. Clone your forked repository to your local machine.

3. Create a new branch for your feature or bug fix.

4. Make your changes and test thoroughly.

5. Commit your changes and push them to your GitHub repository.

6. Create a pull request to the original repository.

## Contact

If you have any questions or need further assistance, feel free to reach out to the project maintainers:

- Email: [harshittext+lehan@gmail.com](mailto:harshittext+lehkan@gmail.com)

We hope you find Lekhan useful for your blogging needs! Happy blogging!
