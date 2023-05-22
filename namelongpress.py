def isLongPressedName(name: str, typed: str) -> bool:
    i, j = 0, 0  # Pointers for name and typed strings

    while j < len(typed):
        # Check if characters match
        if i < len(name) and name[i] == typed[j]:
            i += 1
            j += 1
        # Check for long key press in typed
        elif j > 0 and typed[j] == typed[j - 1]:
            j += 1
        else:
            return False

    # Ensure name string is fully traversed
    return i == len(name)
