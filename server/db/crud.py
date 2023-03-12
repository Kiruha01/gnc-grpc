from .model import Session, Item


def create_item(name, description):
    with Session() as session:
        item = Item(name=name, description=description)
        session.add(item)
        session.commit()
        item = session.query(Item).filter_by(id=item.id).first()
    return item


# get an item by id
def get_item(id):
    session = Session()
    item = session.query(Item).filter_by(id=id).first()
    session.close()
    return item


# delete an item by id
def delete_item(id):
    session = Session()
    item = session.query(Item).filter_by(id=id).first()
    session.delete(item)
    session.commit()
    session.close()


# get many items with paging
def get_items(page=1, per_page=10):
    session = Session()
    items = session.query(Item).offset((page-1)*per_page).limit(per_page).all()
    session.close()
    return items
