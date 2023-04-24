from typing import Type


class BaseRepository:
    def __init__(self, model: Type):
        self.model = model

    async def add(self, new_item: Type) -> Type:
        return await new_item.create()

    async def get_all(self) -> list:
        return await self.model.all().to_list()

    async def get(self, id: int) -> Type:
        item = await self.model.get(id)
        if item:
            return item

    async def delete(self, id: int) -> bool:
        item = await self.model.get(id)
        if item:
            await item.delete()
            return True

    async def update(self, id: int, data: dict) -> Type:
        des_body = {k: v for k, v in data.items() if v is not None}
        update_query = {"$set": dict(des_body)}
        item = await self.model.get(id)
        if item:
            await item.update(update_query)
            return item
        return False

    async def get_by(self, **kwargs) -> Type:
        item = await self.model.find_one(**kwargs)
        if item:
            return item

    async def get_all_by(self, **kwargs) -> list:
        items = await self.model.find(**kwargs).to_list()
        if items:
            return items

    async def delete_by(self, **kwargs) -> bool:
        item = await self.model.find_one(**kwargs)
        if item:
            await item.delete()
            return True

    async def update_by(self, data: dict, **kwargs) -> Type:
        des_body = {k: v for k, v in data.items() if v is not None}
        update_query = {"$set": dict(des_body)}
        item = await self.model.find_one(**kwargs)
        if item:
            await item.update(update_query)
            return item
        return False

    async def delete_all(self) -> bool:
        await self.model.delete_many({})
        return True

    async def delete_all_by(self, **kwargs) -> bool:
        await self.model.delete_many(kwargs)
        return True

    async def count(self) -> int:
        return await self.model.count_documents({})

    async def count_by(self, **kwargs) -> int:
        return await self.model.count_documents(kwargs)

    async def exists(self, **kwargs) -> bool:
        return await self.model.exists(**kwargs)
