def get_component(subtree, selector, attribute=None, return_list=False):
    try:
        if attribute:
            return subtree.select(selector).pop(0)[attribute].strip()
        if return_list:
            return [item.get_text().strip() for item in subtree.select(selector)]
        return subtree.select(selector).pop(0).get_text().strip()
    except IndexError:
        return None