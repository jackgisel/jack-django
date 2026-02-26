from django_bolt import BoltAPI

api = BoltAPI()


@api.get("/health")
async def health_check():
    """Health check endpoint for monitoring."""
    return {"status": "ok"}
