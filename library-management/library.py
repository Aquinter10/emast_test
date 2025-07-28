def gettitle(s):
    colon_index = s.find(":")
    if colon_index == -1:
        return ""
    comma_index = s.find(",", colon_index)
    if comma_index == -1:
        return s[colon_index + 1:].strip()
    return s[colon_index + 1:comma_index].strip()

class Library:
    def __init__(self):
        self.items = []
        self.borrowed_items = []

    def add_item(self, item):
        self.items.append(item)

    def borrow_item(self, item_name):
        for item in self.items:
            if gettitle(item.get_details()) == item_name and item_name not in self.borrowed_items:
                self.borrowed_items.append(item)
                return f"You have borrowed '{item_name}'."
        return f"'{item_name}' is not available for borrowing."

    def return_item(self, item_name):
        if item_name in self.borrowed_items:
            del self.borrowed_items[item_name]
            return f"You have returned '{item_name}'."
        return f"'{item_name}' was not borrowed."


    def list_available_items(self):
        return [item.get_details() for item in self.items if item not in self.borrowed_items]
    
    def list_borrowed_items(self):
        return [item.get_details() for item in self.items if item in self.borrowed_items]

    def most_borrowed_item(self):
        if not self.borrowed_items:
            return "No items have been borrowed."
        item_counts = {}
        for item in self.borrowed_items:
            
            title = gettitle(item.get_details())
            item_counts[title] = item_counts.get(title, 0) + 1
        most_borrowed = max(item_counts, key=item_counts.get)
        return f"The most borrowed item is '{most_borrowed}'."