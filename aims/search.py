def search_by_category(items, category):
    return [dvd for dvd in items if category.lower() == dvd.category.lower()]

def search_by_title(items, title):
    return [item for item in items if title.lower() in item.title.lower()]