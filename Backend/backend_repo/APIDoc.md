### API Documentation

#### Endpoint: `api/posts/`
**Method**: GET  
**Query Parameters**:
- `page`: (optional) Page number for pagination.
- `page_size`: (optional) Number of posts per page.

**Response**:
```json
{
    "count": 50,
    "next": "http://localhost:8000/api/posts/?page=2",
    "previous": null,
    "results": [
        {
            "id": "uuid",
            "text": "Post text",
            "timestamp": "2024-12-27T00:00:00Z",
            "user": "username",
            "comment_count": 3,
            "comments": [
                {
                    "text": "Comment text",
                    "timestamp": "2024-12-27T00:00:00Z",
                    "user": "commenter_username"
                },
                ...
            ]
        },
        ...
    ]
}
