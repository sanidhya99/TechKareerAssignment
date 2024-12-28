import uuid
from faker import Faker
from django.core.management.base import BaseCommand
from apps.demo.models import Post, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = "Populates the database with sample posts and comments"

    def handle(self, *args, **kwargs):
        fake = Faker()

        try:
            # Fetch the user with ID 1
            user = User.objects.get(id=1)
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR("User with ID 1 does not exist. Please create it first."))
            return

        num_posts = 10  # Number of posts to create
        comments_per_post = 5  # Number of comments per post

        # Create posts
        for _ in range(num_posts):
            post = Post.objects.create(
                id=uuid.uuid4(),
                text=fake.text(max_nb_chars=200),
                user=user
            )

            # Create comments for each post
            for _ in range(comments_per_post):
                Comment.objects.create(
                    id=uuid.uuid4(),
                    text=fake.text(max_nb_chars=100),
                    post=post,
                    user=user
                )

        self.stdout.write(self.style.SUCCESS(
            f"Database populated with {num_posts} posts and {num_posts * comments_per_post} comments, all by user ID 1."
        ))
