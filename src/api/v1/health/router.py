from fastapi import APIRouter, status


router = APIRouter(prefix=f"/health")


@router.get("/", status_code=status.HTTP_200_OK)
async def health_check():
    """
    Check if services is healthy and responsing with 200 code.

    :return: Dictionary with message that confirms that service is healthy
    :rtype: dict
    """
    return {"message": "Healthy"}
