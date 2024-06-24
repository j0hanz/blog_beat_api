### Database Structure

This document provides a detailed overview of Blog Beat's database schema, including the tables, their attributes, and the relationships between them. The database stores information about users, profiles, posts, comments, likes, favorites, followers, and social media links.

![Blog Beat API](https://github.com/j0hanz/blog_beat_api/assets/159924955/24f39e32-d3ab-462d-988b-136f5fa4fef0)

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
        * favourites (ManyToManyField): Many-to-many relationship with User (users who favourited this post).
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
* **SocialMediaLink:** Stores links to social media profiles of a user.
    * Attributes:
        * id (BigAuto): Primary Key.
        * owner (ForeignKey): Foreign Key referencing User.id (user who owns the link).
        * platform (CharField).
        * url (URLField).

### Relationships

* A User has a one-to-one relationship with a Profile.
* A User can follow many Users (many-to-many relationship) through Follower.
* A User can create many Posts (one-to-many relationship).
* A User can like many Posts (many-to-many relationship) through Like.
* A User can comment on many Posts (many-to-many relationship) through Comment.
* A User can favorite many Posts (many-to-many relationship) through the favourites field of Post.
* A User can have many SocialMediaLinks (one-to-many relationship).
