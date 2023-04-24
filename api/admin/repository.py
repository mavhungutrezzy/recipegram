from .models import Admin


async def add_admin(new_admin: Admin) -> Admin:
    return await new_admin.create()
