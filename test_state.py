from brain.state_manager import (
    set_pending,
    get_pending,
    clear_pending
)


set_pending({
    "action": "delete",
    "name": "notes.txt"
})


print(get_pending())


clear_pending()


print(get_pending())