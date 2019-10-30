# extract valid data used for updating to avoid overwriting info with empty data
def get_valid_update_info(data_object):
    update_info = {}
    for attr in data_object:
        if data_object[attr] != "" and data_object[attr] != None:
            update_info[attr] = data_object[attr]
    return update_info


def check_logged_in(active_users, email):
    for user_id in active_users:
        if active_users[user_id]["email"] == email:
            return True
    return False