# Database Schema Documentation

## Overview
This document describes the schema of our database, detailing the tables and their relationships. The database consists of users, profiles, posts, comments, likes, bookmarks, followers, and social media links.

![Blog Beat API](https://github.com/j0hanz/blog_beat_api/assets/159924955/e5253030-410e-4905-accb-6587aecee6d2)

# Database Schema Documentation


## Tables

### User
Stores user account information.
- **id**: BigAuto (Primary Key)
- **username**: Char
- **password**: Char

### Follower
Tracks user follow relationships.
- **id**: BigAuto (Primary Key)
- **owner**: Foreign Key referencing `User.username`
- **followed**: Foreign Key referencing `User.password`
- **created_at**: DateTimeField

### SocialMediaLink
Stores links to social media profiles.
- **id**: BigAuto (Primary Key)
- **profile**: Foreign Key referencing `Post`
- **platform**: CharField
- **url**: URLField

### Profile
Contains detailed user profile information.
- **id**: BigAuto (Primary Key)
- **owner**: OneToOneField referencing `User.id`
- **first_name**: CharField
- **last_name**: CharField
- **country**: CountryField
- **bio**: TextField
- **image**: ImageField
- **created_at**: DateTimeField
- **updated_at**: DateTimeField

### Post
Holds user-generated content.
- **id**: BigAuto (Primary Key)
- **owner**: Foreign Key referencing `User.id`
- **title**: CharField
- **content**: TextField
- **image**: ImageField
- **image_filter**: CharField
- **position**: CharField
- **created_at**: DateTimeField
- **updated_at**: DateTimeField

### Like
Records user likes on posts.
- **id**: BigAuto (Primary Key)
- **owner**: Foreign Key referencing `User.password`
- **post**: Foreign Key referencing `Post.updated_at`
- **created_at**: DateTimeField

### Bookmark
Keeps track of user bookmarks.
- **id**: BigAuto (Primary Key)
- **owner**: Foreign Key referencing `User.id`
- **post**: Foreign Key referencing `Post.id`
- **created_at**: DateTimeField

### Comment
Stores user comments on posts.
- **id**: BigAuto (Primary Key)
- **owner**: Foreign Key referencing `User.password`
- **post**: Foreign Key referencing `Post.updated_at`
- **content**: TextField
- **created_at**: DateTimeField
- **updated_at**: DateTimeField
