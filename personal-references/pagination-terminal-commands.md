# Terminal commands for Pagination

- python3
- from flaskblog.models import Post
- Post.query.all() # To get all the posts
    ```python
    posts = Post.query.all()
    for post in posts:
        print(post)
    ```
- posts = Post.query.paginate() # To get all the posts with pagination
- dir(posts) # To get all the attributes and methods of the object
- posts.per_page # To get the number of posts per page. The default is 20.
    ```python
    posts = Post.query.paginate(page=1, per_page=5)
    for post in posts.items:
        print(post)
    ```
- posts.has_next # To check if there is a next page
- posts.has_prev # To check if there is a previous page
- posts.next_num # To get the number of the next page
- posts.prev_num # To get the number of the previous page
- posts.pages # To get the total number of pages
- if you wanna check the page 2,
    ```python
    posts = Post.query.paginate(page=2, per_page=5)
    for post in posts.items:
        print(post)
    ```
- posts = Post.query.paginate(per_page=5) # To get the first page with 5 posts
- posts.total # To get the total number of posts

while scrolling through normal posts database, you might call it using `for post in posts`, but when it is paginated, you must use `for post in posts.items` to get the posts.

