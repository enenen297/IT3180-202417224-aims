def search_by_title(items, title):
    return [item for item in items if title.strip().lower() in item.title.lower()]