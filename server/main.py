import logging
from concurrent import futures

import grpc

from grpc_module.items_pb2_grpc import add_ItemServiceServicer_to_server
from grpc_module import items_pb2_grpc
from grpc_module.items_pb2 import Item, ItemResponse, Empty

from db import crud


class ItemServiceServicer(items_pb2_grpc.ItemServiceServicer):
    """Provides methods that implement functionality of route guide server."""

    def GetById(self, request, context):
        item = crud.get_item(request.id)
        if not item:
            return Item(id=-1, name="", description="")

        return Item(id=item.id, name=item.name, description=item.description)

    def PutItem(self, request, context):
        item = crud.create_item(request.name, request.description)
        return ItemResponse(item={'id': item.id, 'name': item.name, 'description': item.description})

    def DeleteById(self, request, context):
        crud.delete_item(request.id)
        return Empty()

    def GetManyItems(self, request, context):
        items = crud.get_items(request.page_number, request.page_length)
        for item in items:
            yield Item(id=item.id, name=item.name, description=item.description)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_ItemServiceServicer_to_server(
        ItemServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
