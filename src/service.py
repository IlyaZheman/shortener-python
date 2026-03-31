from src.database.crud import add_slug_to_database, get_long_url_by_slug_from_database
from src.exceptions import NoLongUrlFoundException
from src.shortener import generate_random_slug


async def generate_short_url(
        long_url: str,
) -> str:
    slug = generate_random_slug()
    await add_slug_to_database(
        slug=slug,
        long_url=long_url
    )
    return slug


async def get_long_url_by_slug(slug: str) -> str:
    long_url = await get_long_url_by_slug_from_database(slug)
    if not long_url:
        raise NoLongUrlFoundException()
    return long_url
