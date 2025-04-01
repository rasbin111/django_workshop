from django.db import models


class Author(models.Model):
    """
    Represents an author with a name attribute.

    Attributes:
        name (CharField): The name of the author, limited to 100 characters.

    Methods:
        __str__(): Returns the string representation of the author's name.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Post(models.Model):
    """
    Represents a blog post with a title, content, and an associated author.

    Attributes:
        title (CharField): The title of the post, limited to 100 characters.
        content (TextField): The main content of the post.
        author (ForeignKey): A reference to the Author model, with a cascade delete behavior.

    Methods:
        __str__(): Returns the string representation of the post's title.
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)
