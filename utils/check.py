def check_prefix(content, prefix_list):
    for prefix in prefix_list:
        if content.startswith(prefix):
            return prefix
    return None

def check_keyword(content, keyword_list):
    for keyword in keyword_list:
        if keyword in content:
            return keyword
    return None

def is_wx_account(id):
    if id is None:
        return False
    return not id.lower().startswith("gh_")
