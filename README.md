# Blog Beat Backend

---

## Links

<p>
  <a href="https://blog-beat-17c62545ca2a.herokuapp.com" style="text-decoration: none;">
    <img src="https://img.icons8.com/ios-filled/15/ffffff/web.png" alt="Frontend App"> Frontend App
  </a>
</p>
<p>
  <a href="https://github.com/j0hanz/blog-beat-web" style="text-decoration: none;">
    <img src="https://img.icons8.com/ios-filled/15/ffffff/github.png" alt="Frontend Repository"> Frontend Repository
  </a>
</p>
<p>
  <a href="https://blog-beat-api-bab609deb9ee.herokuapp.com" style="text-decoration: none;">
    <img src="https://img.icons8.com/ios-filled/15/ffffff/api.png" alt="API"> API
  </a>
</p>
<p>
  <a href="https://github.com/j0hanz/blog_beat_api" style="text-decoration: none;">
    <img src="https://img.icons8.com/ios-filled/15/ffffff/github.png" alt="API Repository"> API Repository
  </a>
</p>


### Database Structure

This document provides a detailed overview of Blog Beat's database schema, including the tables, their attributes, and the relationships between them. The database stores information about users, profiles, posts, comments, likes, favorites, and followers.

![erd](https://github.com/j0hanz/blog_beat_api/assets/159924955/6b11144b-f52f-4ab2-99df-9b07f1758f1a)

---

**Entities**

* **User:** Stores user account information.
    * Attributes:
        * id (BigAuto): Primary Key.
        * username (CharField).
        * password (CharField).

* **Profile:** Contains detailed user profile information.
    * Attributes:
        * id (BigAuto): Primary Key.
        * owner (OneToOneField): Foreign Key referencing User.id (one-to-one relationship).
        * first_name (CharField).
        * last_name (CharField).
        * country (CountryField).
        * bio (TextField).
        * image (ImageField).
        * created_at (DateTimeField).
        * updated_at (DateTimeField).

* **Post:** Stores user-generated content.
    * Attributes:
        * id (BigAuto): Primary Key.
        * owner (ForeignKey): Foreign Key referencing User.id (user who created the post).
        * title (CharField).
        * content (TextField).
        * image (ImageField).
        * image_filter (CharField).
        * location (CharField).
        * created_at (DateTimeField).
        * updated_at (DateTimeField).

* **Like:** Records user likes on posts.
    * Attributes:
        * id (BigAuto): Primary Key.
        * owner (ForeignKey): Foreign Key referencing User.id (user who liked the post).
        * post (ForeignKey): Foreign Key referencing Post.id (post being liked).
        * created_at (DateTimeField).

* **Comment:** Stores user comments on posts.
    * Attributes:
        * id (BigAuto): Primary Key.
        * owner (ForeignKey): Foreign Key referencing User.id (user who created the comment).
        * post (ForeignKey): Foreign Key referencing Post.id (post being commented on).
        * content (TextField).
        * created_at (DateTimeField).
        * updated_at (DateTimeField).

* **Follower:** Tracks user follow relationships.
    * Attributes:
        * id (BigAuto): Primary Key.
        * owner (ForeignKey): Foreign Key referencing User.id (user who follows someone).
        * followed (ForeignKey): Foreign Key referencing User.id (user being followed).
        * created_at (DateTimeField).

* **Favorite:** Tracks user favorite posts.
    * Attributes:
        * id (BigAuto): Primary Key.
        * owner (ForeignKey): Foreign Key referencing User.id (user who favorited the post).
        * post (ForeignKey): Foreign Key referencing Post.id (post being favorited).
        * created_at (DateTimeField).

### Relationships

* A User has a one-to-one relationship with a Profile.
* A User can follow many Users (many-to-many relationship) through Follower.
* A User can create many Posts (one-to-many relationship).
* A User can like many Posts (many-to-many relationship) through Like.
* A User can comment on many Posts (many-to-many relationship) through Comment.
* A User can favorite many Posts (many-to-many relationship) through Favorite.

---


## Packages

- [asgiref==3.8.1](https://pypi.org/project/asgiref/3.8.1/)
- [certifi==2024.6.2](https://pypi.org/project/certifi/2024.6.2/)
- [cffi==1.16.0](https://pypi.org/project/cffi/1.16.0/)
- [charset-normalizer==3.3.2](https://pypi.org/project/charset-normalizer/3.3.2/)
- [cloudinary==1.40.0](https://pypi.org/project/cloudinary/1.40.0/)
- [cryptography==42.0.8](https://pypi.org/project/cryptography/42.0.8/)
- [defusedxml==0.7.1](https://pypi.org/project/defusedxml/0.7.1/)
- [dj-database-url==2.2.0](https://pypi.org/project/dj-database-url/2.2.0/)
- [dj-rest-auth==6.0.0](https://pypi.org/project/dj-rest-auth/6.0.0/)
- [Django==4.2.9](https://pypi.org/project/Django/4.2.9/)
- [django-allauth==0.63.3](https://pypi.org/project/django-allauth/0.63.3/)
- [django-cloudinary-storage==0.3.0](https://pypi.org/project/django-cloudinary-storage/0.3.0/)
- [django-cors-headers==4.4.0](https://pypi.org/project/django-cors-headers/4.4.0/)
- [django-countries==7.6.1](https://pypi.org/project/django-countries/7.6.1/)
- [django-filter==24.2](https://pypi.org/project/django-filter/24.2/)
- [django-model-utils==4.5.1](https://pypi.org/project/django-model-utils/4.5.1/)
- [djangorestframework==3.15.2](https://pypi.org/project/djangorestframework/3.15.2/)
- [djangorestframework-simplejwt==5.3.1](https://pypi.org/project/djangorestframework-simplejwt/5.3.1/)
- [gunicorn==22.0.0](https://pypi.org/project/gunicorn/22.0.0/)
- [idna==3.7](https://pypi.org/project/idna/3.7/)
- [jsonfield==3.1.0](https://pypi.org/project/jsonfield/3.1.0/)
- [oauthlib==3.2.2](https://pypi.org/project/oauthlib/3.2.2/)
- [pillow==10.3.0](https://pypi.org/project/Pillow/10.3.0/)
- [psycopg2==2.9.9](https://pypi.org/project/psycopg2/2.9.9/)
- [pycparser==2.22](https://pypi.org/project/pycparser/2.22/)
- [PyJWT==2.8.0](https://pypi.org/project/PyJWT/2.8.0/)
- [python3-openid==3.2.0](https://pypi.org/project/python3-openid/3.2.0/)
- [pytz==2024.1](https://pypi.org/project/pytz/2024.1/)
- [requests==2.32.3](https://pypi.org/project/requests/2.32.3/)
- [requests-oauthlib==2.0.0](https://pypi.org/project/requests-oauthlib/2.0.0/)
- [sqlparse==0.5.0](https://pypi.org/project/sqlparse/0.5.0/)
- [swapper==1.3.0](https://pypi.org/project/swapper/1.3.0/)
- [urllib3==2.2.2](https://pypi.org/project/urllib3/2.2.2/)
- [whitenoise==6.7.0](https://pypi.org/project/whitenoise/6.7.0/)

---

## Technologies Used

### Languages
- **Python:** The core programming language used to write this API.

### Frameworks
- **Django:** The main framework providing the foundation for this API.
- **Django REST Framework:** Builds on top of Django to create RESTful APIs.

### Libraries

#### Authentication
- **dj-rest-auth:** Simplifies the creation of authentication endpoints with Django REST Framework.
- **django-allauth:** A comprehensive authentication app for Django.
- **djangorestframework-simplejwt:** JSON Web Token (JWT) based authentication for secure frontend communication.

#### Database
- **dj-database-url:** Helps parse URLs for easy configuration in Django.
- **psycopg2:** A PostgreSQL adapter for Python.

#### Image Handling
- **cloudinary:** Facilitates interaction with Cloudinary for cloud-based image storage.
- **django-cloudinary-storage:** Integrates Cloudinary for media storage in Django.
- **Pillow:** Used for image processing tasks.

#### Utilities
- **gunicorn:** A WSGI server for deploying the application in production.
- **django-cors-headers:** Adds Cross-Origin Resource Sharing headers to allow requests from different origins.
- **django-taggit:** Adds tagging functionality to posts, making content easier to search.

### Database
- **PostgreSQL:** Used as the database for this project, hosted on Elephant SQL.

### Image Storage
- **Cloudinary:** Utilized for storing images in the cloud.

### Deployment Service
- **Heroku:** The platform used to deploy this project.

---

## Deployment

### Database Setup
1. Set up a PostgreSQL database on [ElephantSQL](https://www.elephantsql.com/).

### Heroku Configuration
1. Create an app on Heroku.
2. On the Heroku app's settings page, add the following config vars:
   - `DATABASE_URL`: Your PostgreSQL server URL.
   - `SECRET_KEY`: A secret key from [Djecrety](https://djecrety.ir/).
   - `DISABLE_COLLECTSTATIC`: `1`.
   - `CLOUDINARY_URL`: Your Cloudinary API environment variable.

### Local Environment Setup
1. Install necessary packages:

    ```bash
    pip install dj_database_url psycopg2
    ```

2. Import `dj_database_url` in `settings.py`.

3. Update the `DATABASES` configuration in `settings.py`:

    ```python
    if 'DEV' in os.environ:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
    else:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
        }
        print("Connected to external database")
    ```

4. Add the database URL to `env.py`:

    ```python
    os.environ['DATABASE_URL'] = 'your-ElephantSQL-database-url'
    os.environ['DEV'] = '1'  # Temporarily comment this out to connect to the external database
    ```

5. Verify the connection to the external database:

    ```bash
    python manage.py makemigrations --dry-run
    ```

    Ensure "Connected to external database" is printed, then remove the print statement and run:

    ```bash
    python manage.py migrate
    ```

6. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

    Verify the superuser in ElephantSQL under "Table queries" > "auth_user".

### Additional Packages
1. Install Gunicorn and Django CORS Headers:

    ```bash
    pip install gunicorn django-cors-headers
    ```

2. Save the installed packages to `requirements.txt`:

    ```bash
    pip freeze --local > requirements.txt
    ```

3. Create a `Procfile` in the root directory:

    ```plaintext
    release: python manage.py makemigrations && python manage.py migrate
    web: gunicorn blog_beat_api.wsgi
    ```

4. Update `ALLOWED_HOSTS` in `settings.py`:

    ```python
    ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOST')]
    ```

    Add the environment variable in `env.py`:

    ```python
    os.environ['ALLOWED_HOST'] = 'your-gitpod-workspace-url'
    ```

### CORS Configuration
1. Add `'corsheaders'` to `INSTALLED_APPS` in `settings.py`.
2. Add `'corsheaders.middleware.CorsMiddleware'` to the top of the `MIDDLEWARE` list.
3. Configure allowed origins for CORS:

    ```python
    if 'CLIENT_ORIGIN' in os.environ:
        CORS_ALLOWED_ORIGINS = [os.environ.get('CLIENT_ORIGIN')]

    if 'CLIENT_ORIGIN_DEV' in os.environ:
        extracted_url = re.match(r'^.+-', os.environ.get('CLIENT_ORIGIN_DEV', ''), re.IGNORECASE).group(0)
        CORS_ALLOWED_ORIGIN_REGEXES = [rf"{extracted_url}(eu|us)\d+\w\.gitpod\.io$"]
    ```

4. Enable cross-origin credentials:

    ```python
    CORS_ALLOW_CREDENTIALS = True
    ```

5. Set JWT authentication settings:

    ```python
    REST_AUTH = {
        'USE_JWT': True,
        'JWT_AUTH_SECURE': True,
        'JWT_AUTH_COOKIE': 'my-app-auth',
        'JWT_AUTH_REFRESH_COOKIE': 'my-refresh-token',
        'JWT_AUTH_SAMESITE': 'None',
        'USER_DETAILS_SERIALIZER': 'blog_beat_api.serializers.CurrentUserSerializer'
    }
    ```

### Secret Key and Debug Configuration
1. Set the `SECRET_KEY` in `env.py`:

    ```python
    os.environ.setdefault("SECRET_KEY", "MyNewRandomValueHere")
    ```

2. Update `SECRET_KEY` in `settings.py`:

    ```python
    SECRET_KEY = os.getenv('SECRET_KEY')
    ```

3. Set the `DEBUG` value in `settings.py`:

    ```python
    DEBUG = 'DEV' in os.environ
    ```

### Final Steps
1. Ensure `requirements.txt` is up to date and push to GitHub.
2. On Heroku, connect the app to your GitHub repository under the deploy tab.
3. Click "Deploy Branch". After deployment, ensure the app works as expected.

### Cloning and Forking
1. Clone or fork the project from [GitHub](https://github.com/j0hanz/blog_beat_api).

2. Set up a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up your own environment variables in an `env.py` file.

By following these steps, you can successfully deploy and set up the Blog Beat API.

## Credits

This project was inspired by the [Moments DRF API](https://github.com/Code-Institute-Solutions/drf-api/tree/master) project by Code Institute. The Moments project served as a valuable reference, influencing several code implementations in this API.
