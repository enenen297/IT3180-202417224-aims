def search_by_title(items, title):
    return [item for item in items if title.lower() in item.title.lower()]