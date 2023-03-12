import sys

import grpc

from grpc_module.items_pb2_grpc import ItemServiceStub
from grpc_module.items_pb2 import Item, ItemRequest, PaginationRequest


def create_item(stub):
    name = input("Name: ")
    description = input("Description: ")
    response = stub.PutItem(Item(name=name, description=description))
    print("Item created with id {}".format(response.item.id))


def delete_item(stub):
    id = input("Id: ")
    while not id.isdigit():
        id = input("Invalid id.\nId: ")

    id = int(id)
    stub.DeleteById(ItemRequest(id=id))
    print("Item deleted with id {}".format(id))


def get_item(stub):
    id = input("Id: ")
    while not id.isdigit():
        id = input("Invalid id.\nId: ")

    id = int(id)
    item = stub.GetById(ItemRequest(id=id))
    if item.id == -1:
        print("Item not found")
        return

    print("Item with id {}".format(id))
    print("\tName: {}".format(item.name))
    print("\tDescription: {}".format(item.description))


def get_many_items(stub):
    page = input("Page: ")
    while not page.isdigit():
        page = input("Invalid page.\nPage: ")

    page = int(page)
    per_page = input("Per page: ")
    while not per_page.isdigit():
        per_page = input("Invalid per page.\nPer page: ")

    per_page = int(per_page)
    items = stub.GetManyItems(PaginationRequest(page_number=page, page_length=per_page))

    for item in items:
        print("Id: {}".format(item.id))
        print("Name: {}".format(item.name))
        print("Description: {}".format(item.description))
        print()


def process(command: str, stub):
    if command == "\\h":
        print(
"""
Commands:
* \\h - help
* \\q - quit

* \\c - create item
* \\d - delete item
* \\g - get item
* \\gs - get many items
"""
)
    elif command == "\\q":
        sys.exit(1)
    elif command == "\\c":
        create_item(stub)
    elif command == "\\d":
        delete_item(stub)
    elif command == "\\g":
        get_item(stub)
    elif command == "\\gs":
        get_many_items(stub)


if __name__ == '__main__':
    print("Items client. Type \\h for help.")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = ItemServiceStub(channel)
        while True:
            command = input(">> ")
            process(command.strip(), stub)
